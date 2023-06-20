import tkinter as tk    
from DAO import DAO

class TipoproductoListBox:
    def __init__(self):
        self.tipoproducto_seleccionado = tk.StringVar()
    
    def mostrar_ventana(self):
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

        def move_author():
            selected_index = categories_listbox.curselection()
            if selected_index:
                selected_author = categories_listbox.get(selected_index[0])
                categories_listbox.delete(selected_index[0])
                selected_categories_listbox.insert(tk.END, selected_author)

        def move_back_author():
            selected_index = selected_categories_listbox.curselection()
            if selected_index:
                selected_categories = selected_categories_listbox.get(selected_index[0])
                selected_categories_listbox.delete(selected_index[0])
                categories_listbox.insert(tk.END, selected_categories)

        def return_values():
            self.tipoproducto_seleccionado.set(selected_categories_listbox.get(0, tk.END))
            root.destroy()

        def filter_categories():
            search_str = filter_entry.get().lower()
            filtered_categories = [author for author in categories if search_str in author.lower()]
            categories_listbox.delete(0, tk.END)
            for author in filtered_categories:
                categories_listbox.insert(tk.END, author)

        filter_label = tk.Label(root, text="Buscar un tipo de producto:").pack()
        filter_entry = tk.Entry(root)
        filter_entry.pack()

        filter_button = tk.Button(root, text="Buscar", command=filter_categories)
        filter_button.pack()

        move_button = tk.Button(root, text="Seleccionar", command=move_author)
        move_button.pack()

        move_back_button = tk.Button(root, text="Retirar", command=move_back_author)
        move_back_button.pack()

        return_button = tk.Button(root, text="Ingresar", command=return_values)
        return_button.pack()

        root.mainloop()

    def obtener_tipos_seleccionados(self):
        return self.tipoproducto_seleccionado
