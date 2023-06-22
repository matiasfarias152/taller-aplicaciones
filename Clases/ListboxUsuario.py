import tkinter as tk    
from DAO import DAO

class ListboxUsuario:
    def __init__(self):
        self.usuario_seleccionado = tk.StringVar()
    
    def mostrar_ventana(self,frame):
        dao = DAO()
    

        categories_listbox = tk.Listbox(frame)

        
        usuarios = dao.obtener_usuarios()
        for autor in usuarios:
            categories_listbox.insert(tk.END, autor)
            categories_listbox.pack(side=tk.LEFT)
            categories_listbox.configure(width=25, height=15)


        selected_categories_listbox = tk.Listbox(frame)
        selected_categories_listbox.pack(side=tk.RIGHT)
        selected_categories_listbox.configure(width=25, height=15)

        def move_author():
            selected_index = categories_listbox.curselection()
            if selected_index:
                selected_author = categories_listbox.get(selected_index[0])
                categories_listbox.delete(selected_index[0])
                selected_categories_listbox.insert(tk.END, selected_author)
            autoresget = selected_categories_listbox.get(0, tk.END)
            self.usuario_seleccionado.set(autoresget)

        def move_back_author():
            selected_index = selected_categories_listbox.curselection()
            if selected_index:
                selected_categories = selected_categories_listbox.get(selected_index[0])
                selected_categories_listbox.delete(selected_index[0])
                categories_listbox.insert(tk.END, selected_categories)
                autoresget = selected_categories_listbox.get(0, tk.END)
                self.usuario_seleccionado.set(autoresget)
        # def return_values():
        #     autoresget = selected_categories_listbox.get(0, tk.END)

        #     # autoresget = [autor.strip('{') for autor in autoresget]
        #     self.tipoproducto_seleccionado.set(autoresget)
        #     # root.destroy()

        def filter_categories():
            search_str = filter_entry.get().lower()
            filtered_categories = [author for author in usuarios if search_str in author.lower()]
            categories_listbox.delete(0, tk.END)
            for author in filtered_categories:
                categories_listbox.insert(tk.END, author)

        filter_label = tk.Label(frame, text="Buscar Usuario:").pack()
        filter_entry = tk.Entry(frame)
        filter_entry.pack()

        filter_button = tk.Button(frame, text="Buscar", command=filter_categories)
        filter_button.pack()

        move_button = tk.Button(frame, text="Seleccionar", command=move_author)
        move_button.pack()

        move_back_button = tk.Button(frame, text="Retirar", command=move_back_author)
        move_back_button.pack()

        # return_button = tk.Button(frame, text="Ingresar", command=return_values)
        # return_button.pack()

        # root.mainloop()

    def obtener_usuario_seleccionados(self):
        return self.usuario_seleccionado
