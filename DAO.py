#Aqui se trabajan las funciones que interactuen con el dao 
import mysql.connector
import credencial
from User import User
from Producto import Producto
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
        sql = "INSERT INTO usuario (nombre, contrasena) VALUES (%s, %s)"
        values = (self.get_user(), self.get_password())
        self.cursor.execute(sql, values)  
        self.cerrar()

    def validar_credenciales(self) -> bool:
        """
        Función para validar las credenciales del usuario en la base de datos.

        :return: True si las credenciales son válidas, False en caso contrario.
        :rtype: bool
    """
             
    #conectar a la base de datos.
        self.conectar()
    # Ejecutar la consulta para validar los datos de credenciales del usuario.
        sql = "SELECT * FROM credenciales WHERE usuario = %s AND contrasena = %s"
        values = (self.usuario, self.contrasena)
        self.__cursor.execute(sql, values)
        resultado = self.__cursor.fetchone()
        self.cerrar()

        if resultado:
        # Si se encuentran los datos en la base de datos, se devuelve True.
            return True
        else:
        # Si no se encuentran los datos en la base de datos, se devuelve False.
            return False
        

    
    

    """
    Funcion para registrar productos

    registrar un producto en la base de datos

    obtener el producto con su id,nombre,tipo,categoria y descripcion para luego insertarlo en la base de datos
    """
    def registrarProducto(self,producto:Producto): #Se asignan los 2 parametros self y producto, donde producto es un objeto de tipo Producto
        self.conectar()  #Se conecta a la base de datos
        sql = 'INSERT INTO productos (idProducto, nombre, tipo, categoria, descripcion) VALUES (%s, %s, %s, %s, %s)' #Sentencia SQL para ingresar items a la base de datos
        values = (producto.get_id(), producto.get_nombre(), producto.get_tipo(), producto.get_categoria(), producto.get_descripcion()) #Valores que tendran los items ingresados
        self.__cursor.execute(sql,values) #Ejecución de la sentencia SQL y valores
        self.cerrar() #Se cierra la conexión a la base de datos