"""
clase para los autores de la base de datos

"""
class Autor:
    """
    constructor de la clase

    :param nombre: nombre.
    :type nombre: str.
    """

    def __init__(self,id:int,nombre=str) :
        self.__nombre = nombre
        self.__id = id

    def get_id(self):
        return self.__id
    def set_id(self,id):
        self.__id = id

        
    def get_nombre(self):
        return self.__nombre   

    def set_nombre(self,nombre):
        self.__nombre = nombre