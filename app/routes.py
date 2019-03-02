from flask import render_template, flash, redirect, session
from app import app
from app.forms import LoginForm
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='uruguia_bd_test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def bienvenido():
    form = LoginForm() # Formulario de forms.py, se importa
    if form.validate_on_submit(): #Al submitear data se corre esto
        with connection.cursor() as cursor:
            email=form.email.data
            password=form.password.data
            query = "SELECT 1 FROM usuario WHERE email=%s AND contrasena=%s"
            cursor.execute(query,(email,password))
            #results = cursor.fetchall()
            # connection.commit()
            results = cursor.rowcount
            if results==0:
                flash('El usuario que acabas de ingresar no existe')                
                session['invalid_user']="true"               
                return redirect('/')
            return redirect('/principal')
        # Manda un mensaje, podrás verlo comentado en bienvenido.html
        #flash('Login requested for user {}, remember_me={}'.format(
        #    form.username.data, form.remember_me.data))
    return render_template('bienvenido.html', form=form)

@app.route('/index/registro')
def registro():
    return render_template('registro.html')

@app.route('/principal')
def index():
    session.pop('invalid_user', None)
    return render_template('principal.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')