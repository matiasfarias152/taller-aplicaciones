from tkinter import *

ventana = Tk()
ventana.geometry("900x550")
ventana.title("Inicio de Sesion")
ventana.resizable(False,False)
ventana.config(background="#D4EFDF")
main_title = Label(text="Ingrese sus credenciales", font=("Cambria",13),bg="#56CD63",fg="white",width="550",height="2")
main_title.pack()

usermane_label= Label(text="Nombre de Usuario", bg="#F4F6F7")
usermane_label.place(x=22, y=70)
password_label= Label(text="Contraseña", bg="#F4F6F7")
password_label.place(x=22, y=130)
mainloop()