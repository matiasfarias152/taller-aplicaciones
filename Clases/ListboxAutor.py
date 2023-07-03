import tkinter as tk    
from DAO import DAO

class ListboxAutor:
    def __init__(self):
        self.tipoproducto_seleccionado = tk.StringVar()
    
    def mostrar_ventana(self,frame):
        dao = DAO()
    

        autores_listbox = tk.Listbox(frame)

        autores = dao.obtener_autores()
        for autor in autores:
            autores_listbox.insert(tk.END, autor)
            autores_listbox.pack(side=tk.LEFT)
            autores_listbox.configure(width=25, height=15)


        selected_autores_listbox = tk.Listbox(frame)
        selected_autores_listbox.pack(side=tk.RIGHT)
        selected_autores_listbox.configure(width=25, height=15)

        def move_author():
            selected_index = autores_listbox.curselection()
            if selected_index:
                selected_author = autores_listbox.get(selected_index[0])
                autores_listbox.delete(selected_index[0])
                selected_autores_listbox.insert(tk.END, selected_author)
            autoresget = selected_autores_listbox.get(0, tk.END)
            self.tipoproducto_seleccionado.set(autoresget)

        def move_back_author():
            selected_index = selected_autores_listbox.curselection()
            if selected_index:
                selected_autores = selected_autores_listbox.get(selected_index[0])
                selected_autores_listbox.delete(selected_index[0])
                autores_listbox.insert(tk.END, selected_autores)
                autoresget = selected_autores_listbox.get(0, tk.END)
                self.tipoproducto_seleccionado.set(autoresget)
        # def return_values():
        #     autoresget = selected_autores_listbox.get(0, tk.END)

        #     # autoresget = [autor.strip('{') for autor in autoresget]
        #     self.tipoproducto_seleccionado.set(autoresget)
        #     # root.destroy()

        # def filter_autores():
        #     search_str = filter_entry.get().lower()
        #     filtered_autores = [author for author in autores if search_str in author.lower()]
        #     autores_listbox.delete(0, tk.END)
        #     for author in filtered_autores:
        #         autores_listbox.insert(tk.END, author)

        # filter_label = tk.Label(frame, text="Buscar Autor:").pack()
        # filter_entry = tk.Entry(frame)
        # filter_entry.pack()

        # filter_button = tk.Button(frame, text="Buscar", command=filter_autores)
        # filter_button.pack()

        move_button = tk.Button(frame, text="Seleccionar", command=move_author)
        move_button.pack()

        move_back_button = tk.Button(frame, text="Retirar", command=move_back_author)
        move_back_button.pack()

        # return_button = tk.Button(frame, text="Ingresar", command=return_values)
        # return_button.pack()

        # root.mainloop()

    def obtener_tipos_seleccionados(self):
        return self.tipoproducto_seleccionado