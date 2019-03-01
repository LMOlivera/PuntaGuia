from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm
import pymysql

# Hay que revisar esto, tal vez se pueda mejorar
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def bienvenido():
    form = LoginForm() # Formulario de forms.py, se importa
    if form.validate_on_submit(): #Al submitear data se corre esto
        # BASE DE DATOS!!!
        db = pymysql.connect("localhost", "root", "", "uruguia_bd_test")
        cursor = db.cursor()
        sql = "SELECT * FROM usuario"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        #####################

        # Manda un mensaje, podrás verlo comentado en bienvenido.html
        #flash('Login requested for user {}, remember_me={}'.format(
        #    form.username.data, form.remember_me.data))
        return redirect('/principal')
    return render_template('bienvenido.html', form=form)

@app.route('/index/registro')
def registro():
    return render_template('registro.html')

@app.route('/principal')
def index():
    return render_template('principal.html')