import tkinter as tk    
from DAO import DAO
from tkinter import messagebox

class ListboxBodega:
    def __init__(self):
        self.bodega_seleccionada = tk.StringVar()

    def mostrar_ventana(self, frame):
        """
        Muestra la ventana con la lista de bodegas y la lista de bodegas seleccionadas.
        
        Parámetros:
        - frame: El marco de la ventana donde se mostrarán los elementos.
        """

        dao = DAO()

        global selected_bodegas_listbox

        etiqueta_bodegas = tk.Label(frame, text="Bodegas")
        etiqueta_bodegas.grid(row=1, column=0, padx=10, pady=10)

        bodegas_listbox = tk.Listbox(frame)
        bodegas_listbox.grid(row=2, column=0, padx=10)

        bodegas = dao.obtener_bodegas()
        for bodega in bodegas:
            bodegas_listbox.insert(tk.END, bodega)

        etiqueta_bodegas_seleccionadas = tk.Label(frame, text="Bodegas seleccionadas")
        etiqueta_bodegas_seleccionadas.grid(row=1, column=1, padx=10, pady=10)

        selected_bodegas_listbox = tk.Listbox(frame)
        selected_bodegas_listbox.grid(row=2, column=1, padx=10)

        def move_bodega():
            """
            Mueve la bodega seleccionada de la lista de bodegas a la lista de bodegas seleccionadas.
            """
            if selected_bodegas_listbox.size() == 1:
                messagebox.showerror("Error", "Ya hay una bodega seleccionada")
            else:
                selected_index = bodegas_listbox.curselection()
                if selected_index:
                    selected_bodega = bodegas_listbox.get(selected_index[0])
                    bodegas_listbox.delete(selected_index[0])
                    selected_bodegas_listbox.insert(tk.END, selected_bodega)
                bodegasget = selected_bodegas_listbox.get(0, tk.END)
                self.bodega_seleccionada.set(bodegasget)

        def move_back_bodega():
            """
            Mueve la bodega seleccionada de la lista de bodegas seleccionadas a la lista de bodegas.
            """
            selected_index = selected_bodegas_listbox.curselection()
            if selected_index:
                selected_categories = selected_bodegas_listbox.get(selected_index[0])
                selected_bodegas_listbox.delete(selected_index[0])
                bodegas_listbox.insert(tk.END, selected_categories)
                bodegasget = selected_bodegas_listbox.get(0, tk.END)
                self.bodega_seleccionada.set(bodegasget)

        move_button = tk.Button(frame, text="Seleccionar", command=move_bodega)
        move_button.grid(row=3, column=0, pady=10)

        move_back_button = tk.Button(frame, text="Retirar", command=move_back_bodega)
        move_back_button.grid(row=3, column=1, pady=10)

    def obtener_bodegas_seleccionadas(self):
        """
        Obtiene las bodegas seleccionadas.
        
        Retorna:
        - Las bodegas seleccionadas en forma de cadena.
        """
        return self.bodega_seleccionada
    
    def clear_listbox(listbox):
        """
        Limpia el contenido de un cuadro de lista.
        
        Parámetros:
        - listbox: El cuadro de lista a limpiar.
        """
        selected_bodegas_listbox.delete(0, tk.END)

    def tamanio_selected(self):
        """
        Obtiene el tamaño de la lista de bodegas seleccionadas.
        
        Retorna:
        - El tamaño de la lista de bodegas seleccionadas.
        """
        tamanio = selected_bodegas_listbox.size()
        print(tamanio)
        return tamanio