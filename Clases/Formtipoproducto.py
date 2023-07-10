import tkinter as tk    
from DAO import DAO
from tkinter import messagebox


'''
clase para crear el formulario de tipo de producto.
'''
class TipoproductoListBox:
    def __init__(self):
        self.tipoproducto_seleccionado = tk.StringVar()
    
    def mostrar_ventana(self):
        '''
        La funcion mostrar_vetana(), genera un listbox, que por el lado izquierdo del listbox se muestran
        los tipo de productos que hay en la base de datos, por el lado derecho estara vacio esperando a que se 
        muevan.
        '''
        dao = DAO()
        root = tk.Tk()

        categories_listbox = tk.Listbox(root)

        categories = dao.obtener_tiposproductos()
        for category in categories:
            categories_listbox.insert(tk.END, category)
            categories_listbox.pack(side=tk.LEFT)
            categories_listbox.configure(width=25, height=15)


        selected_categories_listbox = tk.Listbox(root)
        selected_categories_listbox.pack(side=tk.RIGHT)
        selected_categories_listbox.configure(width=25, height=15)

        def move_producto():
            '''
            Mueve el producto seleccionado de la lista productos a la lista productos seleccionados
            '''  
            if selected_categories_listbox.size() == 1:
                messagebox.showerror("Error", "Ya hay un tipo de producto seleccionado")
            else:
                selected_index = categories_listbox.curselection()
                if selected_index:
                    selected_producto = categories_listbox.get(selected_index[0])
                    categories_listbox.delete(selected_index[0])
                    selected_categories_listbox.insert(tk.END, selected_producto)

        def move_back_producto():
            '''
            Mueve el producto seleccionado a la lista de productos
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
            self.tipoproducto_seleccionado.set(selected_categories_listbox.get(0, tk.END))
            root.destroy()
        
        '''
        Botón para mover el producto al lado derecho
        '''
        move_button = tk.Button(root, text="Seleccionar", command=move_producto)
        move_button.pack()

        '''
        Botón para retirar el producto y devolverlo al lado izquierdo
        '''
        move_back_button = tk.Button(root, text="Retirar", command=move_back_producto)
        move_back_button.pack()

        '''
        Botón para una vez terminado todo recupere los valores ingresados por el usuario
        '''
        return_button = tk.Button(root, text="Ingresar", command=return_values)
        return_button.pack()

        root.mainloop()

    def obtener_tipos_seleccionados(self):
        '''
        Obtiene los productos seleccionados

        retorna:
        el tipo producto seleccionados en forma de cadena.
        '''
        return self.tipoproducto_seleccionado
