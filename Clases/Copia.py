"""
clase para las copias en la base de datos

"""
class Copia:
    """
    constructor de la clase

    :param id: id.
    :type id: int.
    :param nombre: nombre.
    :type nombre: str.
    :param descripcion: descripcion.
    :type descripcion: str.
    :param idproducto: idproducto.
    :type idproducto: int.
    :param idbodega: idbodega.
    :type idbodega: int.


    """

    def __init__(self,id:int,nombre=str,descripcion=str,idproducto=int,idbodega=int) :
        self.__nombre = nombre
        self.__id = id
        self.__descripcion = descripcion
        self.__idproducto = idproducto
        self.__idbodega = idbodega
    def get_id(self):
        return self.__id
    def set_id(self,id):
        self.__id = id

        
    def get_nombre(self):
        return self.__nombre   

    def set_nombre(self,nombre):
        self.__nombre = nombre
    
    def get_descripcion(self):
        return self.__descripcion
    def set_descripcion(self,descripcion):
        self.__descripcion = descripcion

    def get_idproducto(self):
        return self.__idproducto
    def set_idproducto(self,idproducto):
        self.__idproducto = idproducto
    
    def get_idbodega(self):
        return self.__idbodega
    def set_idbodega(self,idbodega):
        self.__idbodega = idbodega