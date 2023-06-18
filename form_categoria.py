import tkinter as tk
from DAO import *
from Clases.Categoria import *

def categoriaslistbox():

    root = tk.Tk()
    dao = DAO()
    categories_listbox = tk.Listbox(root)

    categories = dao.obtener_categorias()

    for category in categories:
        categories_listbox.insert(tk.END, category)
        categories_listbox.pack(side=tk.LEFT)


    def filter_categories():
        search_str = filter_entry.get().lower()
        filtered_categories = [category for category in categories if search_str in category.lower()]
        categories_listbox.delete(0, tk.END)
        for category in filtered_categories:
            categories_listbox.insert(tk.END, category)

    filter_label = tk.Label(root, text="Filtrar por categoria:")
    filter_label.place(relx = 0.5, rely = 0.5, anchor = 'sw')
    filter_label.pack()

    filter_entry = tk.Entry(root)
    filter_entry.pack()

    filter_button = tk.Button(root, text="Buscar", command=filter_categories)
    filter_button.pack()


    selected_categories_listbox = tk.Listbox(root)
    selected_categories_listbox.pack(side=tk.RIGHT)
    
    def move_category():
        selected_index = categories_listbox.curselection()
        if selected_index:
            selected_category = categories_listbox.get(selected_index[0])
            categories_listbox.delete(selected_index[0])
            selected_categories_listbox.insert(tk.END, selected_category)

    def move_back_category():
        selected_index = selected_categories_listbox.curselection()
        if selected_index:
            selected_category = selected_categories_listbox.get(selected_index[0])
            selected_categories_listbox.delete(selected_index[0])
            categories_listbox.insert(tk.END, selected_category)


    def registrar_categoria():
        dao = DAO()
        categorias = selected_categories_listbox.get(0, tk.END)
        categoria = Categoria("",categorias)
        dao.registrarCategoria(categoria)




    def return_values():
        selected_categories = selected_categories_listbox.get(0, tk.END)
        return selected_categories
        

    move_button = tk.Button(root, text="Seleccionar", command=move_category)
    move_button.pack()

    move_back_button = tk.Button(root, text="Retirar", command=move_back_category)
    move_back_button.pack()



    return_button = tk.Button(root, text="Ingresar categoria", command=return_values)
    return_button.pack()

    boton_registrar = tk.Button(root, text="Registrar categorias", command=registrar_categoria)

    root.mainloop()

