"""
clase para las bodegas de la base de datos

"""
class Bodega:
    """
    constructor de la clase

    :param id: id.
    :type id: int
    :param nombre: nombre.
    :type nombre: str.
    :param ubicacion: ubicacion.
    :type ubicacion: str.

    """

    def __init__(self,id:int,nombre=str,ubicacion=str) :
        self.__nombre = nombre
        self.__id = id
        self.__ubicacion = ubicacion


    def get_id(self):
        return self.__id
    def set_id(self,id):
        self.__id = id

        
    def get_nombre(self):
        return self.__nombre   

    def set_nombre(self,nombre):
        self.__nombre = nombre
    
    def get_ubicacion(self):
        return self.__ubicacion
    def set_ubicacion(self,ubicacion):
        self.__ubicacion = ubicacion