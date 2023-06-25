import tkinter as tk    
from DAO import DAO

class ListboxUsuario:
    def __init__(self):
        self.usuario_seleccionado = tk.StringVar()
    
    def mostrar_ventana(self,frame):
        dao = DAO()
    

        usuarios_listbox = tk.Listbox(frame)

        
        usuarios = dao.obtener_usuarios()
        for autor in usuarios:
            usuarios_listbox.insert(tk.END, autor)
            usuarios_listbox.pack(side=tk.LEFT)
            usuarios_listbox.configure(width=25, height=15)


        selected_usuarios_listbox = tk.Listbox(frame)
        selected_usuarios_listbox.pack(side=tk.RIGHT)
        selected_usuarios_listbox.configure(width=25, height=15)

        def move_user():
            selected_index = usuarios_listbox.curselection()
            if selected_index:
                selected_user = usuarios_listbox.get(selected_index[0])
                usuarios_listbox.delete(selected_index[0])
                selected_usuarios_listbox.insert(tk.END, selected_user)
            autoresget = selected_usuarios_listbox.get(0, tk.END)
            self.usuario_seleccionado.set(autoresget)

        def move_back_user():
            selected_index = selected_usuarios_listbox.curselection()
            if selected_index:
                selected_usuarios = selected_usuarios_listbox.get(selected_index[0])
                selected_usuarios_listbox.delete(selected_index[0])
                usuarios_listbox.insert(tk.END, selected_usuarios)
                autoresget = selected_usuarios_listbox.get(0, tk.END)
                self.usuario_seleccionado.set(autoresget)
        # def return_values():
        #     autoresget = selected_usuarios_listbox.get(0, tk.END)

        #     # autoresget = [autor.strip('{') for autor in autoresget]
        #     self.tipoproducto_seleccionado.set(autoresget)
        #     # root.destroy()

        def filter_usuarios():
            search_str = filter_entry.get().lower()
            filtered_usuarios = [user for user in usuarios if search_str in user.lower()]
            usuarios_listbox.delete(0, tk.END)
            for user in filtered_usuarios:
                usuarios_listbox.insert(tk.END, user)

        filter_label = tk.Label(frame, text="Buscar Usuario:").pack()
        filter_entry = tk.Entry(frame)
        filter_entry.pack()

        filter_button = tk.Button(frame, text="Buscar", command=filter_usuarios)
        filter_button.pack()

        move_button = tk.Button(frame, text="Seleccionar", command=move_user)
        move_button.pack()

        move_back_button = tk.Button(frame, text="Retirar", command=move_back_user)
        move_back_button.pack()

        # return_button = tk.Button(frame, text="Ingresar", command=return_values)
        # return_button.pack()

        # root.mainloop()

    def obtener_usuario_seleccionados(self):
        return self.usuario_seleccionado
