import tkinter as tk
from tkinter.ttk import Combobox


formulario = tk.Tk()
formulario.geometry("300x200") # Tamaño de la ventana
formulario.title("Formulario de categorías") # Título de la ventana

# Etiqueta
categoria_etiqueta = tk.Label(formulario, text="Seleccione su categoría:") 
categoria_etiqueta.pack() # La agregamos a la ventana
categorias = ["Ficción", "No ficción", "Fantasía", "Terror", "Biografía"]

# Selector de categorías
categoria_seleccionar = Combobox(formulario, values=categorias, state="readonly")
categoria_seleccionar.pack() # Lo agregamos a la ventana

def obtener_categoria():
    categoria = categoria_seleccionar.get()
    print("La categoría seleccionada es:", categoria)

boton_obtener = tk.Button(formulario, text="Obtener categoría", command=obtener_categoria)
boton_obtener.pack()

formulario.mainloop()