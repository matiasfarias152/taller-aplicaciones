#CREANDO LOGIN CON PYTHON Y TKINTER.

#IMPORTAMOS LIBRERÍAS NECESARIAS.
from tkinter import *
import os
from DAO import *
from User import *

#CREAMOS VENTANA PRINCIPAL.
def ventana_inicio():
    global ventana_principal
    pestas_color="DarkGrey"
    ventana_principal=Tk()
    ventana_principal.geometry("300x250")#DIMENSIONES DE LA VENTANA
    ventana_principal.title("Login con tkinter")#TITULO DE LA VENTANA
    Label(text="Escoja su opción", bg="LightGreen", width="300", height="2", font=("Calibri", 13)).pack()#ETIQUETA CON TEXTO
    Label(text="").pack()
    Button(text="Acceder", height="2", width="30", bg=pestas_color, command=login).pack() #BOTÓN "Acceder"
    Label(text="").pack()
    Button(text="Registrarse", height="2", width="30", bg=pestas_color, command=registro).pack() #BOTÓN "Registrarse".
    Label(text="").pack()
    ventana_principal.mainloop()

#CREAMOS VENTANA PARA REGISTRO.
def registro():
    global ventana_registro
    ventana_registro = Toplevel(ventana_principal)
    ventana_registro.title("Registro")
    ventana_registro.geometry("300x250")
 
    global nombre_usuario
    global clave
    global telefono
    global correo
    global rut
    global entrada_telefono
    global entrada_correo
    global entrada_rut
    global entrada_nombre
    global entrada_clave
    nombre_usuario = StringVar() #DECLARAMOS "string" COMO TIPO DE DATO PARA "nombre_usuario"
    clave = StringVar() #DECLARAMOS "string" COMO TIPO DE DATO PARA "clave"
    telefono = IntVar()#  comentar
    correo = StringVar()# comentar
    rut = StringVar()# falta comentar



    Label(ventana_registro, text="Introduzca datos", bg="LightGreen").pack()
    Label(ventana_registro, text="").pack()
    etiqueta_nombre = Label(ventana_registro, text="Nombre de usuario * ")
    etiqueta_nombre.pack()
    entrada_nombre = Entry(ventana_registro, textvariable=nombre_usuario) #ESPACIO PARA INTRODUCIR EL NOMBRE.
    entrada_nombre.pack()
    etiqueta_clave = Label(ventana_registro, text="Contraseña * ")
    etiqueta_clave.pack()
    entrada_clave = Entry(ventana_registro, textvariable=clave, show='*') #ESPACIO PARA INTRODUCIR LA CONTRASEÑA.
    entrada_clave.pack()
    etiqueta_correo = Label(ventana_registro, text="Correo * ")
    etiqueta_correo.pack()
    entrada_correo = Entry(ventana_registro, textvariable=correo)
    entrada_correo.pack()
    etiqueta_telefono = Label(ventana_registro, text="Telefono *")
    etiqueta_telefono.pack()
    entrada_telefono = Entry(ventana_registro, textvariable=telefono)
    entrada_telefono.pack()
    etiqueta_rut = Label(ventana_registro, text="Rut *")
    etiqueta_rut.pack()
    entrada_rut = Entry(ventana_registro, textvariable=rut)
    entrada_rut.pack()

    Label(ventana_registro, text="").pack()
    Button(ventana_registro, text="Registrarse", width=10, height=1, bg="LightGreen", command = registro_usuario).pack() #BOTÓN "Registrarse"

#CREAMOS VENTANA PARA LOGIN.

def login():
    global ventana_login
    ventana_login = Toplevel(ventana_principal)
    ventana_login.title("Acceso a la cuenta")
    ventana_login.geometry("300x250")
    Label(ventana_login, text="Introduzca nombre de usuario y contraseña").pack()
    Label(ventana_login, text="").pack()
 
    global verifica_usuario
    global verifica_clave
 
    verifica_usuario = StringVar()
    verifica_clave = StringVar()
 
    global entrada_login_usuario
    global entrada_login_clave
 
    Label(ventana_login, text="Nombre usuario * ").pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    Label(ventana_login, text="").pack()
    Label(ventana_login, text="Contraseña * ").pack()
    entrada_login_clave = Entry(ventana_login, textvariable=verifica_clave, show= '*')
    entrada_login_clave.pack()
    Label(ventana_login, text="").pack()
    Button(ventana_login, text="Acceder", width=10, height=1, command = verifica_login).pack()

