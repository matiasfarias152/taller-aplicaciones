from tkinter import *
import os
from DAO import *
from Clases.Producto import *
from tkinter.ttk import Combobox


#Funcion para registrar el producto

def registrar_producto():
    dao = DAO()#Inicializar el DAO
    descripcion_info= descripcion.get() #Obtener la descripcion
    categorias = dao.obtener_categorias() #Obtener las categorias en la base de datos
    tipoproducto = dao.obtener_tiposproductos() #Obtener los tipos de productos en la base de datos
    idcategoria = dao.obtener_idcategorias(categorias,) #Obtener el id de la categoria
    idtipoproducto = dao.obtener_idtipoproducto(tipoproducto,) #Obtener el id del tipo de producto
    
    producto = Producto("",descripcion_info,idcategoria,idtipoproducto)
    dao.registrarProducto(producto)

    Label(ventana, text="Registro completado con éxito", fg="green", font=("calibri", 11)).pack()
    
# Crear la ventana principal
dao = DAO()
ventana = Tk()
ventana.title("Formulario de Productos")
categorias = dao.obtener_categorias()
tipos_producto = dao.obtener_tiposproductos()
global descripcion 
global entrada_descripcion

descripcion = StringVar() #DECLARAMOS "string" COMO TIPO DE DATO PARA "descripcion"


# Etiqueta y campo de texto para la descripción
etiqueta_descripcion = Label(ventana, text="Descripción:")
etiqueta_descripcion.pack()
entrada_descripcion = Entry(ventana, textvariable=descripcion)
entrada_descripcion.pack()

# Etiqueta y combobox para la categoría
etiqueta_categoria = Label(ventana, text="Categoría:")
etiqueta_categoria.pack()
entrada_categoria = Combobox(ventana, values=categorias)
entrada_categoria.pack()

# Etiqueta y combobox para el tipo de producto
etiqueta_producto = Label(ventana, text="Tipo de Producto:")
etiqueta_producto.pack()
entrada_producto = Combobox(ventana, values=tipos_producto)
entrada_producto.pack()

# Botón para registrar el producto
Label(ventana, text="").pack()
Button(ventana, text="Registrar", width=10, height=1, bg="LightGreen", command=registrar_producto).pack()


# Ejecutar la aplicación
ventana.mainloop()




