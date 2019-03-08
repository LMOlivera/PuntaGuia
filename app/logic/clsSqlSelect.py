import pymysql.cursors

class SqlSelect:
    def __init__(self):
        self.conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='uruguia_bd_test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        self.userdata = ""
    
    def login(self, email, password):
        with self.conexion.cursor() as cursor:
            query = "SELECT id_usuario, email, nombre, tipo FROM usuario WHERE email=%s AND contrasena=%s"
            cursor.execute(query,(email,password))
            self.userdata = cursor.fetchone()
            results = cursor.rowcount            
            if results==0:               
                return False
            else:
                return True
        pass
    
    def conseguir_ide(self, nombre):
        with self.conexion.cursor() as cursor:
            query = """
                    SELECT ide FROM lugar
                    WHERE nombre=%s
                    """
            cursor.execute(query,(nombre))
            ide = cursor.fetchone()
            return ide['ide']
        pass