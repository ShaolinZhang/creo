import os
from flask import Flask, request, render_template, g, redirect, Response, session, send_from_directory
from sqlalchemy import *
from sqlalchemy.pool import NullPool

from dotenv import load_dotenv

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)

load_dotenv('.env.dev')

DATABASEURI = 'mysql://' + os.getenv("USERNAME") + ':' + os.getenv("PASSWORD") + '@' + os.getenv("HOSTNAME") + '/' + os.getenv("DATABASE_NAME") + '?charset=utf8'
engine = create_engine(DATABASEURI)

context = dict()
context['company_name'] = os.getenv("COMPANY_NAME")

@app.before_request
def before_request():
    try:
        g.conn = engine.connect()
    except:
        print("uh oh, problem connecting to database")
        import traceback
        traceback.print_exc()
        g.conn = None

@app.teardown_request
def teardown_request(exception):
    try:
        g.conn.close()
    except Exception as e:
        pass

@app.route('/', methods = ['GET', 'POST'])
def index():
    context['page_name'] = 'Home'
    return render_template("home.html", **context)

if __name__ == "__main__":

    import click

    @click.command()
    @click.option('--debug', is_flag=True)
    @click.option('--threaded', is_flag=True)
    @click.option('--test', is_flag=True)
    @click.argument('HOST', default='0.0.0.0')
    @click.argument('PORT', default=8080, type=int) # customize

    def run(debug, threaded, host, port):
        HOST, PORT = host, port
        print("running on %s:%d" % (HOST, PORT))
        app.config['SESSION_TYPE'] = 'filesystem'
        app.run(host=HOST, port=PORT, debug=True, threaded=True)

    run()
