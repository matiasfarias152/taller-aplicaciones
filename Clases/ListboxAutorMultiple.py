import tkinter as tk    
from DAO import DAO
from tkinter import messagebox

class ListboxAutorMultiple:
    def __init__(self):
        self.tipoproducto_seleccionado = tk.StringVar()
    
    def mostrar_ventana(self, frame):
        dao = DAO()
        global selected_autores_listbox

        etiqueta_autores = tk.Label(frame, text="Autores")
        etiqueta_autores.grid(row=1, column=0, padx=10, pady=10)

        autores_listbox = tk.Listbox(frame)
        autores_listbox.grid(row=2, column=0, padx=10)

        autores = dao.obtener_autores()
        for autor in autores:
            autores_listbox.insert(tk.END, autor)

        etiqueta_autores_seleccionados = tk.Label(frame, text="Autores seleccionados")
        etiqueta_autores_seleccionados.grid(row=1, column=1, padx=10, pady=10)

        selected_autores_listbox = tk.Listbox(frame)
        selected_autores_listbox.grid(row=2, column=1, padx=10)

        def move_author():
            
                selected_index = autores_listbox.curselection()
                if selected_index:
                    selected_author = autores_listbox.get(selected_index[0])
                    autores_listbox.delete(selected_index[0])
                    selected_autores_listbox.insert(tk.END, selected_author)
                autoresget = selected_autores_listbox.get(0, tk.END)
                self.tipoproducto_seleccionado.set(autoresget)

        def move_back_author():
            selected_index = selected_autores_listbox.curselection()
            if selected_index:
                selected_autores = selected_autores_listbox.get(selected_index[0])
                selected_autores_listbox.delete(selected_index[0])
                autores_listbox.insert(tk.END, selected_autores)
                autoresget = selected_autores_listbox.get(0, tk.END)
                self.tipoproducto_seleccionado.set(autoresget)

        move_button = tk.Button(frame, text="Seleccionar", command=move_author)
        move_button.grid(row=3, column=0, pady=10)

        move_back_button = tk.Button(frame, text="Retirar", command=move_back_author)
        move_back_button.grid(row=3, column=1, pady=10)

    def obtener_tipos_seleccionados(self):
        return self.tipoproducto_seleccionado
    
    def clear_listbox(listbox):
        selected_autores_listbox.delete(0, tk.END)
    
    def tamanio_selected(self):
        tamanio = selected_autores_listbox.size()
        print(tamanio)
        return tamanio