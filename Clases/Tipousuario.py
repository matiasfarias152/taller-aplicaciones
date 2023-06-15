"""
clase para crear un nuevo tipo de usuario y ingresarlo en la base de datos en MySQL.
"""



class Tipousuario:

    
    """
    se declara el constructor de la clase

    :param tipousuario: tipousuario.
    :type tipousuario: str.
    :param idTipo: idTipo.
    :type idTipo: int.
    """
    def __init__(self,idTipo:int,tipousuario:str):
        self.__tipousuario = tipousuario
        self.__idTipo = idTipo

    def get_tipousuario(self):
        return self.__tipousuario
    def set_tipousuario(self,tipousuario):
        self.__tipousuario = tipousuario
    
    def get_idTipo(self):
        return self.__idTipo
    def set_idTipo(self,idTipo):
        self.__idTipo = idTipo