"""
clase para los autores de la base de datos

"""
class Autor:
    """
    constructor de la clase

    :param nombre: nombre.
    :type nombre: str.
    """

    def __init__(self,nombre=str) :
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre   

    def set_nombre(self,nombre):
        self.__nombre = nombre