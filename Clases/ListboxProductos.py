import tkinter as tk    
from DAO import DAO

class ListboxProductos:
    def __init__(self):
        self.tipoproducto_seleccionado = tk.StringVar()
    
    def mostrar_ventana(self):
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
            selected_index = productos_listbox.curselection()
            if selected_index:
                selected_producto = productos_listbox.get(selected_index[0])
                productos_listbox.delete(selected_index[0])
                selected_productos_listbox.insert(tk.END, selected_producto)

        def move_back_producto():
            selected_index = selected_productos_listbox.curselection()
            if selected_index:
                selected_productos = selected_productos_listbox.get(selected_index[0])
                selected_productos_listbox.delete(selected_index[0])
                productos_listbox.insert(tk.END, selected_productos)

        def return_values():
            self.tipoproducto_seleccionado.set(selected_productos_listbox.get(0, tk.END))
            root.destroy()

        def filter_productos():
            search_str = filter_entry.get().lower()
            filtered_productos = [producto for producto in productos if search_str in producto.lower()]
            productos_listbox.delete(0, tk.END)
            for producto in filtered_productos:
                productos_listbox.insert(tk.END, producto)

        filter_label = tk.Label(root, text="Buscar un tipo de producto:").pack()
        filter_entry = tk.Entry(root)
        filter_entry.pack()

        filter_button = tk.Button(root, text="Buscar", command=filter_productos)
        filter_button.pack()

        move_button = tk.Button(root, text="Seleccionar", command=move_producto)
        move_button.pack()

        move_back_button = tk.Button(root, text="Retirar", command=move_back_producto)
        move_back_button.pack()

        return_button = tk.Button(root, text="Ingresar", command=return_values)
        return_button.pack()

        root.mainloop()

    def obtener_tipos_seleccionados(self):
        return self.tipoproducto_seleccionado
