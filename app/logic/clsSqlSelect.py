import pymysql.cursors

class SqlSelect:
    def __init__(self):
        self.conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='unicorns1998',
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
    
    def listarLugaresDeEmpresa(self, ide):
        with self.conexion.cursor() as cursor:
            query = """
                    SELECT l.ide
                    FROM tiene t
                    INNER JOIN lugar l
                    ON t.ide=l.ide
                    WHERE id=%s
                    """
            cursor.execute(query,(ide))
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
            cursor.execute(query,(email))
            idU = cursor.fetchone()
            return idU
        self.conexion.commit()
        pass

    def conseguir_ultimo_idMasUno(self):
        with self.conexion.cursor() as cursor:
            query = """
                    SELECT id_usuario
                    FROM usuario
                    ORDER BY id_usuario
                    DESC LIMIT 1
                    """
            cursor.execute(query)
            idU = cursor.fetchone()
            if bool(idU):
                return (idU['id_usuario']+1)
            else:
                return 1
        self.conexion.commit()
        pass

    def conseguir_tabla_tiene(self, id_lugar, id_usuario):
        with self.conexion.cursor() as cursor:
            query = """
                    SELECT ide, id
                    FROM tiene
                    WHERE ide=%s AND id=%s
                    """
            cursor.execute(query,(id_lugar, id_usuario))
            tiene = cursor.fetchone()
            return tiene
        self.conexion.commit()
        pass

    def conseguir_datos_lugar(self, nombre):
        with self.conexion.cursor() as cursor:
            query = """
                    SELECT ide,
                           nombre,
                           descripcion,
                           ubicacion,
                           tipo,
                           horario,
                           fecha
                    FROM lugar
                    WHERE nombre=%s
                    """
            cursor.execute(query,(nombre))
            lugar = cursor.fetchone()
            return lugar
        self.conexion.commit()
        pass
    
    def conseguir_datos_pertenece_a(self, ide):
        with self.conexion.cursor() as cursor:
            query = """
                    SELECT ide,
                           idc
                    FROM pertenece_a
                    WHERE ide=%s
                    """
            cursor.execute(query,(ide))
            pertenece_a = cursor.fetchone()
            return pertenece_a
        self.conexion.commit()
        pass
    
    def conseguir_categorias(self):
        with self.conexion.cursor() as cursor:
            query = """
                    SELECT idc,
                           nombre
                    FROM categoria
                    """
            cursor.execute(query)
            categorias = cursor.fetchall()
            return categorias
        self.conexion.commit()
        pass

    def conseguir_lugares(self, categoria):
        with self.conexion.cursor() as cursor:
            query = """
                    SELECT l.ide, l.nombre, l.descripcion, l.ubicacion, l.tipo, l.horario, l.fecha
                    FROM lugar AS l
                    INNER JOIN pertenece_a AS p ON l.ide = p.ide
                    WHERE p.idc=%s
                    ORDER BY l.ide
                    """
            cursor.execute(query,(categoria))
            lugares = cursor.fetchall()
            return lugares
        self.conexion.commit()
        pass

    def conseguir_orden(self, id):
        with self.conexion.cursor() as cursor:
            query = """
                    SELECT orden
                    FROM agrega_a_lista
                    WHERE id=%s
                    ORDER BY orden DESC LIMIT 1
                    """
            cursor.execute(query,(id))
            orden = cursor.fetchone()
            try:
                return orden['orden']
            except:
                return 0
        pass  

    def conseguir_PorVisitar(self, id):
        with self.conexion.cursor() as cursor:
            query = """
                    SELECT ide
                    FROM agrega_a_lista
                    WHERE id=%s
                    """
            cursor.execute(query,(id))
            enLista = cursor.fetchall()
            lista = []
            for row in enLista:
                lista.append(row['ide'])
            return lista
        pass

    def conseguir_listado_PorVisitar(self, id):
        with self.conexion.cursor() as cursor:
            query = """
                    SELECT l.ide, l.nombre, l.descripcion, l.ubicacion, l.tipo, l.horario 
                    FROM lugar l
                    INNER JOIN agrega_a_lista a
                    ON l.ide=a.ide
                    WHERE a.id=%s
                    ORDER BY a.orden
                    """
            cursor.execute(query,(id))
            por_visitar = cursor.fetchall()
            return por_visitar
        pass
