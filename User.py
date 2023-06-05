"""
clase para validar el usuario y contraseña en la base de datos para verificar si el usuario y la contraseña son correctos en MySQL.
"""
from DAO import DAO
import credencial 
from funciones import *
from form_ingreso import *

class User():
    """
    constructor de la clase.

    :param username: username.
    :type username: str.
    :param password: password.
    :type password: str.
    """
    def __init__(self, username:str, password:str):
        self.username = username
        self.password = password

    def get_user(self):
        return self.username
    
    def set_user(self, username:str):
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, password:str):
        self.password = password