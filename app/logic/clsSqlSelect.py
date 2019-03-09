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
    
    def listarLugares(self, id):
        with self.conexion.cursor() as cursor:
            query = """
                    SELECT l.nombre,
                            l.descripcion,
                            l.ubicacion,
                            l.tipo,
                            l.horario,
                            l.fecha
                    FROM tiene t
                    INNER JOIN lugar l
                    ON t.ide=l.ide
                    WHERE id=%s
                    """
            cursor.execute(query,(id))
            listaLugares = cursor.fetchall()
            return listaLugares            
        self.conexion.commit()
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
    
    def listarDatosUsuario(self, id, tipo):
        with self.conexion.cursor() as cursor:
            query="SELECT nombre, contrasena FROM usuario WHERE id_usuario=" + str(id)
            cursor.execute(query)
            usuario=cursor.fetchone()
            empresa={}
            turista={}
            if tipo=='turista':
                query="SELECT edad, pais_origen FROM turista WHERE id=" + str(id)
                cursor.execute(query)
                turista=cursor.fetchone()
                empresa={"nombre":"Ninguno"}
            else:
                query="SELECT nombre FROM empresa WHERE id=" + str(id)
                cursor.execute(query)
                empresa=cursor.fetchone()
                turista={"edad":"0", "pais_origen":"Ninguno"}
            userdata={"contrasena": usuario['contrasena'],"edad": turista['edad'],"pais_origen": turista['pais_origen'],"nombre": empresa['nombre']}            
            return userdata
        pass

    def conseguir_id(self, email):
        with self.conexion.cursor() as cursor:
            query = """
            SELECT id_usuario FROM usuario
            WHERE email=%s
            """
            idU = cursor.execute(query,(email))
            return idU
        self.conexion.commit()
        pass
