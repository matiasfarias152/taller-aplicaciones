"""
clase para los movimientos de bodega en la base de datos

"""
class BodegaMov:
    """
    constructor de la clase

    :param id: id.
    :type id: int.
    :param estado: estado.
    :type estado: tinyint.
    :param idmov: idmov.
    :type idmov: int.
    :param idbodega: idbodega.
    :type idbodega: int.



    """

    def __init__(self,id:int,estado,idmov=int,idbodega=int):
        self.__estado = estado
        self.__idmov = idmov
        self.__id = id
        self.__idbodega = idbodega

    def get_id(self):
        return self.__id
    def set_id(self,id):
        self.__id = id

        
    def get_estado(self):
        return self.__estado   
    def set_estado(self,estado):
        self.__estado = estado
    
    def get_idmov(self):
        return self.__idmov
    def set_idmov(self,idmov):
        self.__idmov = idmov

    def get_idbodega(self):
        return self.__idbodega
    def set_idbodega(self,idbodega):
        self.__idbodega = idbodega
