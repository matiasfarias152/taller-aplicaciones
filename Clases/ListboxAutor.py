import tkinter as tk    
from DAO import DAO
from tkinter import messagebox


'''
clase para crear el formulario de autor.
'''
class ListboxAutor:
    def __init__(self):
        self.tipoproducto_seleccionado = tk.StringVar()
    
    def mostrar_ventana(self, frame):
        '''
        La funcion mostrar_vetana(), genera un listbox, que por el lado izquierdo del listbox se muestran
        los autores que hay en la base de datos, por el lado derecho estara vacio esperando a que se 
        muevan.
        '''
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
            '''
            Mueve el autor seleccionado de la lista autores a la lista autores seleccionados
            ''' 
            if selected_autores_listbox.size() == 1:
                messagebox.showerror("Error", "Ya hay un autor seleccionado")
            else:    
                selected_index = autores_listbox.curselection()
                if selected_index:
                    selected_author = autores_listbox.get(selected_index[0])
                    autores_listbox.delete(selected_index[0])
                    selected_autores_listbox.insert(tk.END, selected_author)
                autoresget = selected_autores_listbox.get(0, tk.END)
                self.tipoproducto_seleccionado.set(autoresget)

        def move_back_author():
            '''
            Mueve el autor seleccionado a la lista de autores
            '''
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
        '''
        Obtiene los valores seleccionados

        retorna:
        el autor seleccionados en forma de cadena.
        '''
        return self.tipoproducto_seleccionado
    
    def clear_listbox(listbox):
        '''
        Limpia el contenido de una lista

        parámetros:
        listbox: El cuadro de lista a limpiar.
        '''
        selected_autores_listbox.delete(0, tk.END)
    
    def tamanio_selected(self):
        '''
        Obtiene el tamaño de la lista de autor

        retorna:
        el tamaño de la lista de autor seleccionado.
        '''
        tamanio = selected_autores_listbox.size()
        print(tamanio)
        return tamanio