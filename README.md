# UruGuia
Proyecto del primer año de la carrera Analista TI del proyecto b_IT. Guía turística para Uruguay.

# Cómo trabajar con este repositorio
Este es un pequeño manual para saber como están organizadas las cosas en el proyecto.

## Archivos
- Base de datos: Contiene el diagrama de la base de datos y un archivo SQL para cargar en WAMPServer.
- Prototipo - Interfaz de usuario: Imagenes prototipo para implementar en el programa.
- app: Contiene el programa.
  - static: Contiene archivos estáticos (CSS y Javascript).
  - templates: Contiene las plantillas HTML del programa.
  -__init__.py: Inicia la aplicación en si.
  - routes.py: Contiene las direcciones (routing) del sistema.
- README.md: Esta guía.
- Start-Server-bat: Si lo ejecutas en tu computadora cargará la aplicación en tu navegador.
- uruguia.py: Este archivo carga todo lo de la carpeta "app".

## Setup
Para poder usar el sistema se debe tener instalado:
- Python 3
- pip
  - Flask
  - flask-WTF
  - pymysql
- Y tener abierta la base de datos del proyecto en WAMPServer.

### Base de datos
La base de datos del proyecto está hecha en MySQL. Se debe descargar [WAMPServer](http://www.wampserver.es/#home), entrar en phpMyAdmin, crear una base de datos (por ejemplo, UruGuia_bd_test), entrar a ella y en la pestaña de SQL ingresar el contenido del archivo que se encuentra en la carpeta "Base de Datos".

Ahora, para poder hacer que la aplicación Flask se conecte a WAMPServer, se debe editar el archivo "routes.py". El objeto "connection" llama a una función con una serie de parámetros los cuales se deben modificar para poder conectarse:
```python
connection = pymysql.connect(host='localhost', 
                             user='root', #Nombre del usuario que usamos para conectarnos a WAMPServer, 'root' por defecto.
                             password='', #Si el usuario anterior tiene contraseña debemos escribirla aquí
                             db='uruguia_bd_test', #Nombre de la base de datos dentro de WAMPServer
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
```
Cambiando esos 3 parámetros haremos a Flask compatible con WAMPServer.

## Enlace a la documentación
[Clic aquí](https://docs.google.com/document/d/1TsIIBK_cYJA3LC4x0MBcTItuWLZIk1NgaCrmfUnJ-nE/edit?usp=sharing).
