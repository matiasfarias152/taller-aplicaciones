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
    def __init__(self,id:int,nombre:str,tipo:str,categoria:str,descripcion:str):
        self.__id = id
        self.__nombre = nombre
        self.__tipo = tipo
        self.__categoria = categoria
        self.__descripcion = descripcion    

    def get_id(self):
        return self.__id
    def set_id(self,id:int):
        self.__id = id
        
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre:str):
        self.__nombre = nombre
        
    def get_tipo(self):
        return self.__tipo
    def set_tipo(self,tipo:str):
        self.__tipo = tipo
        
    def get_categoria(self):
        return self.__categoria
    def set_categoria(self,categoria:str):
        self.__categoria = categoria
        
    def get_descripcion(self):
        return self.__descripcion
    def set_descripcion(self,descripcion:str):
        self.__descripcion = descripcion
        
    def __str__(self):
        cadena = f'ID: {self.__id} \n Nombre: {self.__nombre} \n Tipo: {self.__tipo} \n Categoria: {self.__categoria} \n Descripcion: {self.__descripcion} '
        return cadena
