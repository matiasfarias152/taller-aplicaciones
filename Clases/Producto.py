"""
clase que se utiliza para registrar productos en la base de datos
"""


class Producto:

    """
    se declara el constructor de la clase

    :param id: id.
    :type id: int.
    :param nombre: nombre.
    :type nombre: str.
    :param tipo: tipo
    :type tipo: str
    :param categoria : categoria
    :type categoria: str
    :param descripcion: descripcion
    :type descripcion: str
    """
    def __init__(self,id:int,descripcion:str,categoria:str,tipoproducto:str):
        self.__id = id
        self.__tipoproducto = tipoproducto
        self.__categoria = categoria
        self.__descripcion = descripcion    

    def get_id(self):
        return self.__id
    def set_id(self,id:int):
        self.__id = id
        

    def get_tipoproducto(self):
        return self.__tipoproducto
    def set_tipoproducto(self,tipo:str):
        self.__tipoproducto = tipo
        
    def get_categoria(self):
        return self.__categoria
    def set_categoria(self,categoria:str):
        self.__categoria = categoria
        
    def get_descripcion(self):
        return self.__descripcion
    def set_descripcion(self,descripcion:str):
        self.__descripcion = descripcion
        
    def __str__(self):
        cadena = f'ID: {self.__id} \n \n Tipo: {self.__tipoproducto} \n Categoria: {self.__categoria} \n Descripcion: {self.__descripcion} '
        return cadena
