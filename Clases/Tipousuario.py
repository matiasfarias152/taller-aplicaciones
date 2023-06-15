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
    def __init__(self,idTipo:int,rol:str):
        self.__rol = rol
        self.__idTipo = idTipo

    def get_tipousuario(self):
        return self.__rol
    def set_tipousuario(self,rol):
        self.__rol= rol
    
    def get_idTipo(self):
        return self.__idTipo
    def set_idTipo(self,idTipo):
        self.__idTipo = idTipo