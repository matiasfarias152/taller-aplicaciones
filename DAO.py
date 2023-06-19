#Aqui se trabajan las funciones que interactuen con el dao 
import mysql.connector
import credencial 
from Clases.User import User
from Clases.Producto import Producto
from Clases.Tipousuario import Tipousuario
from Clases.Categoria import Categoria
from Clases.Tipo_producto import Tipo_producto
from Clases.Autor import Autor
class DAO:
    def __init__(self):
        self.__conexion = None
        self.__cursor = None
        
    def conectar(self):
        self.__conexion = mysql.connector.connect(**credencial.get_credenciales())
        self.__cursor = self.__conexion.cursor()
        
    def cerrar(self):
        self.__conexion.commit()
        self.__conexion.close()        

    def crear_usuario(self,usuario:User):
        """
        crear un nueva usuario en la base de datos.

        recuperar el nombre de usuario y la contraseña ingresados y los inserta en la base de datos.
        """

        # Conectar en la base de datos.
        self.conectar()
        # crear el nombre de usuario y la contraseña en la base de datos.
        sql = "INSERT INTO usuario (idusuario,telefono,correo,nombre,rut,tipousuario_idtipousuario,contrasena) VALUES (%s, %s,%s,%s,%s,%s,%s)"
        values = (usuario.get_idUser(),usuario.get_telefono(), usuario.get_correo(), usuario.get_user(), usuario.get_rut(), usuario.get_tipousuario(),usuario.get_password())
        self.__cursor.execute(sql, values)  
        self.cerrar()

    def validar_credenciales(self,usuario,contrasena) -> bool:
        """
        Función para validar las credenciales del usuario en la base de datos.

        :return: True si las credenciales son válidas, False en caso contrario.
        :rtype: bool
    """
             
    #conectar a la base de datos.
        self.conectar()
    # Ejecutar la consulta para validar los datos de credenciales del usuario.
        sql = "SELECT nombre,contrasena FROM usuario WHERE nombre = %s AND contrasena = %s"
        values = (usuario, contrasena)
        self.__cursor.execute(sql, values)
        resultado = self.__cursor.fetchone()
        self.cerrar()
        

        if resultado:
        # Si se encuentran los datos en la base de datos, se devuelve True.
            return True
        else:
        # # Si no se encuentran los datos en la base de datos, se devuelve False.
            return False
        
    """
    Funcion para validar permisos

    otorgar permisos de acuerdo con la base de datos

    obtener el nombre y consultar el id en la base de datos
    """

    def validar_permisos(self,nombre):
        self.conectar()
        sql = 'SELECT tipousuario_idtipousuario FROM usuario WHERE nombre = %s'
        values = (nombre,)
        self.__cursor.execute(sql,values)
        id = self.__cursor.fetchone()
        self.cerrar()
        return id[0]


    

    """
    Funcion para registrar productos

    registrar un producto en la base de datos

    obtener el producto con su id,nombre,tipo,categoria y descripcion para luego insertarlo en la base de datos
    """
    def registrarProducto(self,producto:Producto): #Se asignan los 2 parametros self y producto, donde producto es un objeto de tipo Producto
        self.conectar()  #Se conecta a la base de datos
        sql = 'INSERT INTO producto (idproducto, descripcion, categoria_idcategoria, tipoproducto_idtipo) VALUES (%s, %s, %s, %s)' #Sentencia SQL para ingresar items a la base de datos
        values = (producto.get_id(),producto.get_descripcion(),producto.get_categoria(),producto.get_tipoproducto()) #Valores que tendran los items ingresados
        self.__cursor.execute(sql,values) #Ejecución de la sentencia SQL y valores
        self.cerrar() #Se cierra la conexión a la base de datos y guarda

    """
    Funcion para registrar autores

    registrar un autor en la base de datos

    obtener el idautor y nombre para luego insertarlo en la base de datos
    """

    def registrarAutor(self,autor:Autor): #Se asignan los 2 parametros self y autor, donde autor es un objeto de tipo Autor
        self.conectar() #Se conecta a la base de datos
        sql = 'INSERT INTO autor (idautor,nombre) VALUES (%s, %s)'#Sentencia SQL para ingresar items a la base de datos
        values = (autor.get_id(),autor.get_nombre())#Valores que tendran los items ingresados
        self.__cursor.execute(sql,values)#Ejecución de la sentencia SQL y valores
        self.cerrar()#Se cierra la conexión a la base de datos y guarda




    """
    Funcion para registrar tipos de usuario

    registrar un tipo de usuario en la base de datos

    obtener el tipo de usuario con su id y rol para luego insertarlo en la base de datos
    """
    
    def registrarTipousuario(self,tipousuario:Tipousuario):
        self.conectar()#Se conecta a la base de datos
        sql = 'INSERT INTO tipousuario (idtipousuario, rol) VALUES (%s, %s)'#Sentencia SQL para ingresar tipo de usuarios a la base de datos
        values = (tipousuario.get_idTipo(), tipousuario.get_tipousuario()) # Se recuperan los valores con las 2 funciones get de la clase Tipousuario
        self.__cursor.execute(sql,values)# Se ejecuta la sentencia SQL y sus valores
        self.cerrar()#Se cierra la conexion a la base de datos con un commit
    

    """
    Funcion para registrar categorias

    registrar una categoria en la base de datos

    obtener la categoria con su id y categoria para luego insertarlo en la base de datos
    """

    def registrarCategoria(self,categoria:Categoria):
        self.conectar()#Se conecta a la base de datos
        sql = 'INSERT INTO categoria (idcategoria, categoria) VALUES (%s, %s)'#Sentencia SQL para ingresar una categoria a la base de datos
        values = (categoria.get_idCategoria(), categoria.get_categoria())#Se recuperan los valores con las 2 funciones get de la clase Categoria
        self.__cursor.execute(sql,values)#Se ejecuta la sentencia SQL y sus valores
        self.cerrar()#Se cierra la conexion a la base de datos con un commit

        
    """
    Funcion para registrar tipos de producto

    registrar un tipo de producto en la base de datos

    obtener el tipo de producto con su id y su tipo para luego insertarlo en la base de datos
    """

    def registrarTipoproducto(self,tipoproducto:Tipo_producto):
        self.conectar()#Se conecta a la base de datos
        sql = 'INSERT INTO tipoproducto(idtipo,tipo) VALUES (%s,%s)'#Sentencia SQL para ingresar un tipo de producto a la base de datos
        values = (tipoproducto.get_idtipo(),tipoproducto.get_tipo_producto())#Se recuperan los valores con las 2 funciones get de la clase Tipo_producto
        self.__cursor.execute(sql,values)#Se ejecuta la sentencia SQL y sus valores
        self.cerrar()#Se cierra la coenxion a la base de datos con un commit


    """
    Funcion para obtener tipos de usuario

    obtener los tipos de usuario disponible

    obtener los tipos de usuario ingresados en la base de datos
    """

    def obtener_tiposusuario(self):
        self.conectar()#Se conecta a la base de datos
        sql = 'SELECT rol FROM tipousuario' #Sentencia SQL para consultar los roles existentes
        self.__cursor.execute(sql)
        roles = self.__cursor.fetchall()#Obtener los roles 
        self.cerrar()
        roles = [rol[0].strip('{') for rol in roles]
        return roles# Retornar todos los roles existentes
    
    def obtener_idtipousuario(self,rol):
        self.conectar()#Se conecta a la base de datos
        sql = 'SELECT idtipousuario FROM tipousuario WHERE rol = %s'
        values = (rol,)
        self.__cursor.execute(sql,values)
        idtipo = self.__cursor.fetchone()
        self.cerrar()
        return idtipo[0]

    """
    Funcion para obtener tipos de producto

    obtener los tipos de productos disponible

    obtener los tipos de productos ingresados en la base de datos
    """

    def obtener_tiposproductos(self):
        self.conectar()#Se conecta a la base de datos
        sql = 'SELECT tipo FROM tipoproducto' #Sentencia SQL para consultar los tipos de productos existentes
        self.__cursor.execute(sql)
        tipos = self.__cursor.fetchall()#Obtener tipos de productos
        self.cerrar()
        tipos = [tipo[0].strip('{') for tipo in tipos] #Quitarles el caracter "{" a los datos obtenidos
        return tipos# Retornar todos los tipos existentes
    
    """
    Funcion para obtener los id's de tipos de productos

    obtener los id's de  tipos de productos disponibles

    obtener los id's de tipos de productos ingresados en la base de datos
    """

    def obtener_idtipoproducto(self,tipo):
        self.conectar()#Se conecta a la base de datos
        sql = 'SELECT idtipo FROM tipoproducto WHERE tipo = %s'
        values = (tipo,)
        self.__cursor.execute(sql,values)
        idtipo = self.__cursor.fetchone()
        self.cerrar()
        print(idtipo)
        return idtipo[0]

    """
    Funcion para obtener las categorias

    obtener las categorias disponibles

    obtener las categorias ingresadas en la base de datos
    """

    def obtener_categorias(self):
        self.conectar()#Se conecta a la base de datos
        sql = 'SELECT categoria FROM categoria' #Sentencia SQL para consultar los tipos de productos existentes
        self.__cursor.execute(sql)
        categorias = self.__cursor.fetchall()#Obtener las categorias 
        self.cerrar()
        categorias = [categoria[0].strip('{') for categoria in categorias] #Quitarles el caracter "{" a los datos obtenidos
        return categorias #Retornar las categorias 
    
    """
    Funcion para obtener los id's de las categorias

    obtener los id's de categorias disponibles

    obtener los id's de categorias ingresadas en la base de datos
    """

    def obtener_idcategorias(self,categoria):
        self.conectar()#Se conecta a la base de datos
        sql = 'SELECT idcategoria FROM categoria WHERE categoria = %s'
        values = (categoria,)
        self.__cursor.execute(sql,values)
        idcategoria = self.__cursor.fetchone()
        self.cerrar()
        print(idcategoria)
        return idcategoria[0]

    