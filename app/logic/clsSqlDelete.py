import pymysql.cursors

class SqlDelete:
    def __init__(self):
        self.conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='puntaguia_bd_test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    
    #SI ES UNA EMPRESA DEBE BORRARSE TAMBIEN LOS LUGARES ASOCIADOS Y TAMBIEN DE LA LISTA DEL TIPO TURISTA
    def borrarUsuario(self, id_usuario, tipo, lugares={}):
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
                query = """
                        DELETE FROM tiene WHERE id=%s
                        """ 
                cursor.execute(query,(id_usuario))
                #AHORA DEBE BORRAR DE LUGAR, PERTENECE_A, VISITO y AGREGA_A_LISTA
                if bool(lugares):
                        for lugar in lugares:
                                query = """
                                        DELETE FROM lugar WHERE ide=%s
                                        """ 
                                cursor.execute(query,(lugar['ide']))
                                query = """
                                        DELETE FROM pertenece_a WHERE ide=%s
                                        """ 
                                cursor.execute(query,(lugar['ide']))
                                query = """
                                        DELETE FROM visito WHERE ide=%s
                                        """ 
                                cursor.execute(query,(lugar['ide']))
                                query = """
                                        DELETE FROM lugar agrega_a_lista ide=%s
                                        """ 
                                cursor.execute(query,(lugar['ide']))
        self.conexion.commit()
        pass

    def borrarLugar(self, ide):
        with self.conexion.cursor() as cursor:
                valor = ide
                query = """
                        DELETE FROM tiene WHERE ide=%s
                        """ 
                cursor.execute(query,(valor))
                query2 = """
                        DELETE FROM pertenece_a WHERE ide=%s
                        """ 
                cursor.execute(query2,(valor))
                query3 = """
                        DELETE FROM visito WHERE ide=%s
                        """ 
                cursor.execute(query3,(valor))
                query4 = """
                        DELETE FROM agrega_a_lista WHERE ide=%s
                        """ 
                cursor.execute(query4,(valor))
                query5 = """
                        DELETE FROM lugar WHERE ide=%s
                        """ 
                cursor.execute(query5,(valor))
        self.conexion.commit()
        pass

    def borrarDePorVisitar(self, id, ide):
        with self.conexion.cursor() as cursor:
                query = """
                        DELETE FROM agrega_a_lista
                        WHERE id=%s AND ide=%s
                        """ 
                cursor.execute(query,(id,ide))
        self.conexion.commit()
        pass

