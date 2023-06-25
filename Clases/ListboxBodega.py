import tkinter as tk    
from DAO import DAO

class ListboxBodega:
    def __init__(self):
        self.bodega_seleccionada = tk.StringVar()
    
    def mostrar_ventana(self,frame):
        dao = DAO()
    

        bodegas_listbox = tk.Listbox(frame)

        bodegas = dao.obtener_bodegas()
        for autor in bodegas:
            bodegas_listbox.insert(tk.END, autor)
            bodegas_listbox.pack(side=tk.LEFT)
            bodegas_listbox.configure(width=25, height=15)


        selected_bodegas_listbox = tk.Listbox(frame)
        selected_bodegas_listbox.pack(side=tk.RIGHT)
        selected_bodegas_listbox.configure(width=25, height=15)

        def move_bodega():
            selected_index = bodegas_listbox.curselection()
            if selected_index:
                selected_bodega = bodegas_listbox.get(selected_index[0])
                bodegas_listbox.delete(selected_index[0])
                selected_bodegas_listbox.insert(tk.END, selected_bodega)
            autoresget = selected_bodegas_listbox.get(0, tk.END)
            self.bodega_seleccionada.set(autoresget)

        def move_back_bodega():
            selected_index = selected_bodegas_listbox.curselection()
            if selected_index:
                selected_bodegas = selected_bodegas_listbox.get(selected_index[0])
                selected_bodegas_listbox.delete(selected_index[0])
                bodegas_listbox.insert(tk.END, selected_bodegas)
                autoresget = selected_bodegas_listbox.get(0, tk.END)
                self.bodega_seleccionada.set(autoresget)
        # def return_values():
        #     autoresget = selected_bodegas_listbox.get(0, tk.END)

        #     # autoresget = [autor.strip('{') for autor in autoresget]
        #     self.tipoproducto_seleccionado.set(autoresget)
        #     # root.destroy()

        def filter_bodegas():
            search_str = filter_entry.get().lower()
            filtered_bodegas = [bodega for bodega in bodegas if search_str in bodega.lower()]
            bodegas_listbox.delete(0, tk.END)
            for bodega in filtered_bodegas:
                bodegas_listbox.insert(tk.END, bodega)

        filter_label = tk.Label(frame, text="Buscar Bodega:").pack()
        filter_entry = tk.Entry(frame)
        filter_entry.pack()

        filter_button = tk.Button(frame, text="Buscar", command=filter_bodegas)
        filter_button.pack()

        move_button = tk.Button(frame, text="Seleccionar", command=move_bodega)
        move_button.pack()

        move_back_button = tk.Button(frame, text="Retirar", command=move_back_bodega)
        move_back_button.pack()

        # return_button = tk.Button(frame, text="Ingresar", command=return_values)
        # return_button.pack()

        # root.mainloop()

    def obtener_bodegas_seleccionadas(self):
        return self.bodega_seleccionada
