

"""
clase para la tabla bodega_usuario de la base de datos

"""


class Bodega_usuario:

    """
    constructor de la clase

    :param idbodegausuario: idbodegausuario.
    :type idbodegausuario: int
    :param idusuario: idusuario.
    :type idusuario: int.
    :param idbodega: idbodega.
    :type idbodega: int.

    """


    def __init__(self,idbodegausuario:int,idusuario:int,idbodega:int):
        self.__idbodegausuario = idbodegausuario
        self.__idusuario = idusuario
        self.__idbodega = idbodega

    def get_idbodegausuario(self):
        return self.__idbodegausuario
    def set_idtipo(self,id):
        self.__idbodegausuario = id
        
    def get_idusuario(self):
        return self.__idusuario

    def set_idusuario(self,idusuario):
        self.__idusuario = idusuario

    def get_idbodega(self):
        return self.__idbodega
    def set_idbodega(self,idbodega):
        self.__idbodega = idbodega    