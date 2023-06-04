from tkinter import *

ventana = Tk()
ventana.geometry("900x550")
ventana.title("Inicio de Sesion")
ventana.resizable(False,False)
ventana.config(background="#D4EFDF")
main_title = Label(text="Ingrese sus credenciales", font=("Cambria",13),bg="#56CD63",fg="white",width="550",height="2")
main_title.pack()

username_label= Label(text="Nombre de Usuario", bg="#F4F6F7")
username_label.place(x=22, y=70)
password_label= Label(text="Contraseña", bg="#F4F6F7")
password_label.place(x=22, y=130)

username = StringVar()
password = StringVar()

username_entry = Entry(textvariable=username,width="40")
password_entry = Entry(textvariable=password,width="40", show="*")

username_entry.place(x=22, y=100)
password_entry.place(x=22, y=160)
mainloop()