from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField
# Este archivo contiene todos los formularios del sistema.

class LoginForm(FlaskForm):
    # validators argument es para validaciones.
    # DataRequired chequea que no estén vacíos, aunque existen más validaciones.
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField("Iniciar sesión")