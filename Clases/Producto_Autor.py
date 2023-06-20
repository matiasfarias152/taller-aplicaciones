"""
clase para la tabla producto_autor  de la base de datos

"""
class Producto_Autor:
    """
    constructor de la clase

    :param id: id.
    :type id: int.
    :param idproducto: idproducto.
    :type idproducto: int.
    :param idautor: idautor.
    :type idautor: int.
    """

    def __init__(self,id:int,idproducto=int,idautor=int) :
        self.__idproducto = idproducto
        self.__id = id
        self.__idautor = idautor

    def get_id(self):
        return self.__id
    def set_id(self,id):
        self.__id = id

        
    def get_idproducto(self):
        return self.__idproducto

    def set_idproducto(self,idproducto):
        self.__idproducto = idproducto
    
    def get_idautor(self):
        return self.__idautor
    def set_idautor(self,idautor):
        self.__idautor = idautor