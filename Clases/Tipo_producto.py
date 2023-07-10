class Tipo_producto:

    """
    Clase para representar un tipo de producto.
    """
    def __init__(self,idtipo:int,tipo_producto:str):

        """
        Constructor de la clase Tipo_producto.

        :param idtipo: El ID del tipo de producto.
        :param tipo_producto: El nombre del tipo de producto.
        :type idtipo: int.
        :type tipo_producto: str.
        """

        self.__tipo_producto = tipo_producto
        self.__idtipo = idtipo

    def get_idtipo(self):

        """
        Función para obtener el ID del tipo de producto.

        :return: El ID del tipo de producto.
        """
        return self.__idtipo
    
    def set_idtipo(self,id):

        """
        Función para establecer el ID del tipo de producto.

        :param id: El ID del tipo de producto a establecer.
        """
        self.__idtipo = id
        
    def get_tipo_producto(self):

        """
        Función para obtener el nombre del tipo de producto.

        :return: El nombre del tipo de producto.
        """
        return self.__tipo_producto

    def set_tipo_producto(self,tipo_producto):

        """
        Función para establecer el nombre del tipo de producto.

        :param tipo_producto: El nombre del tipo de producto a establecer.
        """
        self.__tipo_producto = tipo_producto    