import os
# Necesario para hacer andar el login, la verdad no entiendo porqué ni como funciona
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'