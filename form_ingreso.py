from tkinter import *

#recoge los datos y los muestra por consola
def send_data():
    username_data= username.get()
    password_data = str(password.get())
    print(username_data, "\t", password_data)

    #crea un archivo txt en donde se guardaran los datos que van ingresando
    newfile = open("registro.txt", "a") #la "a" significa append
    newfile.write(username_data)
    newfile.write("\t")
    newfile.write(password_data)
    newfile.write("\t")
    newfile.write("\n")
    newfile.close()
    print("Nuevo Usuario Registrado \n Nombre: {} | Contraseña: {}   ".format(username_data,password_data))

    #una vez ingreso los datos al form, lo que hacen estas dos lineas es borrar los datos y dejar clear el form
    username_entry.delete(0,END)
    password_entry.delete(0,END)



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
password_label.place(x=22, y=150)

username = StringVar()
password = StringVar()

username_entry = Entry(textvariable=username,width="40")
password_entry = Entry(textvariable=password,width="40", show="*")

username_entry.place(x=22, y=100)
password_entry.place(x=22, y=180)

submit_btn = Button(ventana, text="Enviar Informacion", command=send_data, width="30", height="2", bg="#F4F6F7")
submit_btn.place(x=22, y=230)

ventana.mainloop()
 