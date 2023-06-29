"""
clase para ingresar un movimiento de una copia en la base de datos en MySQL.
"""


class CopiaMovimiento:
    """
    se declara el constructor de la clase

    :param idcopiamov: idcopiamov.
    :type idcopiamov: int.
    :param idcopia: idcopia.
    :type idcopia: int.
    :param idmov: idmov.
    :type idmov: int.
    """
    def __init__(self, idcopiamov:int, idcopia:int, idmov:int):
        self.__idcopiamov = idcopiamov
        self.__idcopia = idcopia
        self.__idmov = idmov

    def get_idmov(self):
        return self.__idmov
    def set_idmov(self,idmov):
        self.__idmov = idmov

    def get_idcopiamov(self):
        return self.__idcopiamov
    def set_idcopiamov(self,idcopiamov):
        self.__idcopiamov = idcopiamov
    
    def get_idcopia(self):
        return self.__idcopia
    def set_idcopia(self,idcopia):
        self.__idcopia = idcopia
        