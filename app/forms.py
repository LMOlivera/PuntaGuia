from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField
from wtforms.widgets import PasswordInput
# Este archivo contiene todos los formularios del sistema.

class LoginForm(FlaskForm):
    # validators argument es para validaciones.
    # DataRequired chequea que no estén vacíos, aunque existen más validaciones.
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField("Iniciar sesión")

class RegisterForm(FlaskForm):
    email = EmailField('Email')
    nombre = StringField('Nombre y apellido')
    password = PasswordField('Contraseña')
    # foto?
    tipo = StringField('Tipo')
    # TURISTA
    edad = StringField('Edad')
    pais = StringField('País de origen')
    # EMPRESA
    nombreEmpresa = StringField('Nombre de la empresa')
    submit = SubmitField("Crear usuario")

class ModifyForm(FlaskForm):
    nombre = StringField('Nombre y apellido')
    password = PasswordField('Contraseña', widget=PasswordInput(hide_value=False))
    # foto?
    # TURISTA
    edad = StringField('Edad')
    pais = StringField('País de origen')
    # EMPRESA
    nombreEmpresa = StringField('Nombre de la empresa')
    submit = SubmitField("Guardar cambios")

class Lugar(FlaskForm):
    nombre = StringField('Nombre del establecimiento/evento')
    descripcion = TextAreaField('Descripción')
    # imagen?
    ubicacion = StringField('Ubicación')

    categoria = SelectField(u'Categoría', choices=[('1', 'Categoria 1'), ('2', 'Categoria 2'), ('3', 'Categoria 3')])
    tipo = RadioField('Es un', choices=[("Establecimiento","Establecimiento"),("Evento","Evento")], default='Establecimiento')
    horario = StringField('Horario')
    fecha = StringField('Fecha(AAAA/MM/DD)')
    submit = SubmitField("Registrar")