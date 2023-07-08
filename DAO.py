#Aqui se trabajan las funciones que interactuen con el dao 
import mysql.connector
import credencial 
from Clases.User import User
from Clases.Producto import Producto
from Clases.Tipousuario import Tipousuario
from Clases.Categoria import Categoria
from Clases.Tipo_producto import Tipo_producto
from Clases.Autor import Autor
from Clases.Producto_Autor import *
from Clases.Bodega import *
from Clases.Bodega_usuario import *
from Clases.Copia import *
from Clases.Movimiento import *
from Clases.BodegaMov import *
from Clases.CopiaMovimiento import *

class DAO:
    
    def __init__(self):
        self.__conexion = None
        self.__cursor = None
        
    def conectar(self):
        self.__conexion = mysql.connector.connect(**credencial.get_credenciales())
        self.__cursor = self.__conexion.cursor()
        
    def cerrar(self):
        self.__conexion.commit()
        self.__conexion.close()        

    def crear_usuario(self,usuario:User):
        """
        crear un nueva usuario en la base de datos.

        recuperar el nombre de usuario y la contraseña ingresados y los inserta en la base de datos.
        """

        # Conectar en la base de datos.
        self.conectar()
        # crear el nombre de usuario y la contraseña en la base de datos.
        sql = "INSERT INTO usuario (idusuario,telefono,correo,nombre,rut,tipousuario_idtipousuario,contrasena) VALUES (%s, %s,%s,%s,%s,%s,%s)"
        values = (usuario.get_idUser(),usuario.get_telefono(), usuario.get_correo(), usuario.get_user(), usuario.get_rut(), usuario.get_tipousuario(),usuario.get_password())
        self.__cursor.execute(sql, values)  
        self.cerrar()

    def validar_credenciales(self,usuario,contrasena) -> bool:
        """
        Función para validar las credenciales del usuario en la base de datos.

        :return: True si las credenciales son válidas, False en caso contrario.
        :rtype: bool
    """
             
    #conectar a la base de datos.
        self.conectar()
    # Ejecutar la consulta para validar los datos de credenciales del usuario.
        sql = "SELECT nombre,contrasena FROM usuario WHERE nombre = %s AND contrasena = %s"
        values = (usuario, contrasena)
        self.__cursor.execute(sql, values)
        resultado = self.__cursor.fetchone()
        self.cerrar()
        

        if resultado:
        # Si se encuentran los datos en la base de datos, se devuelve True.
            return True
        else:
        # # Si no se encuentran los datos en la base de datos, se devuelve False.
            return False
        
    """
    Funcion para validar permisos

    otorgar permisos de acuerdo con la base de datos

    obtener el nombre y consultar el id en la base de datos
    """

    def validar_permisos(self,nombre):
        self.conectar()
        sql = 'SELECT tipousuario_idtipousuario FROM usuario WHERE nombre = %s'
        values = (nombre,)
        self.__cursor.execute(sql,values)
        id = self.__cursor.fetchone()
        self.cerrar()
        return id[0]


    

    """
    Funcion para registrar productos

    registrar un producto en la base de datos

    obtener el producto con su id,nombre,tipo,categoria y descripcion para luego insertarlo en la base de datos
    """
    def registrarProducto(self,producto:Producto): #Se asignan los 2 parametros self y producto, donde producto es un objeto de tipo Producto
        self.conectar()  #Se conecta a la base de datos
        sql = 'INSERT INTO producto (idproducto, descripcion, categoria_idcategoria, tipoproducto_idtipo) VALUES (%s, %s, %s, %s)' #Sentencia SQL para ingresar items a la base de datos
        values = (producto.get_id(),producto.get_descripcion(),producto.get_categoria(),producto.get_tipoproducto()) #Valores que tendran los items ingresados
        self.__cursor.execute(sql,values) #Ejecución de la sentencia SQL y valores
        self.cerrar() #Se cierra la conexión a la base de datos y guarda

    """
    Funcion para registrar autores

    registrar un autor en la base de datos

    obtener el idautor y nombre para luego insertarlo en la base de datos
    """

    def registrarAutor(self,autor:Autor): #Se asignan los 2 parametros self y autor, donde autor es un objeto de tipo Autor
        self.conectar() #Se conecta a la base de datos
        sql = 'INSERT INTO autor (idautor,nombre) VALUES (%s, %s)'#Sentencia SQL para ingresar items a la base de datos
        values = (autor.get_id(),autor.get_nombre())#Valores que tendran los items ingresados
        self.__cursor.execute(sql,values)#Ejecución de la sentencia SQL y valores
        self.cerrar()#Se cierra la conexión a la base de datos y guarda


    """
    Funcion para registrar bodegas

    registrar una bodega en la base de datos

    obtener el id, nombre y ubicacion para luego insertarlo en la base de datos
    """

    def registrarBodega(self,bodega:Bodega): #Se asignan los 2 parametros self y bodega, donde bodega es un objeto de tipo Bodega
        self.conectar() #Se conecta a la base de datos
        sql = 'INSERT INTO bodega (idbodega,nombre,ubicacion) VALUES (%s, %s,%s)'#Sentencia SQL para ingresar items a la base de datos
        values = (bodega.get_id(),bodega.get_nombre(),bodega.get_ubicacion())#Valores que tendran los items ingresados
        self.__cursor.execute(sql,values)#Ejecución de la sentencia SQL y valores
        self.cerrar()#Se cierra la conexión a la base de datos y guarda




    """
    Funcion para registrar tipos de usuario

    registrar un tipo de usuario en la base de datos

    obtener el tipo de usuario con su id y rol para luego insertarlo en la base de datos
    """
    
    def registrarTipousuario(self,tipousuario:Tipousuario):
        self.conectar()#Se conecta a la base de datos
        sql = 'INSERT INTO tipousuario (idtipousuario, rol) VALUES (%s, %s)'#Sentencia SQL para ingresar tipo de usuarios a la base de datos
        values = (tipousuario.get_idTipo(), tipousuario.get_tipousuario()) # Se recuperan los valores con las 2 funciones get de la clase Tipousuario
        self.__cursor.execute(sql,values)# Se ejecuta la sentencia SQL y sus valores
        self.cerrar()#Se cierra la conexion a la base de datos con un commit
    

    """
    Funcion para registrar categorias

    registrar una categoria en la base de datos

    obtener la categoria con su id y categoria para luego insertarlo en la base de datos
    """

    def registrarCategoria(self,categoria:Categoria):
        self.conectar()#Se conecta a la base de datos
        sql = 'INSERT INTO categoria (idcategoria, categoria) VALUES (%s, %s)'#Sentencia SQL para ingresar una categoria a la base de datos
        values = (categoria.get_idCategoria(), categoria.get_categoria())#Se recuperan los valores con las 2 funciones get de la clase Categoria
        self.__cursor.execute(sql,values)#Se ejecuta la sentencia SQL y sus valores
        self.cerrar()#Se cierra la conexion a la base de datos con un commit

        
    """
    Funcion para registrar tipos de producto

    registrar un tipo de producto en la base de datos

    obtener el tipo de producto con su id y su tipo para luego insertarlo en la base de datos
    """

    def registrarTipoproducto(self,tipoproducto:Tipo_producto):
        self.conectar()#Se conecta a la base de datos
        sql = 'INSERT INTO tipoproducto(idtipo,tipo) VALUES (%s,%s)'#Sentencia SQL para ingresar un tipo de producto a la base de datos
        values = (tipoproducto.get_idtipo(),tipoproducto.get_tipo_producto())#Se recuperan los valores con las 2 funciones get de la clase Tipo_producto
        self.__cursor.execute(sql,values)#Se ejecuta la sentencia SQL y sus valores
        self.cerrar()#Se cierra la coenxion a la base de datos con un commit




    """
    Funcion para registrar movimientos en bodegas

    registrar un movimiento en la base de datos

    registrar un movimiento vinculado a una bodega en la base de datos
    """

    def registrarBodegamov(self,bodegamov:BodegaMov):
        self.conectar()#Se conecta a la base de datos
        sql = 'INSERT INTO bodega_movimiento(idbodegamov,estado,movimiento_idmov,bodega_idbodega) VALUES (%s,%s,%s,%s)'#Sentencia SQL para ingresar un tipo de producto a la base de datos
        values = (bodegamov.get_id(),bodegamov.get_estado(),bodegamov.get_idmov(), bodegamov.get_idbodega())#Se recuperan los valores con las 4 funciones get de la clase BodegaMov
        self.__cursor.execute(sql,values)#Se ejecuta la sentencia SQL y sus valores
        self.cerrar()#Se cierra la conexion a la base de datos con un commit

    """
    Funcion para registrar movimientos de copias

    registrar un movimiento de copias en la base de datos

    ingresar un movimiento de copias en la base de datos
    """

    def registrarCopiamovimiento(self,copiamovimiento:CopiaMovimiento):
        self.conectar()#Se conecta a la base de datos
        sql = 'INSERT INTO copia_movimiento(idcopiamov,copia_idcopia,movimiento_idmov) VALUES (%s,%s,%s)'#Sentencia SQL para ingresar un tipo de producto a la base de datos
        values = (copiamovimiento.get_idcopiamov(),copiamovimiento.get_idcopia(),copiamovimiento.get_idmov())#Se recuperan los valores con las 4 funciones get de la clase BodegaMov
        self.__cursor.execute(sql,values)#Se ejecuta la sentencia SQL y sus valores
        self.cerrar()#Se cierra la conexion a la base de datos con un commit


    """
    Funcion para obtener bodegas

    obtener las bodegas disponibles

    obtener las bodegas ingresados en la base de datos
    """

    def obtener_bodegas(self):
        self.conectar()
        sql = 'SELECT nombre FROM bodega'
        self.__cursor.execute(sql)
        bodegas = self.__cursor.fetchall()
        self.cerrar()
        bodegas = [producto[0].strip('{') for producto in bodegas]
        return bodegas
    



    
    """
    Funcion para obtener copias

    obtener las copias disponibles

    obtener las copias ingresadas en la base de datos
    """

    def obtener_copias(self,idbodega):
        self.conectar()
        sql = 'SELECT CONCAT (idcopia,"-",nombre) FROM copia WHERE bodega_idbodega = %s'
        values = (idbodega,)
        self.__cursor.execute(sql,values)
        copias = self.__cursor.fetchall()
        self.cerrar()
        copias = [copia[0].strip('{') for copia in copias]
        return copias
    


    """
    Funcion para obtener el ultimo id de los movimientos

    obtener el id del ultimo movimiento disponible

    obtener id del ultimo movimiento registrado en la base de datos
    """

    def obtener_ultimomov(self):
        self.conectar()
        sql = 'SELECT MAX(idmov) FROM movimiento'
        self.__cursor.execute(sql)
        idmov = self.__cursor.fetchone()
        self.cerrar()
        return idmov[0]

    """
    Funcion para obtener los ids de las bodegas

    obtener los id's de las bodegas disponibles

    obtener los id's de bodegas ingresadas en la base de datos
    """

    def obtener_idbodega(self,nombre):
        self.conectar()
        sql = 'SELECT idbodega FROM bodega WHERE nombre = %s'
        values = (nombre,)
        self.__cursor.execute(sql,values)
        idbodega = self.__cursor.fetchone()
        self.cerrar()
        
        return idbodega[0]

    """
    Funcion para obtener los ids de las copias

    obtener los id's de las copias disponibles

    obtener los id's de copias ingresadas en la base de datos
    """

    def obtener_idcopia(self,nombre):
        self.conectar()
        sql = 'SELECT idcopia FROM copia WHERE nombre = %s LIMIT 1'
        values = (nombre,)
        self.__cursor.execute(sql,values)
        idcopia = self.__cursor.fetchone()
        self.cerrar()
        
        return idcopia[0]


    
    """
    Funcion para obtener usuarios

    obtener los usuarios disponibles

    obtener los usuarios ingresados en la base de datos
    """

    def obtener_usuarios(self):
        self.conectar()
        sql = 'SELECT nombre FROM usuario'
        self.__cursor.execute(sql)
        usuarios = self.__cursor.fetchall()
        self.cerrar()
        usuarios = [producto[0].strip('{') for producto in usuarios]
        return usuarios
    
    """
    Funcion para obtener los ids de los usuarios

    obtener los id's de los usuarios disponibles

    obtener los id's de usuarios ingresados en la base de datos
    """

    def obtener_idusuario(self,nombre):
        self.conectar()
        sql = 'SELECT idusuario FROM usuario WHERE nombre = %s'
        values = (nombre,)
        self.__cursor.execute(sql,values)
        idusuario = self.__cursor.fetchone()
        self.cerrar()
        return idusuario[0]

    """
    Funcion para obtener productos

    obtener los productos disponibles

    obtener los productos ingresados en la base de datos
    """

    def obtener_productos(self):
        self.conectar()
        sql = 'SELECT descripcion FROM producto'
        self.__cursor.execute(sql)
        productos = self.__cursor.fetchall()
        self.cerrar()
        productos = [producto[0].strip('{') for producto in productos]
        return productos


    def obtener_idproductos(self,producto):
        self.conectar()#Se conecta a la base de datos
        sql = 'SELECT idproducto FROM producto WHERE descripcion = %s'
        values = (producto,)
        self.__cursor.execute(sql,values)
        idproducto = self.__cursor.fetchone()
        self.cerrar()
        return idproducto[0]

    """
    Funcion para obtener autores

    obtener los autores disponibles

    obtener los autores ingresados en la base de datos
    """

    def obtener_autores(self):
        self.conectar()
        sql = 'SELECT nombre FROM autor'
        self.__cursor.execute(sql)
        autores = self.__cursor.fetchall()
        self.cerrar()
        autores = [autor[0].strip('{') for autor in autores]
        return autores
        



    def obtener_idautor(self,autor):
        self.conectar()#Se conecta a la base de datos
        sql = 'SELECT idautor FROM autor WHERE nombre = %s'
        values = (autor,)
        self.__cursor.execute(sql,values)
        idautor = self.__cursor.fetchone()
        self.cerrar()
        return idautor[0]


    """
    Funcion para asignar autores

    asignar un autor a un producto

    asignar un autor a un producto en la base de datos
    """


    def asignarAutor(self,producto_autor:Producto_Autor):
        self.conectar()#Se conecta a la base de datos 
        sql = 'INSERT INTO producto_autor(idproductoautor,producto_idproducto,autor_idautor) VALUES (%s,%s,%s)'#Sentencia SQL para ingresar un tipo de producto a la base de datos
        values = (producto_autor.get_id(),producto_autor.get_idproducto(),producto_autor.get_idautor())#Se recuperan los valores con las 2 funciones get de la clase Tipo_producto
        self.__cursor.execute(sql,values)#Se ejecuta la sentencia SQL y sus valores
        self.cerrar()#Se cierra la coenxion a la base de datos con un commit




    """
    Funcion para asignar usuarios a bodega

    asignar usuarios a una bodega

    asignar varios usuarios a una bodega en la base de datos
    """


    def asignarBodega(self,bodega_usuario:Bodega_usuario):
        self.conectar()#Se conecta a la base de datos 
        sql = 'INSERT INTO bodega_usuario(idbodegausuario,usuario_idusuario,bodega_idbodega) VALUES (%s,%s,%s)'#Sentencia SQL para ingresar un tipo de producto a la base de datos
        values = (bodega_usuario.get_idbodegausuario(),bodega_usuario.get_idusuario(),bodega_usuario.get_idbodega())#Se recuperan los valores con las 3 funciones get de la clase Bodega_usuario
        self.__cursor.execute(sql,values)#Se ejecuta la sentencia SQL y sus valores
        self.cerrar()#Se cierra la coenxion a la base de datos con un commit


    """
    Funcion para asignar copias a productos y bodegas

    asignar copias a una bodega y producto

    asignar varias copias a una bodega en la base de datos
    """


    def asignarCopia(self,copia:Copia):
        self.conectar()#Se conecta a la base de datos 
        sql = 'INSERT INTO copia(idcopia,nombre,descripcion,producto_idproducto,bodega_idbodega) VALUES (%s,%s,%s,%s,%s)'#Sentencia SQL para ingresar una copia a la base de datos
        values = (copia.get_id(),copia.get_nombre(),copia.get_descripcion(),copia.get_idproducto(),copia.get_idbodega())#Se recuperan los valores con las 5 funciones get de la clase Copia
        self.__cursor.execute(sql,values)#Se ejecuta la sentencia SQL y sus valores
        self.cerrar()#Se cierra la coenxion a la base de datos con un commit


    
    """
    Funcion para asignar movimientos a usuarios

    asignar movimientos a un usuario

    asignar movimientos de un usuario a la base de datos
    """


    def asignarMovimiento(self,movimiento:Movimiento):
        self.conectar()#Se conecta a la base de datos 
        sql = 'INSERT INTO movimiento(idmov,fecha,usuario_idusuario) VALUES (%s,%s,%s)'#Sentencia SQL para ingresar un movimiento a la base de datos
        values = (movimiento.get_id(),movimiento.get_fecha(),movimiento.get_idusuario())#Se recuperan los valores con las 3 funciones get de la clase Movimiento
        self.__cursor.execute(sql,values)#Se ejecuta la sentencia SQL y sus valores
        self.cerrar()#Se cierra la coenxion a la base de datos con un commit


    """
    Funcion para obtener tipos de usuario

    obtener los tipos de usuario disponible

    obtener los tipos de usuario ingresados en la base de datos
    """

    def obtener_tiposusuario(self):
        self.conectar()#Se conecta a la base de datos
        sql = 'SELECT rol FROM tipousuario' #Sentencia SQL para consultar los roles existentes
        self.__cursor.execute(sql)
        roles = self.__cursor.fetchall()#Obtener los roles 
        self.cerrar()
        roles = [rol[0].strip('{') for rol in roles]
        return roles# Retornar todos los roles existentes
    
    def obtener_idtipousuario(self,rol):
        self.conectar()#Se conecta a la base de datos
        sql = 'SELECT idtipousuario FROM tipousuario WHERE rol = %s'
        values = (rol,)
        self.__cursor.execute(sql,values)
        idtipo = self.__cursor.fetchone()
        self.cerrar()
        return idtipo[0]

    """
    Funcion para obtener tipos de producto

    obtener los tipos de productos disponible

    obtener los tipos de productos ingresados en la base de datos
    """

    def obtener_tiposproductos(self):
        self.conectar()#Se conecta a la base de datos
        sql = 'SELECT tipo FROM tipoproducto' #Sentencia SQL para consultar los tipos de productos existentes
        self.__cursor.execute(sql)
        tipos = self.__cursor.fetchall()#Obtener tipos de productos
        self.cerrar()
        tipos = [tipo[0].strip('{') for tipo in tipos] #Quitarles el caracter "{" a los datos obtenidos
        return tipos# Retornar todos los tipos existentes
    
    """
    Funcion para obtener los id's de tipos de productos

    obtener los id's de  tipos de productos disponibles

    obtener los id's de tipos de productos ingresados en la base de datos
    """

    def obtener_idtipoproducto(self,tipo):
        self.conectar()#Se conecta a la base de datos
        sql = 'SELECT idtipo FROM tipoproducto WHERE tipo = %s'
        values = (tipo,)
        self.__cursor.execute(sql,values)
        idtipo = self.__cursor.fetchone()
        self.cerrar()
        print(idtipo)
        return idtipo[0]

    """
    Funcion para obtener las categorias

    obtener las categorias disponibles

    obtener las categorias ingresadas en la base de datos
    """

    def obtener_categorias(self):
        self.conectar()#Se conecta a la base de datos
        sql = 'SELECT categoria FROM categoria' #Sentencia SQL para consultar los tipos de productos existentes
        self.__cursor.execute(sql)
        categorias = self.__cursor.fetchall()#Obtener las categorias 
        self.cerrar()
        categorias = [categoria[0].strip('{') for categoria in categorias] #Quitarles el caracter "{" a los datos obtenidos
        return categorias #Retornar las categorias 
    
    """
    Funcion para obtener los id's de las categorias

    obtener los id's de categorias disponibles

    obtener los id's de categorias ingresadas en la base de datos
    """

    def obtener_idcategorias(self,categoria):
        self.conectar()#Se conecta a la base de datos
        sql = 'SELECT idcategoria FROM categoria WHERE categoria = %s'
        values = (categoria,)
        self.__cursor.execute(sql,values)
        idcategoria = self.__cursor.fetchone()
        self.cerrar()
        print(idcategoria)
        return idcategoria[0]


    """
    Funcion para obtener productos filtrandolos por bodega y editorial

    obtener los productos filtrados disponibles

    obtener los productos disponibles en la base de datos
    """

    def obtenerproductosfiltro(self,bodega,editorial):
        self.conectar()#Se conecta a la base de datos
        sql = 'SELECT copia.nombre, COUNT(*)AS cantidad, tipoproducto.tipo AS tipo_producto FROM copia JOIN producto ON copia.producto_idproducto = producto.idproducto JOIN producto_autor ON producto.idproducto = producto_autor.producto_idproducto JOIN autor ON producto_autor.autor_idautor = autor.idautor JOIN bodega ON copia.bodega_idbodega = bodega.idbodega JOIN tipoproducto ON producto.tipoproducto_idtipo = tipoproducto.idtipo WHERE bodega.idbodega = %s AND autor.idautor = %s GROUP BY copia.nombre, tipoproducto.tipo'
        values = (bodega,editorial)
        self.__cursor.execute(sql,values)
        resultados = self.__cursor.fetchall()
        self.cerrar()
        return resultados

    def obtenerstockbodegas(self):
        self.conectar()#Se conecta a la base de datos
        sql = 'SELECT bodega.nombre, bodega.ubicacion, COUNT(*) AS cantidad FROM bodega JOIN copia ON copia.bodega_idbodega = bodega.idbodega GROUP BY bodega.nombre'
        self.__cursor.execute(sql)
        resultados = self.__cursor.fetchall()
        self.cerrar()
        return resultados

    def obtenermovimientosusuario(self):
        self.conectar()#Se conecta a la base de datos
        sql = 'SELECT movimiento.idmov, movimiento.fecha, movimiento.usuario_idusuario, usuario.nombre FROM movimiento JOIN usuario ON movimiento.usuario_idusuario = usuario.idusuario'
        self.__cursor.execute(sql)
        resultados = self.__cursor.fetchall()
        self.cerrar()
        return resultados

    
    def eliminarBodega(self,idbodega):
        self.conectar()
        sql = 'DELETE FROM `bodega` WHERE idbodega = %s'
        values = (idbodega,)
        self.__cursor.execute(sql,values)
        self.cerrar()

    def eliminarAutor(self,idautor):
        self.conectar()
        sql = 'DELETE FROM `autor` WHERE idautor = %s'
        values = (idautor,)
        self.__cursor.execute(sql,values)
        self.cerrar()

    
    def eliminarProducto(self,idproducto):
        self.conectar()
        sql = 'DELETE FROM `producto` WHERE idproducto = %s'
        values = (idproducto,)
        self.__cursor.execute(sql,values)
        self.cerrar()

    # def obtener

    """
    Funcion para actualizar los id's de bodega en las copias

    obtener los id's de bodegas de las copias y actualizarlos

    Actualizar los bodega_idbodega de la tabla copia ingresadas en la base de datos
    """

    def actualizar_idbodegacopias(self,idbodega,idcopia):
        self.conectar()#Se conecta a la base de datos
        sql = 'UPDATE copia SET bodega_idbodega = %s WHERE idcopia = %s'
        values = (idbodega,idcopia)
        self.__cursor.execute(sql,values)
        self.cerrar()
 