class Tipo_producto:
    def __init__(self,idtipo:int,tipo_producto:str):
        self.__tipo_producto = tipo_producto
        self.__idtipo = idtipo

    def get_idtipo(self):
        return self.__idtipo
    def set_idtipo(self,id):
        self.__idtipo = id
        
    def get_tipo_producto(self):
        return self.__tipo_producto

    def set_tipo_producto(self,tipo_producto):
        self.__tipo_producto = tipo_producto    