from flask import render_template, flash, redirect, session, request
from app import app
from app.forms import LoginForm, RegisterForm
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
            query = "SELECT id_usuario, email, nombre, tipo FROM usuario WHERE email=%s AND contrasena=%s"
            cursor.execute(query,(email,password))
            userdata = cursor.fetchone()
            results = cursor.rowcount
            if results==0:
                flash('Usuario y/o contraseña inválidos')                
                session['invalid_user']="true"               
                return redirect('/')
            else:
                session.pop('invalid_user', None)
                session['id_usuario'] = userdata['id_usuario']
                session['email'] = userdata['email']
                session['nombre'] = userdata['nombre']
                session['tipo'] = userdata['tipo']
                return redirect('/principal')
    return render_template('bienvenido.html', form=form)

@app.route('/index/registro', methods=['GET', 'POST'])
def registro():
    nuevo = request.args.to_dict()
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            with connection.cursor() as cursor:
                email = form.email.data
                nombre = form.nombre.data
                password = form.password.data
                tipo = nuevo['tipo']
                query = """
                INSERT INTO usuario
                (email,nombre,contrasena,tipo)
                VALUES
                (%s,%s,%s,%s)
                """
                cursor.execute(query,(email,nombre,password,tipo))
                query = """
                SELECT id_usuario FROM usuario
                WHERE email=%s
                """
                cursor.execute(query,(email))
                userdata = cursor.fetchone()
                id_usuario=userdata['id_usuario']

                if nuevo['tipo']=='turista':
                    edad = form.edad.data
                    pais = form.pais.data
                    query = """
                    INSERT INTO turista
                    (id,edad,pais_origen)
                    VALUES
                    (%s,%s,%s)
                    """
                    cursor.execute(query,(id_usuario,edad,pais))
                else:
                    nombreEmpresa = form.nombreEmpresa.data
                    query = """
                    INSERT INTO empresa
                    (id,nombre)
                    VALUES
                    (%s,%s)
                    """
                    cursor.execute(query,(id_usuario,nombreEmpresa))
            connection.commit()
            session.clear()
            return redirect('/index') 
        except NameError:    
                print('Algo malo acaba de ocurrir: ' + NameError)
        
    return render_template('registro.html', form=form,tipo=nuevo['tipo'])

@app.route('/principal')
def index():
    return render_template('principal.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')