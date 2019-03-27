import os

class Config(object):
    # La variable de configuración SECRET_KEY es muy importante,
    # ya que muchas extensiones de Flask la utilizan como valor
    # criptográfico. Flask-WTF la usa para evitar ataques Cross
    # Site Request Forgery. Sería buena idea investigarla un poco.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # Una vez creada hay que decirle a Flask que la use.
    # routes.py usa app.config.from_object para usarla.
    # puntaguia.py también.