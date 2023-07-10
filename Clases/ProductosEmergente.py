import tkinter as tk
from DAO import DAO
from tkinter import messagebox

class ListboxProductoEmergente:

    """
    Clase para crear una interfaz gráfica de usuario con una ventana emergente, con una lista de productos seleccionables.
    """

    def __init__(self):

        """
        Constructor de la clase ListboxProductoEmergente.

        Inicializa la variable de instancia 'productos_seleccionados' como un objeto StringVar de tkinter.
        """
        self.productos_seleccionados = tk.StringVar()
       

    def mostrar_ventana(self):

        """
        Función para mostrar la ventana emergente de la interfaz gráfica.
        """
        dao = DAO()
        root = tk.Tk()

        productos_listbox = tk.Listbox(root)

        productos = dao.obtener_productos()
        for producto in productos:
            productos_listbox.insert(tk.END, producto)
            productos_listbox.pack(side=tk.LEFT)
            productos_listbox.configure(width=25, height=15)


        selected_productos_listbox = tk.Listbox(root)
        selected_productos_listbox.pack(side=tk.RIGHT)
        selected_productos_listbox.configure(width=25, height=15)

        def move_producto():
            """
            Función para mover un producto de la lista de productos a la lista de productos seleccionados.
            """
            
            if selected_productos_listbox.size() == 1:
                messagebox.showerror("Error", "Ya hay un producto seleccionado")
            else:
                selected_index = productos_listbox.curselection()
                if selected_index:
                    selected_producto = productos_listbox.get(selected_index[0])
                    productos_listbox.delete(selected_index[0])
                    selected_productos_listbox.insert(tk.END, selected_producto)

        def move_back_producto():

            """
            Función para mover un producto de la lista de productos seleccionados a la lista de productos.
            """
            selected_index = selected_productos_listbox.curselection()
            if selected_index:
                selected_productos = selected_productos_listbox.get(selected_index[0])
                selected_productos_listbox.delete(selected_index[0])
                productos_listbox.insert(tk.END, selected_productos)

        def return_values():

            """
            Función para obtener los productos seleccionados y cerrar la ventana emergente.
            """
            self.productos_seleccionados.set(selected_productos_listbox.get(0, tk.END))
            root.destroy()


        move_button = tk.Button(root, text="Seleccionar", command=move_producto)
        move_button.pack()

        move_back_button = tk.Button(root, text="Retirar", command=move_back_producto)
        move_back_button.pack()

        return_button = tk.Button(root, text="Ingresar", command=return_values)
        return_button.pack()

        root.mainloop()

    def obtener_tipos_seleccionados(self):


        """
        Método para obtener los productos seleccionados.

        :return: Los productos seleccionados como un objeto StringVar de tkinter.
        """
        
        return self.productos_seleccionados