#VENTANA "VERIFICACION DE LOGIN".

def verifica_login():
    usuario1 = verifica_usuario.get()
    clave1 = verifica_clave.get()
    entrada_login_usuario.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Nombre usuario *" AL MOSTRAR NUEVA VENTANA.
    entrada_login_clave.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Contraseña *" AL MOSTRAR NUEVA VENTANA.
    dao = DAO()
    resultado = dao.validar_credenciales(usuario1,clave1)
    if resultado == True:
        exito_login()
    elif resultado == False:
        no_clave()




    # lista_archivos = os.listdir() #GENERA LISTA DE ARCHIVOS UBICADOS EN EL DIRECTORIO.
    # #SI EL NOMBRE SE ENCUENTRA EN LA LISTA DE ARCHIVOS..
    # if usuario1 in lista_archivos:
    #     archivo1 = open(usuario1, "r") #APERTURA DE ARCHIVO EN MODO LECTURA
    #     verifica = archivo1.read().splitlines() #LECTURA DEL ARCHIVO QUE CONTIENE EL nombre Y contraseña.
    #     #SI LA CONTRASEÑA INTRODUCIDA SE ENCUENTRA EN EL ARCHIVO...
    #     if clave1 in verifica:
    #         exito_login() #...EJECUTAR FUNCIÓN "exito_login()"
    #     #SI LA CONTRASEÑA NO SE ENCUENTRA EN EL ARCHIVO....
    #     else:
    #         no_clave() #...EJECUTAR "no_clave()"
    # #SI EL NOMBRE INTRODUCIDO NO SE ENCUENTRA EN EL DIRECTORIO...
    # else:
    #     no_usuario() #..EJECUTA "no_usuario()".


# VENTANA "Login finalizado con exito".
 
def exito_login():
    global ventana_exito
    ventana_exito = Toplevel(ventana_login)
    ventana_exito.title("Exito")
    ventana_exito.geometry("150x100")
    Label(ventana_exito, text="Login finalizado con exito").pack()
    Button(ventana_exito, text="OK", command=borrar_exito_login).pack()
 
#VENTANA DE "Contraseña incorrecta".
 
def no_clave():
    global ventana_no_clave
    ventana_no_clave = Toplevel(ventana_login)
    ventana_no_clave.title("ERROR")
    ventana_no_clave.geometry("150x100")
    Label(ventana_no_clave, text="Credenciales Incorrectas").pack()
    Button(ventana_no_clave, text="OK", command=borrar_no_clave).pack() #EJECUTA "borrar_no_clave()".
 
#VENTANA DE "Usuario no encontrado".
 
def no_usuario():
    global ventana_no_usuario
    ventana_no_usuario = Toplevel(ventana_login)
    ventana_no_usuario.title("ERROR")
    ventana_no_usuario.geometry("150x100")
    Label(ventana_no_usuario, text="Usuario no encontrado").pack()
    Button(ventana_no_usuario, text="OK", command=borrar_no_usuario).pack() #EJECUTA "borrar_no_usuario()"

#CERRADO DE VENTANAS

def borrar_exito_login():
    ventana_exito.destroy()
 
 
def borrar_no_clave():
    ventana_no_clave.destroy()
 
 
def borrar_no_usuario():
    ventana_no_usuario.destroy()

#REGISTRO USUARIO
 
def registro_usuario():
    dao = DAO()
    usuario_info = nombre_usuario.get()       #EJEMPLO USO DEL DAO
    clave_info = clave.get()
    correo_info = correo.get()
    telefono_info = telefono.get()
    rut_info = rut.get()
    usuario = User(usuario_info,clave_info,correo_info,telefono_info,rut_info)
    dao.crear_usuario(usuario)
    
    file = open(usuario_info, "w") #CREACION DE ARCHIVO CON "nombre" y "clave"
    file.write(usuario_info + "\n")
    file.write(clave_info)
    file.close()
 
    entrada_nombre.delete(0, END)
    entrada_clave.delete(0, END)
 
    Label(ventana_registro, text="Registro completado con éxito", fg="green", font=("calibri", 11)).pack()
 
 
ventana_inicio()  #EJECUCIÓN DE LA VENTANA DE INICIO.
 

#no tener todas las ventanas abiertas, actualziar la misma ventana a la hora de clickear
    
