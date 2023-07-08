import tkinter as tk    
from DAO import DAO

class ListboxProductos:
    def __init__(self):
        self.tipoproducto_seleccionado = tk.StringVar()
    
    def mostrar_ventana(self, frame):
            dao = DAO()

            etiqueta_productos = tk.Label(frame, text="Productos")
            etiqueta_productos.grid(row=1, column=0, padx=10, pady=10)

            productos_listbox = tk.Listbox(frame)
            productos_listbox.grid(row=2, column=0, padx=10)

            productos = dao.obtener_productos()
            for producto in productos:
                productos_listbox.insert(tk.END, producto)

            etiqueta_productos_seleccionados = tk.Label(frame, text="Productos seleccionados")
            etiqueta_productos_seleccionados.grid(row=1, column=1, padx=10, pady=10)

            selected_productos_listbox = tk.Listbox(frame)
            selected_productos_listbox.grid(row=2, column=1, padx=10)

            def move_producto():
                selected_index = productos_listbox.curselection()
                if selected_index:
                    selected_producto = productos_listbox.get(selected_index[0])
                    productos_listbox.delete(selected_index[0])
                    selected_productos_listbox.insert(tk.END, selected_producto)
                productosget = selected_productos_listbox.get(0, tk.END)
                self.tipoproducto_seleccionado.set(productosget)
            def move_back_producto():
                selected_index = selected_productos_listbox.curselection()
                if selected_index:
                    selected_productos = selected_productos_listbox.get(selected_index[0])
                    selected_productos_listbox.delete(selected_index[0])
                    productos_listbox.insert(tk.END, selected_productos)
                productosget = selected_productos_listbox.get(0, tk.END)
                self.tipoproducto_seleccionado.set(productosget)

            move_button = tk.Button(frame, text="Seleccionar", command=move_producto)
            move_button.grid(row=5, column=0, pady=10)

            move_back_button = tk.Button(frame, text="Retirar", command=move_back_producto)
            move_back_button.grid(row=5, column=1, pady=10)

     

    def obtener_tipos_seleccionados(self):
        return self.tipoproducto_seleccionado