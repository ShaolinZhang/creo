import os
from flask import Flask, request, render_template, g, redirect, session
from sqlalchemy import create_engine
from werkzeug.security import generate_password_hash, check_password_hash

from dotenv import load_dotenv

tmpl_dir = os.path.join(os.path.dirname(
    os.path.abspath(__file__)),
    'templates'
)
app = Flask(__name__, template_folder=tmpl_dir)

load_dotenv('.env.dev')

DATABASEURI = 'mysql://' + os.getenv("USERNAME") + ':' + \
    os.getenv("PASSWORD") + '@' + os.getenv("HOSTNAME") + \
    '/' + os.getenv("DATABASE_NAME") + '?charset=utf8'
engine = create_engine(DATABASEURI)

context = dict()
context['company_name'] = os.getenv("COMPANY_NAME")


@app.before_request
def before_request():
    try:
        g.conn = engine.connect()
    except Exception:
        print("uh oh, problem connecting to database")
        import traceback
        traceback.print_exc()
        g.conn = None


@app.teardown_request
def teardown_request(exception):
    try:
        g.conn.close()
    except Exception:
        pass


@app.route('/', methods=['GET', 'POST'])
def index():
    context['page_name'] = 'Home'
    if session.get('user'):
        context['username'] = session['user']
        return render_template("home.html", **context)
    else:
        return redirect("/login")


@app.route('/login', methods=["GET", "POST"])
def login():
    context['page_name'] = 'Log In'
    session.clear()
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        query_result = g.conn.execute(
            'SELECT * FROM user WHERE username=%s',
            username
        ).fetchone()
        if query_result is not None:
            if check_password_hash(query_result[2], password):
                session.clear()
                session['user'] = username
                return redirect('/')
            else:
                context['login_error_msg'] = 'Incorrect password.'
                return render_template("login.html", **context)
        else:
            context['error_msg'] = 'User does not exist.'
            return render_template("login.html", **context)
    return render_template("login.html", **context)


@app.route('/signup', methods=["GET", "POST"])
def signup():
    context['page_name'] = 'Sign Up'
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        try:
            g.conn.execute(
                'INSERT INTO user(username, email, password) VALUES \
                (%s, %s, %s)', username, email,
                generate_password_hash(password)
            )
        except Exception:
            context['signup_error_msg'] = 'Username already exists.'
            return render_template("signup.html", **context)
        return redirect('/login')
    return render_template("signup.html", **context)


@app.route('/logout', methods=["GET", "POST"])
def logout():
    session.clear()
    return redirect('/login')


if __name__ == "__main__":

    import click

    @click.command()
    @click.option('--debug', is_flag=True)
    @click.option('--threaded', is_flag=True)
    @click.argument('HOST', default='0.0.0.0')
    @click.argument('PORT', default=8080, type=int)
    def run(debug, threaded, host, port):
        HOST, PORT = host, port
        print("running on %s:%d" % (HOST, PORT))
        app.secret_key = os.getenv("SECRET_KEY")
        app.config['SESSION_TYPE'] = 'filesystem'
        app.run(host=HOST, port=PORT, debug=True, threaded=True)

    run()
