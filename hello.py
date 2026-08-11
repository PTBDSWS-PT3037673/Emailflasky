from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment

from datetime import datetime


app = Flask(__name__)

bootstrap = Bootstrap(app)
moment = Moment(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/')
def index():
	return render_template('index.html', current_time=datetime.utcnow(), name='Joshua Merces')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/contextorequisicao/<name>')
def contextorequisicao(name):
    user_agent = request.headers.get('User-Agent')
    remote_ip = request.remote_addr
    host = request.host

    return render_template(
        'contextorequisicao.html',
        name=name,
        user_agent=user_agent,
        remote_ip=remote_ip,
        host=host
    )