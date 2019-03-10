import pymysql.cursors

class SqlUpdate:
    def __init__(self):
        self.conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='uruguia_bd_test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        
    
    def actualizarUsuario(self, nombre, password, id, tipo, edad, pais, nombreEmpresa):
        with self.conexion.cursor() as cursor:
            query="""
                UPDATE usuario
                SET nombre=%s,
                    contrasena=%s
                WHERE id_usuario=""" + str(id)
            cursor.execute(query,(nombre,password))
            if tipo=='turista':
                query="""
                    UPDATE turista
                    SET edad=%s,
                        pais_origen=%s
                    WHERE id=""" + str(id)
                cursor.execute(query,(edad,pais))   
                pass
            else:
                query="""
                    UPDATE empresa
                    SET nombre=%s
                    WHERE id=""" + str(id)
                cursor.execute(query,(nombreEmpresa))
                pass
        self.conexion.commit()
        pass
        
    def actualizarLugarYpertenece_a(self, nombre, descripcion, ubicacion, tipo, horario, fecha, idc, ide):
        with self.conexion.cursor() as cursor:
            query="""
                UPDATE lugar
                SET nombre=%s,
                    descripcion=%s,
                    ubicacion=%s,
                    tipo=%s,
                    horario=%s,
                    fecha=%s
                WHERE ide=""" + str(ide)
            cursor.execute(query,(nombre, descripcion, ubicacion, tipo, horario, fecha))
            query="""
                UPDATE pertenece_a
                SET idc=%s
                WHERE ide=""" + str(ide)
            cursor.execute(query,(idc))
        self.conexion.commit()
        pass