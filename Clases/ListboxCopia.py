import tkinter as tk    
from DAO import DAO
from tkinter import messagebox

class ListboxCopia:
    def __init__(self):
        self.copia_seleccionada = tk.StringVar()

    def mostrar_ventana(self, frame):
        dao = DAO()

        global selected_copias_listbox
        global copias_listbox
        etiqueta_copias = tk.Label(frame, text="Copias")
        etiqueta_copias.grid(row=1, column=0, padx=10, pady=10)

        copias_listbox = tk.Listbox(frame)
        copias_listbox.grid(row=2, column=0, padx=10)


        etiqueta_copias_seleccionadas = tk.Label(frame, text="Copias seleccionadas")
        etiqueta_copias_seleccionadas.grid(row=1, column=1, padx=10, pady=10)

        selected_copias_listbox = tk.Listbox(frame)
        selected_copias_listbox.grid(row=2, column=1, padx=10)

        def move_copia():
            if selected_copias_listbox.size() == 1:
                messagebox.showerror("Error", "Ya hay una copia seleccionada")
            else:
                selected_index = copias_listbox.curselection()
                if selected_index:
                    selected_copia = copias_listbox.get(selected_index[0])
                    copias_listbox.delete(selected_index[0])
                    selected_copias_listbox.insert(tk.END, selected_copia)
                copiasget = selected_copias_listbox.get(0, tk.END)
                self.copia_seleccionada.set(copiasget)

        def move_back_copia():
            selected_index = selected_copias_listbox.curselection()
            if selected_index:
                selected_categories = selected_copias_listbox.get(selected_index[0])
                selected_copias_listbox.delete(selected_index[0])
                copias_listbox.insert(tk.END, selected_categories)
                copiasget = selected_copias_listbox.get(0, tk.END)
                self.copia_seleccionada.set(copiasget)

        move_button = tk.Button(frame, text="Seleccionar", command=move_copia)
        move_button.grid(row=3, column=0, pady=10)

        move_back_button = tk.Button(frame, text="Retirar", command=move_back_copia)
        move_back_button.grid(row=3, column=1, pady=10)

    def obtener_copias_seleccionadas(self):
        return self.copia_seleccionada
    
    def mostrar_copias(self,idbodega):

        copias_listbox.delete(0, tk.END)
        selected_copias_listbox.delete(0, tk.END)
        dao = DAO()
        copias = dao.obtener_copias(idbodega)
        for copia in copias:
            copias_listbox.insert(tk.END, copia)
