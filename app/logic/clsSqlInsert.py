import pymysql.cursors

class SqlInsert:
    def __init__(self):
        self.conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='uruguia_bd_test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        self.userdata = ""
    
    def insertarLugar(self, nombre, descripcion, ubicacion, tipo, horario, fecha):
        with self.conexion.cursor() as cursor:
            query = """
                    INSERT INTO lugar
                    (nombre, descripcion, ubicacion, tipo, horario, fecha)
                    VALUES
                    (%s,%s,%s,%s,%s, %s)
                    """
            cursor.execute(query,(nombre, descripcion, ubicacion, tipo, horario, fecha))
        self.conexion.commit()
        pass

    def insertar_pertenece_a(self, ide, idc):
        with self.conexion.cursor() as cursor:
            query = """
                    INSERT INTO pertenece_a
                    (ide, idc)
                    VALUES
                    (%s,%s)
                    """    
            cursor.execute(query,(ide, idc))
        self.conexion.commit()
        pass
    
    def insertar_tiene(self, ide, id):
        with self.conexion.cursor() as cursor:
            query = """
                    INSERT INTO tiene
                    (ide, id)
                    VALUES
                    (%s,%s)
                    """    
            cursor.execute(query,(ide, id))
        self.conexion.commit()
        pass

    def crearUsuario(self, email, nombre, password, tipo, id_nuevoUsuario, edad, pais, nombreEmpresa):
        with self.conexion.cursor() as cursor:
            query = """
                    INSERT INTO usuario
                    (id_usuario,email,nombre,contrasena,tipo)
                    VALUES
                    (%s,%s,%s,%s,%s)
                    """
            cursor.execute(query,(id_nuevoUsuario,email,nombre,password,tipo))

            if tipo=='turista':
                query = """
                        INSERT INTO turista
                        (id,edad,pais_origen)
                        VALUES
                        (%s,%s,%s)
                        """
                cursor.execute(query,(id_nuevoUsuario,edad,pais))
            else:                
                query = """
                INSERT INTO empresa
                (id,nombre)
                VALUES
                (%s,%s)
                """
                cursor.execute(query,(id_nuevoUsuario,nombreEmpresa))
        self.conexion.commit()
        pass

