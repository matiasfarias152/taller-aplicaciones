from tkinter import *
from tkinter.ttk import Combobox
from DAO import *


def mostrar_error():
    label_error = Label(ventana_principal, text="Credenciales inválidas")
    label_error.pack()

def cerrar_frame():
    # Cerrar frame anterior
    if 'ventana_frame' in globals():
        ventana_frame.destroy()

def verifica_login():
    usuario1 = verifica_usuario.get()
    clave1 = verifica_clave.get()
    entrada_login_usuario.delete(0, END)
    entrada_login_clave.delete(0, END)
    dao = DAO()
    resultado = dao.validar_credenciales(usuario1, clave1)
    if resultado and dao.validar_permisos(usuario1) == 1:
        mostrar_menu()
    else:
        mostrar_error()


def registro_usuario():
    dao = DAO()
    usuario_info = nombre_usuario.get()
    clave_info = clave.get()
    correo_info = correo.get()
    telefono_info = telefono.get()
    rut_info = rut.get()
    roles = entrada_rol.get()
    idtipo = dao.obtener_idtipousuario(roles)

    usuario = User("", telefono_info, correo_info, usuario_info, rut_info, idtipo, clave_info)
    dao.crear_usuario(usuario)

    entrada_nombre.delete(0, END)
    entrada_clave.delete(0, END)
    entrada_correo.delete(0, END)
    entrada_telefono.delete(0, END)
    entrada_rut.delete(0, END)


def registro_autor():
    dao = DAO()
    nombre = entrada_autor.get()
    autor = Autor("", nombre)
    dao.registrarAutor(autor)


def frame_registrarautor():
    global autor
    global entrada_autor
    global ventana_frame

    autor = StringVar()

    # Cerrar frame anterior
    cerrar_frame()

    ventana_frame = Frame(ventana_admin, width=400, height=400)

    Label(ventana_frame, text='Introduzca datos', bg='LightGreen').pack()
    Label(ventana_frame, text="").pack()

    etiqueta_autor = Label(ventana_frame, text='Nombre del autor *')
    etiqueta_autor.pack()
    entrada_autor = Entry(ventana_frame, textvariable=autor)
    entrada_autor.pack()

    Button(ventana_frame, text="Registrarse", width=10, height=1, bg="LightGreen", command=registro_autor).pack()

    ventana_frame.pack(fill='both', expand=1)


def frame_registrarusuario():
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
    global entrada_rol
    global ventana_frame

    nombre_usuario = StringVar()
    clave = StringVar()
    telefono = IntVar()
    correo = StringVar()
    rut = StringVar()

    # Cerrar frame anterior
    cerrar_frame()

    ventana_frame = Frame(ventana_admin, width=400, height=400)
    dao = DAO()
    roles = dao.obtener_tiposusuario()

    Label(ventana_frame, text="Introduzca datos", bg="LightGreen").pack()
    Label(ventana_frame, text="").pack()

    etiqueta_nombre = Label(ventana_frame, text="Nombre de usuario * ")
    etiqueta_nombre.pack()
    entrada_nombre = Entry(ventana_frame, textvariable=nombre_usuario)
    entrada_nombre.pack()

    etiqueta_clave = Label(ventana_frame, text="Contraseña * ")
    etiqueta_clave.pack()
    entrada_clave = Entry(ventana_frame, textvariable=clave, show='*')
    entrada_clave.pack()

    etiqueta_correo = Label(ventana_frame, text="Correo * ")
    etiqueta_correo.pack()
    entrada_correo = Entry(ventana_frame, textvariable=correo)
    entrada_correo.pack()

    etiqueta_telefono = Label(ventana_frame, text="Telefono *")
    etiqueta_telefono.pack()
    entrada_telefono = Entry(ventana_frame, textvariable=telefono)
    entrada_telefono.pack()

    etiqueta_rut = Label(ventana_frame, text="Rut *")
    etiqueta_rut.pack()
    entrada_rut = Entry(ventana_frame, textvariable=rut)
    entrada_rut.pack()

    etiqueta_rol = Label(ventana_frame, text="Selecciona una opción *")
    etiqueta_rol.pack()
    entrada_rol = Combobox(ventana_frame, values=roles, state='readonly')
    entrada_rol.pack()

    Button(ventana_frame, text="Registrarse", width=10, height=1, bg="LightGreen", command=registro_usuario).pack()

    ventana_frame.pack(fill='both', expand=1)


def mostrar_menu():
    ventana_principal.destroy()
    global ventana_admin
    ventana_admin = Tk()
    ventana_admin.title("Menú principal")

    menu_admin = Menu(ventana_admin)
    opciones_registrar = Menu(menu_admin)
    opciones_registrar.add_command(label='Registrar usuario', command=frame_registrarusuario)
    opciones_registrar.add_command(label='Registrar producto')
    opciones_registrar.add_command(label='Registrar categoría')
    opciones_registrar.add_command(label='Registrar autor', command=frame_registrarautor)
    opciones_registrar.add_command(label='Registrar tipo de producto')

    opciones_eliminar = Menu(menu_admin)
    opciones_eliminar.add_command(label='Eliminar productos')
    opciones_eliminar.add_command(label='Eliminar editorial')
    opciones_eliminar.add_command(label='Eliminar bodega')

    menu_admin.add_cascade(label='Registrar', menu=opciones_registrar)
    menu_admin.add_cascade(label='Eliminar', menu=opciones_eliminar)
    ventana_admin.config(menu=menu_admin)

    ventana_admin.mainloop()


ventana_principal = Tk()
ventana_principal.geometry("300x250")
ventana_principal.title("Login con tkinter")
Label(text="").pack()

verifica_usuario = StringVar()
verifica_clave = StringVar()

entrada_login_usuario = Entry(ventana_principal, textvariable=verifica_usuario)
entrada_login_usuario.pack()
Label(ventana_principal, text="").pack()
Label(ventana_principal, text="Contraseña * ").pack()
entrada_login_clave = Entry(ventana_principal, textvariable=verifica_clave, show='*')
entrada_login_clave.pack()
Label(ventana_principal, text="").pack()
Button(ventana_principal, text="Acceder", width=10, height=1, command=verifica_login).pack()

ventana_principal.mainloop()