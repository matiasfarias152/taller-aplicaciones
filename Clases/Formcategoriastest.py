import tkinter as tk
from DAO import DAO
from tkinter import messagebox

'''
clase para crear el formulario de categorias.
'''
class CategoriasListBox:
    def __init__(self):
        self.categorias_seleccionadas = tk.StringVar()

    def mostrar_ventana(self):
        '''
        La funcion mostrar_vetana(), genera un listbox, que por el lado izquierdo del listbox se muestran
        todas las categorias que hay en la base de datos, por el lado derecho estara vacio esperando a que se 
        muevan.
        '''
        dao = DAO()
        root = tk.Tk()

        categories_listbox = tk.Listbox(root)

        categories = dao.obtener_categorias()
        for category in categories:
            categories_listbox.insert(tk.END, category)
            categories_listbox.pack(side=tk.LEFT)
            categories_listbox.configure(width=25, height=15)


        selected_categories_listbox = tk.Listbox(root)
        selected_categories_listbox.pack(side=tk.RIGHT)
        selected_categories_listbox.configure(width=25, height=15)

        def move_categoria():
            '''
            Mueve la categoria seleccionada de la lista categories a la lista categoria seleccionada
            '''           
            if selected_categories_listbox.size() == 1:
                
                messagebox.showerror("Error", "Ya hay una categoria seleccionada")
            else:
                selected_index = categories_listbox.curselection()
                if selected_index:
                    selected_categoria = categories_listbox.get(selected_index[0])
                    categories_listbox.delete(selected_index[0])
                    selected_categories_listbox.insert(tk.END, selected_categoria)

        def move_back_categoria():
            '''
            Mueve la categoria seleccionada a la lista de categories
            '''
            selected_index = selected_categories_listbox.curselection()
            if selected_index:
                selected_categories = selected_categories_listbox.get(selected_index[0])
                selected_categories_listbox.delete(selected_index[0])
                categories_listbox.insert(tk.END, selected_categories)

        def return_values():
            '''
            Retorna los valores seleccionados
            '''
            self.categorias_seleccionadas.set(selected_categories_listbox.get(0, tk.END))
            root.destroy()

        '''
        Botón para mover categoria al lado derecho
        '''
        move_button = tk.Button(root, text="Seleccionar", command=move_categoria)
        move_button.pack()

        '''
        Botón para retirar categoria y devolverla al lado izquierdo
        '''
        move_back_button = tk.Button(root, text="Retirar", command=move_back_categoria)
        move_back_button.pack()

        '''
        Botón para una vez terminado todo recupere los valores ingresados por el usuario
        '''
        return_button = tk.Button(root, text="Ingresar", command=return_values)
        return_button.pack()

        root.mainloop()

    def obtener_categorias_seleccionadas(self):
        '''
        Obtiene las categorias seleccionadas

        retorna:
        la categoria seleccionados en forma de cadena.
        '''
        return self.categorias_seleccionadas
        


    