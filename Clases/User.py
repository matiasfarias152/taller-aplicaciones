"""
clase para validar el usuario y contraseña en la base de datos para verificar si el usuario y la contraseña son correctos en MySQL.
"""




class User:
    """
    constructor de la clase.

    :param username: username.
    :type username: str.
    :param password: password.
    :type password: str.
    :param correo: correo.
    :type correo: str.
    :param rut: rut.
    :type rut: str.
    :param telefono: telefono.
    :type telefono: int.
    """
    def __init__(self, idUser:int ,telefono:str, correo:str,username:str,rut:str,tipousuario:str,password:int):
        self.__username = username
        self.__password = password
        self.__correo = correo
        self.__rut = rut
        self.__telefono = telefono
        self.__idUser = idUser
        self.__tipousuario = tipousuario
    
    def get_tipousuario(self):
        return self.__tipousuario
    def set_tipousuario(self, tipousuario):
        self.__tipousuario = tipousuario

    def get_idUser(self):
        return self.__idUser
    
    def set_idUser(self,id):
        self.__idUser = id

    def get_user(self):
        return self.__username
    
    def set_user(self, username:str):
        self.__username = username

    def get_password(self):
        return self.__password

    def set_password(self, password:str):
        self.__password = password

    def get_correo(self):
        return self.__correo
    
    def set_correo(self,correo:str):
        self.__correo = correo
    
    def get_rut(self):
        return self.__rut
    
    def set_rut(self,rut:str):
        self.__rut = rut
    
    def get_telefono(self):
        return self.__telefono
    
    def set_telefono(self,telefono:int):
        self.__telefono = telefono