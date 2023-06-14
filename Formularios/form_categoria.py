import tkinter as tk

root = tk.Tk()

categories_listbox = tk.Listbox(root)

categories = ["Novela", "Ciencia Ficción", "Misterio", "Romance", "Biografía", "Historia", "Educación", "Cocina", "Arte", "Tecnología"]

for category in categories:
    categories_listbox.insert(tk.END, category)
    categories_listbox.pack(side=tk.LEFT)

selected_categories_listbox = tk.Listbox(root)
selected_categories_listbox.pack(side=tk.RIGHT)

def move_category():
# Obtener el índice de la categoría seleccionada
    selected_index = categories_listbox.curselection()
    if selected_index:
# Obtener el valor de la categoría seleccionada
        selected_category = categories_listbox.get(selected_index[0])
# Eliminar la categoría de la list box de categorías
        categories_listbox.delete(selected_index[0])
# Agregar la categoría a la list box de categorías seleccionadas
        selected_categories_listbox.insert(tk.END, selected_category)

def move_back_category():
# Obtener el índice de la categoría seleccionada en la lista de categorías seleccionadas
    selected_index = selected_categories_listbox.curselection()
    if selected_index:
# Obtener el valor de la categoría seleccionada
        selected_category = selected_categories_listbox.get(selected_index[0])
# Eliminar la categoría de la lista de categorías seleccionadas
        selected_categories_listbox.delete(selected_index[0])
# Agregar la categoría a la lista de categorías
        categories_listbox.insert(tk.END, selected_category)

def return_values():
    selected_categories = selected_categories_listbox.get(0, tk.END)
    print("Categorías seleccionadas:", selected_categories)

move_button = tk.Button(root, text="Seleccionar", command=move_category)
move_button.pack()

move_back_button = tk.Button(root, text="Retirar", command=move_back_category)
move_back_button.pack()

return_button = tk.Button(root, text="Retornar categorías seleccionadas", command=return_values)
return_button.pack()

root.mainloop()