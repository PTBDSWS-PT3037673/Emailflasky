from flask import Flask, abort, request, make_response, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Hello World!</h1> <b><h2>Disciplina PTBDSWS</h2>"

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/contextorequisicao')
def contextorequisicao():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)

@app.route('/codigostatusdiferente')
def badrequest():
    abort(400)

@app.route('/objetorespotas')
def objeto_resposta():
    resp = make_response('<h1>This document carries a cookie</h1>')
    resp.set_cookie('nome_cookie', 'valor')
    return resp

@app.route('/redirecionamento')
def redirecionar():
    return redirect('https://ptb.ifsp.edu.br')

@app.route('/abortar')
def abortar():
    abort(404)