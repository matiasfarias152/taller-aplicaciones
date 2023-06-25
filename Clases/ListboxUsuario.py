import tkinter as tk    
from DAO import DAO

class ListboxUsuario:
    def __init__(self):
        self.usuario_seleccionado = tk.StringVar()
    
    def mostrar_ventana(self,frame):
        dao = DAO()
    

        usuarios_listbox = tk.Listbox(frame)
        
        
        usuarios = dao.obtener_usuarios()
        for usuario in usuarios:
            usuarios_listbox.insert(tk.END, usuario)
            usuarios_listbox.pack(side=tk.LEFT)
            usuarios_listbox.configure(width=25, height=15)


        selected_usuarios_listbox = tk.Listbox(frame)
        selected_usuarios_listbox.pack(side=tk.RIGHT)
        selected_usuarios_listbox.configure(width=25, height=15)

        def move_usuario():
            selected_index = usuarios_listbox.curselection()
            if selected_index:
                selected_usuario = usuarios_listbox.get(selected_index[0])
                usuarios_listbox.delete(selected_index[0])
                selected_usuarios_listbox.insert(tk.END, selected_usuario)
            usuarioesget = selected_usuarios_listbox.get(0, tk.END)
            self.usuario_seleccionado.set(usuarioesget)

        def move_back_usuario():
            selected_index = selected_usuarios_listbox.curselection()
            if selected_index:
                selected_categories = selected_usuarios_listbox.get(selected_index[0])
                selected_usuarios_listbox.delete(selected_index[0])
                usuarios_listbox.insert(tk.END, selected_categories)
                usuarioesget = selected_usuarios_listbox.get(0, tk.END)
                self.usuario_seleccionado.set(usuarioesget)
        # def return_values():
        #     usuarioesget = selected_usuarios_listbox.get(0, tk.END)

        #     # usuarioesget = [usuario.strip('{') for usuario in usuarioesget]
        #     self.tipoproducto_seleccionado.set(usuarioesget)
        #     # root.destroy()

        def filter_usuarios():
            search_str = filter_entry.get().lower()
            filtered_usuarios = [usuario for usuario in usuarios if search_str in usuario.lower()]
            usuarios_listbox.delete(0, tk.END)
            for usuario in filtered_usuarios:
                usuarios_listbox.insert(tk.END, usuario)

        filter_label = tk.Label(frame, text="Buscar Usuario:").pack()
        filter_entry = tk.Entry(frame)
        filter_entry.pack()

        filter_button = tk.Button(frame, text="Buscar", command=filter_usuarios)
        filter_button.pack()

        move_button = tk.Button(frame, text="Seleccionar", command=move_usuario)
        move_button.pack()

        move_back_button = tk.Button(frame, text="Retirar", command=move_back_usuario)
        move_back_button.pack()

        # return_button = tk.Button(frame, text="Ingresar", command=return_values)
        # return_button.pack()

        # root.mainloop()

    def obtener_usuario_seleccionados(self):
        return self.usuario_seleccionado
