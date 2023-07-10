import tkinter as tk    
from DAO import DAO
from tkinter import messagebox 

class ListboxUsuarioMultiple:
    def __init__(self):
        self.usuario_seleccionado = tk.StringVar()

    def mostrar_ventana(self, frame):
        dao = DAO()

        global selected_usuarios_listbox
        
        etiqueta_usuarios = tk.Label(frame, text="Usuarios")
        etiqueta_usuarios.grid(row=4, column=0, padx=10, pady=10)

        usuarios_listbox = tk.Listbox(frame)
        usuarios_listbox.grid(row=5, column=0, padx=10)

        usuarios = dao.obtener_usuarios()
        for usuario in usuarios:
            usuarios_listbox.insert(tk.END, usuario)

        etiqueta_usuarios_seleccionados = tk.Label(frame, text="Usuarios seleccionados")
        etiqueta_usuarios_seleccionados.grid(row=4, column=1, padx=10, pady=10)

        selected_usuarios_listbox = tk.Listbox(frame)
        selected_usuarios_listbox.grid(row=5, column=1, padx=10)

        def move_usuario():
                selected_index = usuarios_listbox.curselection()
                if selected_index:
                    selected_usuario = usuarios_listbox.get(selected_index[0])
                    usuarios_listbox.delete(selected_index[0])
                    selected_usuarios_listbox.insert(tk.END, selected_usuario)
                usuarioesget = selected_usuarios_listbox.get(0, tk.END)
                self.usuario_seleccionado.set(usuarioesget)

        def move_back_usuario():
            selected_index = selected_usuarios_listbox.curselection()
            if selected_index:
                selected_categories = selected_usuarios_listbox.get(selected_index[0])
                selected_usuarios_listbox.delete(selected_index[0])
                usuarios_listbox.insert(tk.END, selected_categories)
                usuarioesget = selected_usuarios_listbox.get(0, tk.END)
                self.usuario_seleccionado.set(usuarioesget)

        move_button = tk.Button(frame, text="Seleccionar", command=move_usuario)
        move_button.grid(row=7, column=0, pady=10)

        move_back_button = tk.Button(frame, text="Retirar", command=move_back_usuario)
        move_back_button.grid(row=7, column=1, pady=10)

    def obtener_usuario_seleccionados(self):
        return self.usuario_seleccionado
    
    def tamanio_selected(self):
        tamanio = selected_usuarios_listbox.size()
        print(tamanio)
        return tamanio