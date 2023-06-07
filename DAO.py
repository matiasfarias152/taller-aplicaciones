#Aqui se trabajan las funciones que interactuen con el dao 
import mysql.connector
import credencial


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