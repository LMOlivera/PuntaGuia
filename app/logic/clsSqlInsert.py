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