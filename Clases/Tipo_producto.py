class Tipo_producto:
    def __init__(self,tipo_producto:str):
        self.__tipo_producto = tipo_producto

    def get_tipo_producto(self):
        return self.__tipo_producto

    def set_tipo_producto(self,tipo_producto):
        self.__tipo_producto = tipo_producto    