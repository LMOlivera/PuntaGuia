# UruGuia

Guía turística para Uruguay. Proyecto del primer año de la carrera Analista TI del proyecto b_IT.

### Enlace a la documentación del proyecto

[Clic aquí](https://docs.google.com/document/d/1TsIIBK_cYJA3LC4x0MBcTItuWLZIk1NgaCrmfUnJ-nE/edit?usp=sharing).

# Cómo trabajar con este repositorio

Este es un pequeño manual para saber como están organizadas las cosas en el proyecto.

### Prerequisitos

Para poder trabajar con este repositorio necesitas tener en tu máquina local lo siguiente (en orden):

- [Python 3](https://www.python.org/downloads/)
- pip (Escribir en la consola CMD de Windows: ```python get-pip.py```)
- Flask (Escribir en la consola CMD de Windows: ```pip install Flask```
- flask-WTF (Escribir en la consola CMD de Windows: ```pip install Flask-WTF```)
- pymysql (Escribir en la consola CMD de Windows: ```python -m pip install PyMySQL```)
- [WAMPServer](http://www.wampserver.es/)

### Instalación

Descargar el repositorio. Abrir WAMPServer e importar la base de datos que se encuentra en la carpeta "Base de datos" del repositorio (uruguia_bd_test.sql).

##### Base de datos

La base de datos del proyecto está hecha en MySQL. Se debe descargar [WAMPServer](http://www.wampserver.es/#home), entrar en phpMyAdmin, crear una base de datos (por ejemplo, uruguia_bd_test), entrar a ella y en la pestaña de SQL ingresar el contenido del archivo que se encuentra en la carpeta "Base de Datos".

Ahora, para poder hacer que la aplicación Flask se conecte a WAMPServer, **se deben editar las 4 clases Sql (Insert, Update, Delete y Select) dentro de la carpeta /app/logic**. El objeto "conexion" llama a una función con una serie de parámetros los cuales se deben modificar para poder conectarse:
```python
self.conexion = pymysql.connect(host='localhost',
                                user='root', #Nombre del usuario que usamos para conectarnos a WAMPServer, 'root' por defecto.
                                password='', #Si el usuario anterior tiene contraseña debemos escribirla aquí
                                db='uruguia_bd_test', #Nombre de la base de datos dentro de WAMPServer
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
```
Cambiando los 3 parámetros comentados haremos a Flask compatible con WAMPServer.

##### Ejecutar el sistema

Si se han instalado todos los programas de prerequisito, se cargó la base de datos en WAMPServer y se modificaron los archivos necesarios para conectarse a la base de datos, lo único que resta hacer es ejecutar el archivo "Start-Server.bat", el cual abrirá una consola CMD y abrirá la aplicación web. Tener en cuenta que es probable que tu navegador se abra antes de que se levante la aplicación, por lo que deberás recargar la página manualmente (F5 en tu navegador).

### Estructura del proyecto
- Base de datos: Contiene el diagrama actual de la base de datos y un archivo SQL para cargar en WAMPServer.
- Prototipo - Interfaz de usuario: Imagenes de prototipo de la interfaz de usuario para implementar en el programa.
- app: Contiene el programa.
  - logic: Contiene clases de Python que se encargan de la lógica de negocio de la aplicación web.
  - static: Contiene archivos estáticos (imagenes, CSS, Javascript).
  - templates: Contiene las plantillas HTML del programa.
  -__init__.py: Inicia la aplicación en si.
  - routes.py: Contiene las URL (routing) del sistema.
- README.md: Esta guía.
- Start-Server.bat: Si lo ejecutas en tu computadora cargará la aplicación en tu navegador.
- uruguia.py: Este archivo carga todo lo de la carpeta "app".

## Construido con

* [Python 3](https://www.python.org/downloads/): El lenguaje de programación elegido.
* [Flask](http://flask.pocoo.org/): Microframework web de fácil uso.
* [WAMPServer](http://www.wampserver.es/): Servidor Apache, MySQL y php para Windows.
* [Visual Studio Code](https://code.visualstudio.com/): Potente IDE de alta personalización.
* [Github](https://github.com/): Source Control y Kanban Board.
* [Discord](https://discordapp.com/): Software de mensajería dividida en canales y videollamadas.
* [Microsoft Project](https://products.office.com/es/project/project-and-portfolio-management-software): Para el diseño del diagrama de Gantt.
* [Google Drive](https://www.google.com/intl/es_ALL/drive/): Para alojar la documentación y los diagramas.
* [draw.io](https://www.draw.io/): Para diagramar la base de datos.

## Autores

* **Lucas Olivera** - *Project Leader, Backend Developer* - [Perfil](https://github.com/LMOlivera)
* **Ángeles Nieves** - *Front-End Developer* - [Perfil](https://github.com/AngelesNieves)
* **Noelia Nieves** - *Front-End Developer* - [Perfil](https://github.com/Noeliang)
* **Juan Rolando** - *Database Developer* - [Perfil](https://github.com/jprolando)

* **Email del grupo** - *softwaredeleste@gmail.com*
