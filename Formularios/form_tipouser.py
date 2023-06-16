import tkinter as tk
from tkinter.ttk import Combobox
from DAO import *
from Clases.Tipousuario import *

formulario = tk.Tk()
formulario.geometry("300x200") # Tamaño de la ventana
formulario.title("Formulario Tipo de Usuario") # Título de la ventana

# Etiqueta
tipouser_etiqueta = tk.Label(formulario, text="Seleccione el tipo de usuario:") 
tipouser_etiqueta.pack() # La agregamos a la ventana
user = ["Bodeguero","Jefe de Bodega "]

# Selector de categorías
usuario_seleccionado = Combobox(formulario, values=user, state="readonly")
usuario_seleccionado.pack() # Lo agregamos a la ventana




def obtener_tipodeusuario(): #Ingresar tipo de usuario a la base de datos
    dao = DAO() #Inicializacion del DAO
    usuario = usuario_seleccionado.get() #Obtener el tipo de usuario
    tipousuario = Tipousuario(usuario) # Crear el objeto tipo usuario con el dato obtenido antes
    dao.registrarTipousuario(tipousuario) # Ingresar el tipo de usuario a la base de datos

boton_obtener = tk.Button(formulario, text="Registrar tipo de usuario", command=obtener_tipodeusuario)
boton_obtener.pack()

formulario.mainloop()