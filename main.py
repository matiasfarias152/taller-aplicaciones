from tkinter import * 
from tkinter.ttk import Combobox
from DAO import *
def mostrar_error():
    label_error = Label(ventana_principal, text="Credenciales invalidas")
    label_error.pack()



    
def verifica_login():
    usuario1 = verifica_usuario.get()
    clave1 = verifica_clave.get()
    entrada_login_usuario.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Nombre usuario *" AL MOSTRAR NUEVA VENTANA.
    entrada_login_clave.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Contraseña *" AL MOSTRAR NUEVA VENTANA.
    dao = DAO()
    resultado = dao.validar_credenciales(usuario1,clave1)
    if resultado == True and dao.validar_permisos(usuario1) == 1:
        mostrar_menu()
    else:
        mostrar_error()


def registro_usuario():
    dao = DAO()#Inicializacion del DAO
    usuario_info = nombre_usuario.get() #Obtener el nobmre de usuario        
    clave_info = clave.get() #Obtener contrasena
    correo_info = correo.get() #Otbener el correo
    telefono_info = telefono.get() #Obtener el telefono
    rut_info = rut.get() #Obtener el rut
    roles = entrada_rol.get() #Obtener el rol
    idtipo = dao.obtener_idtipousuario(roles,)


    usuario = User("",telefono_info,correo_info,usuario_info,rut_info,idtipo,clave_info) #idUser:int ,username:str, password:str,correo:str,rut:str,telefono:int
    dao.crear_usuario(usuario)
    
 
    entrada_nombre.delete(0, END)
    entrada_clave.delete(0, END)
    entrada_correo.delete(0, END)
    entrada_telefono.delete(0, END)
    entrada_rut.delete(0, END)


def registro_autor():
    dao = DAO()
    nombre = entrada_autor.get()
    autor = Autor("",nombre)
    dao.registrarAutor(autor)




def mostrar_menu():
    ventana_principal.destroy()

    
    #Funciones frames
    
    def frame_registrarautor():
        registrar_autor = Frame(ventana_admin, width=400, height=400)
        
        global autor
        global entrada_autor

        autor = StringVar()

        Label(registrar_autor,text='Introduzca datos',bg='LightGreen').pack()
        Label(registrar_autor, text="").pack()
        
        etiqueta_autor = Label(registrar_autor,text='Nombre del autor *')
        etiqueta_autor.pack()
        entrada_autor = Entry(registrar_autor, textvariable=autor)
        entrada_autor.pack()

        Button(registrar_autor, text="Registrarse", width=10, height=1, bg="LightGreen", command = registro_autor).pack() #BOTÓN "Registrarse"

        

        registrar_autor.pack(fill='both',expand = 1)


    def frame_registrarusuario():
        registrar_usuario = Frame(ventana_admin, width=400, height=400)
        dao = DAO()
        roles = dao.obtener_tiposusuario()

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

        nombre_usuario = StringVar() #DECLARAMOS "string" COMO TIPO DE DATO PARA "nombre_usuario"
        clave = StringVar() #DECLARAMOS "string" COMO TIPO DE DATO PARA "clave"
        telefono = IntVar()#  comentar
        correo = StringVar()# comentar
        rut = StringVar()# falta comentar


        Label(registrar_usuario, text="Introduzca datos", bg="LightGreen").pack()
        Label(registrar_usuario, text="").pack()

        etiqueta_nombre = Label(registrar_usuario, text="Nombre de usuario * ")
        etiqueta_nombre.pack()
        entrada_nombre = Entry(registrar_usuario, textvariable=nombre_usuario) #ESPACIO PARA INTRODUCIR EL NOMBRE.
        entrada_nombre.pack()


        etiqueta_clave = Label(registrar_usuario, text="Contraseña * ")
        etiqueta_clave.pack()
        entrada_clave = Entry(registrar_usuario, textvariable=clave, show='*') #ESPACIO PARA INTRODUCIR LA CONTRASEÑA.
        entrada_clave.pack()


        etiqueta_correo = Label(registrar_usuario, text="Correo * ")
        etiqueta_correo.pack()
        entrada_correo = Entry(registrar_usuario, textvariable=correo)
        entrada_correo.pack()


        etiqueta_telefono = Label(registrar_usuario, text="Telefono *")
        etiqueta_telefono.pack()
        entrada_telefono = Entry(registrar_usuario, textvariable=telefono)
        entrada_telefono.pack()


        etiqueta_rut = Label(registrar_usuario, text="Rut *")
        etiqueta_rut.pack()
        entrada_rut = Entry(registrar_usuario, textvariable=rut)
        entrada_rut.pack()


        etiqueta_rol = Label(registrar_usuario, text="Selecciona una opción *")
        etiqueta_rol.pack()
        entrada_rol = Combobox(registrar_usuario, values=roles, state='readonly')
        entrada_rol.pack()

    
        Button(registrar_usuario, text="Registrarse", width=10, height=1, bg="LightGreen", command = registro_usuario).pack() #BOTÓN "Registrarse"

        

        registrar_usuario.pack(fill='both',expand = 1)




    # Crea la nueva ventana para el menú principal
    ventana_admin = Tk()
    ventana_admin.title("Menú principal")

    # Agrega los widgets del menú principal aquí

    #Menu 
    menu_admin = Menu(ventana_admin)

    #Opciones Menu

    #Opcion registrar
    opciones_registrar = Menu(menu_admin)
    opciones_registrar.add_command(label='Registrar usuario',command=frame_registrarusuario)
    opciones_registrar.add_command(label='Registrar producto')
    opciones_registrar.add_command(label='Registrar categoria')
    opciones_registrar.add_command(label='Registrar autor', command=frame_registrarautor)
    opciones_registrar.add_command(label='Registrar tipo de producto')


    opciones_eliminar = Menu(menu_admin)
    opciones_eliminar.add_command(label='Eliminar productos')
    opciones_eliminar.add_command(label='Eliminar editorial')
    opciones_eliminar.add_command(label='Eliminar bodega')


    #Agregar opcion al menu principal

    menu_admin.add_cascade(label='Registrar',menu=opciones_registrar)
    menu_admin.add_cascade(label='Eliminar',menu=opciones_eliminar)
    

    #Asignar al menu principal a la ventana
    ventana_admin.config(menu=menu_admin)






    #Frame registrar usuario



    ventana_admin.mainloop()

         


       
        



global ventana_principal
ventana_principal = Tk()
ventana_principal.geometry("300x250")#DIMENSIONES DE LA VENTANA
ventana_principal.title("Login con tkinter")#TITULO DE LA VENTANA
Label(text="").pack()

global verifica_usuario
global verifica_clave
 
verifica_usuario = StringVar()
verifica_clave = StringVar()
 
global entrada_login_usuario
global entrada_login_clave
 
Label(ventana_principal, text="Nombre usuario * ").pack()
entrada_login_usuario = Entry(ventana_principal, textvariable=verifica_usuario)
entrada_login_usuario.pack()
Label(ventana_principal, text="").pack()
Label(ventana_principal, text="Contraseña * ").pack()
entrada_login_clave = Entry(ventana_principal, textvariable=verifica_clave, show= '*')
entrada_login_clave.pack()
Label(ventana_principal, text="").pack()
Button(ventana_principal, text="Acceder", width=10, height=1, command = verifica_login).pack()








# menu_admin.add_command(Label='Registrar usuario', command =)
 


ventana_principal.mainloop()

