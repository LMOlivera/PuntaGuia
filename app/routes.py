from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def bienvenido():
    return render_template('bienvenido.html')

@app.route('/index/registro')
def registro():
    return render_template('registro.html')


@app.route('/principal')
def index():
    return render_template('index.html', title='Inicio')

