import pymysql.cursors

class SqlDelete:
    def __init__(self):
        self.conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='uruguia_bd_test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    
    def borrarUsuario(self, id_usuario, tipo):
        with self.conexion.cursor() as cursor:
            query = """
                    DELETE FROM usuario WHERE id_usuario=%s
                    """ 
            cursor.execute(query,(id_usuario))
            if tipo=='turista':
                query = """
                        DELETE FROM turista WHERE id=%s
                        """ 
                cursor.execute(query,(id_usuario))
            else:
                query = """
                        DELETE FROM empresa WHERE id=%s
                        """ 
                cursor.execute(query,(id_usuario))
        self.conexion.commit()
        pass

    def borrarLugar(self, ide):
        with self.conexion.cursor() as cursor:
            query = """
                    DELETE FROM tiene WHERE ide=%s
                    """ 
            cursor.execute(query,(ide))
            query = """
                    DELETE FROM lugar WHERE ide=%s
                    """ 
            cursor.execute(query,(ide))
        self.conexion.commit()
        pass