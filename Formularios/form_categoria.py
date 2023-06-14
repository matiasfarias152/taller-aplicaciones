import tkinter as tk

root = tk.Tk()

categories_listbox = tk.Listbox(root)

categories = ["Novela", "Ciencia Ficción", "Misterio", "Romance", "Biografía", "Historia", "Educación", "Cocina", "Arte", "Tecnología"]

for category in categories:
    categories_listbox.insert(tk.END, category)
    categories_listbox.pack(side=tk.LEFT)

new_category_entry = tk.Entry(root)
new_category_entry.pack(side=tk.TOP)

def add_category():
    new_category = new_category_entry.get()
    if new_category:
        categories_listbox.insert(tk.END, new_category)
        new_category_entry.delete(0, tk.END)

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

def return_values():
    selected_categories = selected_categories_listbox.get(0, tk.END)
    print("Categorías seleccionadas:", selected_categories)

move_button = tk.Button(root, text="Seleccionar", command=move_category)
move_button.pack()

move_back_button = tk.Button(root, text="Retirar", command=move_back_category)
move_back_button.pack()

add_category_button = tk.Button(root, text="Añadir categoría", command=add_category)
add_category_button.pack()

return_button = tk.Button(root, text="Retornar categorías seleccionadas", command=return_values)
return_button.pack()

root.mainloop()