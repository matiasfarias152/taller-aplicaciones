"""
clase para crear una nueva categoria de productos y ingresarla en la base de datos en MySQL.
"""


class Categoria:
    """
    se declara el constructor de la clase

    :param idCategoria: idCategoria.
    :type idCategoria: int.
    :param categoria: categoria.
    :type categoria: str.
    """
    def __init__(self, idCategoria:int, categoria:str):
        self.__idCategoria = idCategoria
        self.__categoria = categoria

    def get_idCategoria(self):
        return self.__idCategoria
    def set_idCategoria(self,idCategoria):
        self.__idCategoria = idCategoria
    
    def get_categoria(self):
        return self.__categoria
    def set_categoria(self,categoria):
        self.__categoria = categoria
        