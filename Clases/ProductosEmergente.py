import tkinter as tk
from DAO import DAO
from tkinter import messagebox

class ListboxProductoEmergente:
    def __init__(self):
        self.categorias_seleccionadas = tk.StringVar()
       

    def mostrar_ventana(self):
        dao = DAO()
        root = tk.Tk()

        categories_listbox = tk.Listbox(root)

        categories = dao.obtener_productos()
        for category in categories:
            categories_listbox.insert(tk.END, category)
            categories_listbox.pack(side=tk.LEFT)
            categories_listbox.configure(width=25, height=15)


        selected_categories_listbox = tk.Listbox(root)
        selected_categories_listbox.pack(side=tk.RIGHT)
        selected_categories_listbox.configure(width=25, height=15)

        def move_categoria():
            
            if selected_categories_listbox.size() == 1:
                messagebox.showerror("Error", "Ya hay un producto seleccionado")
            else:
                selected_index = categories_listbox.curselection()
                if selected_index:
                    selected_categoria = categories_listbox.get(selected_index[0])
                    categories_listbox.delete(selected_index[0])
                    selected_categories_listbox.insert(tk.END, selected_categoria)

        def move_back_categoria():
            selected_index = selected_categories_listbox.curselection()
            if selected_index:
                selected_categories = selected_categories_listbox.get(selected_index[0])
                selected_categories_listbox.delete(selected_index[0])
                categories_listbox.insert(tk.END, selected_categories)

        def return_values():
            self.categorias_seleccionadas.set(selected_categories_listbox.get(0, tk.END))
            root.destroy()


        move_button = tk.Button(root, text="Seleccionar", command=move_categoria)
        move_button.pack()

        move_back_button = tk.Button(root, text="Retirar", command=move_back_categoria)
        move_back_button.pack()

        return_button = tk.Button(root, text="Ingresar", command=return_values)
        return_button.pack()

        root.mainloop()

    def obtener_tipos_seleccionados(self):
        return self.categorias_seleccionadas