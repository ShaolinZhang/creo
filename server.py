import os
from flask import Flask, request, render_template, g, redirect, Response, session, send_from_directory

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)

@app.before_request
def before_request():
    pass

@app.teardown_request
def teardown_request(exception):
    pass

@app.route('/', methods = ['GET', 'POST'])
def index():
    pass

if __name__ == "__main__":

    import click

    @click.command()
    @click.option('--debug', is_flag=True)
    @click.option('--threaded', is_flag=True)
    @click.argument('HOST', default='0.0.0.0')
    @click.argument('PORT', default=8080, type=int) # customize

    def run(debug, threaded, host, port):
        HOST, PORT = host, port
        print("running on %s:%d" % (HOST, PORT))
        app.config['SESSION_TYPE'] = 'filesystem'
        app.run(host=HOST, port=PORT, debug=True, threaded=True)

    run()
