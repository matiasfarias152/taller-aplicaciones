import tkinter as tk
from tkinter.ttk import Combobox
from DAO import *
from Clases.Tipo_producto import *

formulario = tk.Tk()
formulario.geometry("300x200") # Tamaño de la ventana
formulario.title("Formulario Tipo de Producto") # Título de la ventana

# Etiqueta
tipoprod_etiqueta = tk.Label(formulario, text="Seleccione el tipo de producto:") 
tipoprod_etiqueta.pack() # La agregamos a la ventana
producto = ["Libro","Enciclopedia","Revista"]

# Selector de categorías
productos_seleccionar = Combobox(formulario, values=producto, state="readonly")
productos_seleccionar.pack() # Lo agregamos a la ventana

def registrar_producto():
    dao = DAO()
    tipo = productos_seleccionar.get()
    tipoproducto = Tipo_producto("",tipo)
    dao.registrarTipoproducto(tipoproducto)

boton_obtener = tk.Button(formulario, text="Obtener tipo producto", command=registrar_producto)
boton_obtener.pack()

formulario.mainloop()