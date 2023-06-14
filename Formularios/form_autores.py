import tkinter as tk

root = tk.Tk()

data_listbox = tk.Listbox(root)

for item in range(10):
    data_listbox.insert(tk.END, "Item " + str(item+1))
    data_listbox.pack(side=tk.LEFT)

empty_listbox = tk.Listbox(root)
empty_listbox.pack(side=tk.RIGHT)

def move_item():
    # Obtener el índice del elemento seleccionado
    selected_index = data_listbox.curselection()
    if selected_index:
        # Obtener el valor del elemento seleccionado
        selected_item = data_listbox.get(selected_index[0])
        # Eliminar el elemento de la list box con datos
        data_listbox.delete(selected_index[0])
        # Agregar el elemento a la list box vacía
        empty_listbox.insert(tk.END, selected_item)

def move_back_item():
    # Obtener el índice del elemento seleccionado en la lista vacía
    selected_index = empty_listbox.curselection()
    if selected_index:
        # Obtener el valor del elemento seleccionado
        selected_item = empty_listbox.get(selected_index[0])
        # Eliminar el elemento de la lista vacía
        empty_listbox.delete(selected_index[0])
        # Agregar el elemento a la lista con datos
        data_listbox.insert(tk.END, selected_item)

def return_values():
    empty_values = empty_listbox.get(0, tk.END)
    print("Valores ingresados:", empty_values)

move_button = tk.Button(root, text="Ingresar", command=move_item)
move_button.pack()

move_back_button = tk.Button(root, text="Retirar", command=move_back_item)
move_back_button.pack()

return_button = tk.Button(root, text="Retornar valores", command=return_values)
return_button.pack()

root.mainloop()