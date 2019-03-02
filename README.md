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
  - flask-login (TESTEANDO ACTUALMENTE)
- Y tener abierta la base de datos del proyecto en WAMPServer.

### Base de datos
La base de datos del proyecto está hecha en MySQL. Se debe descargar [WAMPServer](http://www.wampserver.es/#home), entrar en phpMyAdmin, crear una base de datos (por ejemplo, UruGuia_bd_test), entrar a ella y en la pestaña de SQL ingresar el contenido del archivo que se encuentra en la carpeta "Base de Datos".


### Enlance a la documentación
[Clic aquí](https://docs.google.com/document/d/1TsIIBK_cYJA3LC4x0MBcTItuWLZIk1NgaCrmfUnJ-nE/edit?usp=sharing).