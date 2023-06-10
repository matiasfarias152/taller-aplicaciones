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
    """
    def __init__(self, username:str, password:str):
        self.__username = username
        self.__password = password

    def get_user(self):
        return self.__username
    
    def set_user(self, username:str):
        self.__username = username

    def get_password(self):
        return self.__password

    def set_password(self, password:str):
        self.__password = password