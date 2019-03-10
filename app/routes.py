from flask import render_template, flash, redirect, session, request
from app import app, logic
from app.logic import clsSqlInsert, clsSqlDelete, clsSqlUpdate, clsSqlSelect
from app.forms import LoginForm, RegisterForm, ModifyForm, AgregarLugar

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

@app.route('/index/registro', methods=['GET', 'POST'])
def registro():
    if session.get('logueado'):
        return redirect('/principal')   
    else:
        nuevo = request.args.to_dict()
        form = RegisterForm()
        if form.validate_on_submit():
            try:
                SqlSelect = clsSqlSelect.SqlSelect()                
                SqlInsert = clsSqlInsert.SqlInsert()
                print(SqlSelect.conseguir_ultimo_idMasUno())
                SqlInsert.crearUsuario(form.email.data,
                                        form.nombre.data,
                                        form.password.data,
                                        nuevo['tipo'],
                                        SqlSelect.conseguir_ultimo_idMasUno(),
                                        form.edad.data,
                                        form.pais.data,
                                        form.nombreEmpresa.data
                                        )
                session.clear()
                return redirect('/index') 
            except:    
                print('Algo malo pasó')
                return redirect('/index')
    return render_template('registro.html', title="Registrar un nuevo usuario", form=form, tipo=nuevo['tipo'])

@app.route('/principal')
def index():
    if session.get('logueado'):
        if session['tipo']=='turista':
            listalugares={}
            pass
        else:
            try:
                SqlSelect = clsSqlSelect.SqlSelect()
                listalugares = SqlSelect.listarLugares(session['id_usuario'])
            except:
                listalugares={}      
    else:
        session.clear()
        return redirect('/')
    return render_template('principal.html', title="Página principal", lugares=listalugares)

@app.route('/principal/usuario')
def usuario():
    if not session.get('logueado'):
        session.clear()
        return redirect('/')
    return render_template('usuario.html', title='Datos de la cuenta')

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
                SqlUpdate = clsSqlUpdate.SqlUpdate()
                SqlUpdate.actualizarUsuario(nombre, password, session['id_usuario'], session['tipo'], edad, pais, nombreEmpresa)
                session['nombre'] = nombre
                return redirect("/principal/usuario")
            SqlSelect = clsSqlSelect.SqlSelect()
            userdata = SqlSelect.listarDatosUsuario(session['id_usuario'], session['tipo'])
        except:
            return redirect('/')
    return render_template('modificar_usuario.html', title="Modificar datos de la cuenta", form=form, contrasena=userdata['contrasena'], edad=userdata['edad'], pais=userdata['pais_origen'], nombreEmpresa=userdata['nombre']) 

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

                #INSERTA EN tiene
                SqlInsert.insertar_tiene(ide,session['id_usuario'])

                return redirect("/principal")
        except:
            return redirect('/')      
    return render_template('agregar_lugar.html', title="Registrar un establecimiento o evento", form=form)

@app.route('/principal/eliminar_lugar', methods=['GET','POST'])
def eliminar_lugar():
    if not session.get('logueado'):
        session.clear()
        return redirect('/')
    else:
        try:
            lugar = request.args.to_dict()
            nombreLugar=lugar['nombre']
            SqlSelect = clsSqlSelect.SqlSelect()
            ide = SqlSelect.conseguir_ide(nombreLugar)
            tiene = SqlSelect.conseguir_tabla_tiene(ide, session['id_usuario'])
            if request.method=='POST':
                SqlDelete = clsSqlDelete.SqlDelete()
                SqlDelete.borrarLugar(ide)
                return redirect('/principal')
            if not bool(tiene):
                return redirect('/principal')
        except:
            print('Algo malo ocurrió')
            return redirect('/principal')
    return render_template('eliminar_lugar.html', title="Eliminar establecimiento/evento", ide=ide) 

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
