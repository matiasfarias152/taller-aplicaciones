import tkinter as tk
from tkinter.ttk import Combobox
from DAO import *
from Clases.Categoria import *

formulario = tk.Tk()
formulario.geometry("200x150") # Tamaño de la ventana
formulario.title("Formulario Tipo de categoria") # Título de la ventana


tipocateg_etiqueta = tk.Label(formulario, text="Ingrese el tipo de categoria:")
tipocateg_etiqueta.pack() # La agregamos a la ventana


categoria_entry = tk.Entry(formulario)
categoria_entry.pack()

def enviar_categoria():
    dao = DAO()
    categoriainfo = categoria_entry.get()
    categoria = Categoria("",categoriainfo)
    dao.registrarCategoria(categoria)
    
# Código para guardar la categoría en la base de datos

boton_enviar = tk.Button(formulario, text="Enviar categoría", command=enviar_categoria)
boton_enviar.pack()

formulario.mainloop()