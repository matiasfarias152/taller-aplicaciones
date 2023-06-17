import tkinter as tk

root = tk.Tk()

authors_listbox = tk.Listbox(root)

authors = ["Stephen King", "J.K. Rowling", "Dan Brown", "Agatha Christie", "Nicholas Sparks", "Malcolm X", "Michelle Obama", "Jamie Oliver", "Leonardo da Vinci", "Steve Jobs"]

for author in authors:
    authors_listbox.insert(tk.END, author)
    authors_listbox.pack(side=tk.LEFT)

new_author_entry = tk.Entry(root)
new_author_entry.pack(side=tk.TOP)

def add_author():
    new_author = new_author_entry.get()
    if new_author:
        authors.append(new_author)
        authors_listbox.insert(tk.END, new_author)
        new_author_entry.delete(0, tk.END)

selected_authors_listbox = tk.Listbox(root)
selected_authors_listbox.pack(side=tk.RIGHT)

def move_author():
    selected_index = authors_listbox.curselection()
    if selected_index:
        selected_author = authors_listbox.get(selected_index[0])
        authors_listbox.delete(selected_index[0])
        selected_authors_listbox.insert(tk.END, selected_author)

def move_back_author():
    selected_index = selected_authors_listbox.curselection()
    if selected_index:
        selected_author = selected_authors_listbox.get(selected_index[0])
        selected_authors_listbox.delete(selected_index[0])
        authors_listbox.insert(tk.END, selected_author)

def return_values():
    selected_authors = selected_authors_listbox.get(0, tk.END)
    print("Autores seleccionados:", selected_authors)

def filter_authors():
    search_str = filter_entry.get().lower()
    filtered_authors = [author for author in authors if search_str in author.lower()]
    authors_listbox.delete(0, tk.END)
    for author in filtered_authors:
        authors_listbox.insert(tk.END, author)

filter_label = tk.Label(root, text="Filtrar por autor:")
filter_label.pack()

filter_entry = tk.Entry(root)
filter_entry.pack()

filter_button = tk.Button(root, text="Buscar", command=filter_authors)
filter_button.pack()

move_button = tk.Button(root, text="Seleccionar", command=move_author)
move_button.pack()

move_back_button = tk.Button(root, text="Retirar", command=move_back_author)
move_back_button.pack()

add_author_button = tk.Button(root, text="Añadir autor", command=add_author)
add_author_button.pack()

return_button = tk.Button(root, text="Retornar autores seleccionados", command=return_values)
return_button.pack()

root.mainloop()