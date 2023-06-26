"""
clase para los movimientos de la base de datos

"""
class Movimiento:
    """
    constructor de la clase

    :param id: id.
    :type id: int.
    :param fecha: fecha.
    :type fecha: date.
    :param idusuario: idusuario.
    :type idusuario: int.
    """

    def __init__(self,id:int,fecha,idusuario=int) :
        self.__id = id
        self.__fecha = fecha
        self.__idusuario = idusuario

    def get_id(self):
        return self.__id
    def set_id(self,id):
        self.__id = id

        
    def get_fecha(self):
        return self.__fecha   

    def set_fecha(self,fecha):
        self.__fecha = fecha
    
    def get_idusuario(self):
        return self.__idusuario
    def set_idusuario(self,idusuario):
        self.__idusuario = idusuario