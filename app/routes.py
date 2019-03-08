from flask import render_template, flash, redirect, session, request
from app import app, logic
from app.logic import clsSqlSelect, clsSqlInsert, clsSqlDelete
from app.forms import LoginForm, RegisterForm, ModifyForm, AgregarLugar
import pymysql.cursors

# En cuanto se termine el refactor hay que borrar esto
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='uruguia_bd_test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def bienvenido():
    if session.get('logueado'):
        return redirect('/principal')
    else:        
        form = LoginForm()
        if form.validate_on_submit():
            SqlSelect = clsSqlSelect.SqlSelect()
            email=form.email.data
            password=form.password.data
            if SqlSelect.login(email, password):
                session.pop('invalid_user', None)
                session['logueado']=True
                session['id_usuario'] = SqlSelect.userdata['id_usuario']
                session['email'] = SqlSelect.userdata['email']
                session['nombre'] = SqlSelect.userdata['nombre']
                session['tipo'] = SqlSelect.userdata['tipo']
                del SqlSelect
                return redirect('/principal')
            else:
                flash('Usuario y/o contraseña inválidos')                
                session['invalid_user']="true"               
                return redirect('/')                    
    return render_template('bienvenido.html', title='¡Bienvenido a UruGuia!', form=form)

# PENDIENTE
@app.route('/index/registro', methods=['GET', 'POST'])
def registro():
    if session.get('logueado'):
        return redirect('/principal')   
    else:        
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
    return render_template('registro.html', title="Registrar un nuevo usuario", form=form, tipo=nuevo['tipo'])

# PENDIENTE
@app.route('/principal')
def index():
    if session.get('logueado'):
        print('ok')
    else:
        session.clear()
        return redirect('/')
    return render_template('principal.html', title="Página principal")

# PENDIENTE
@app.route('/principal/usuario')
def usuario():
    if not session.get('logueado'):
        session.clear()
        return redirect('/')
    return render_template('usuario.html', title='Datos de la cuenta')

# PENDIENTE
@app.route('/principal/usuario/modificar', methods=['GET','POST'])
def modificarUsuario():
    if not session.get('logueado'):
        session.clear()
        return redirect('/')
    else:
        form=ModifyForm()
        try:
            if form.validate_on_submit():
                nombre = form.nombre.data
                password = form.password.data
                edad = form.edad.data
                pais = form.pais.data
                nombreEmpresa = form.nombreEmpresa.data
                with connection.cursor() as cursor:
                    query="""
                        UPDATE usuario
                        SET nombre=%s,
                            contrasena=%s
                        WHERE id_usuario=""" + str(session['id_usuario'])
                    cursor.execute(query,(nombre,password))
                    if session['tipo']=='turista':
                        query="""
                            UPDATE turista
                            SET edad=%s,
                                pais_origen=%s
                            WHERE id=""" + str(session['id_usuario'])
                        cursor.execute(query,(edad,pais))
                    else:
                        query="""
                            UPDATE empresa
                            SET nombre=%s
                            WHERE id=""" + str(session['id_usuario'])
                        cursor.execute(query,(nombreEmpresa))
                connection.commit()
                session['nombre'] = nombre
                return redirect("/principal/usuario")
            with connection.cursor() as cursor:
                query="SELECT nombre, contrasena FROM usuario WHERE id_usuario=" + str(session['id_usuario'])
                cursor.execute(query)
                usuario=cursor.fetchone()
                if session['tipo']=='turista':
                    query="SELECT edad, pais_origen FROM turista WHERE id=" + str(session['id_usuario'])
                    cursor.execute(query)
                    turista=cursor.fetchone()
                    empresa={"nombre":"Ninguno"}
                else:
                    query="SELECT nombre FROM empresa WHERE id=" + str(session['id_usuario'])
                    cursor.execute(query)
                    empresa=cursor.fetchone()
                    turista={"edad":"0", "pais_origen":"Ninguno"}
            connection.commit()
        except:
            return redirect('/')                    
    print(session["tipo"])
    return render_template('modificar_usuario.html', title="Modificar datos de la cuenta", form=form, contrasena=usuario['contrasena'], edad=turista['edad'], pais=turista['pais_origen'], nombreEmpresa=empresa['nombre']) 

@app.route('/principal/agregar_lugar', methods=['GET','POST'])
def agregar_lugar():
    if not session.get('logueado'):
        session.clear()
        return redirect('/')
    else:
        form=AgregarLugar()
        try:
            if form.validate_on_submit():
                nombre = form.nombre.data
                descripcion = form.descripcion.data
                ubicacion = form.ubicacion.data
                categoria = form.categoria.data
                tipo = form.tipo.data
                horario = form.horario.data
                fecha = form.fecha.data

                #INSERTA EN lugar
                SqlInsert = clsSqlInsert.SqlInsert()
                SqlInsert.insertarLugar(nombre, descripcion, ubicacion, tipo, horario, fecha)
                
                #CONSIGUE ide DE lugar
                SqlSelect = clsSqlSelect.SqlSelect()
                ide = SqlSelect.conseguir_ide(nombre)

                #INSERTA EN pertenece_a BASANDOSE EN EL ide
                SqlInsert.insertar_pertenece_a(ide,categoria)

                return redirect("/principal")
        except:
            return redirect('/')      
    return render_template('agregar_lugar.html', title="Registrar un establecimiento o evento", form=form)

@app.route('/logout')
def logout():
    try:
        idu = request.args.to_dict()
        iduINT = int(idu['id_usuario'])
        ses = int(session['id_usuario'])
        if iduINT==ses:
            SqlDelete = clsSqlDelete.SqlDelete()
            SqlDelete.borrarUsuario(ses,session['tipo'])
    except:
        print("Logout")           
    session.clear()        
    return redirect('/')
