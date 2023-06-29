from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk
from tkcalendar import *
from DAO import *
from Clases.Formcategoriastest import *
from Clases.Formtipoproducto import *
from Clases.Producto import *
from Clases.ListboxProductos import *
from Clases.ListboxAutor import *
from Clases.Producto_Autor import *
from Clases.Bodega import *
from Clases.ListboxBodega import *
from Clases.ListboxUsuario import *
from Clases.Bodega_usuario import *
from Clases.Copia import *
from Clases.ListboxCopia import *
from Clases.BodegaMov import *
from Clases.CopiaMovimiento import *

categorias_seleccionadas = []

def mostrar_error():
    label_error = Label(ventana_principal, text="Credenciales inválidas")
    label_error.pack()

def cerrar_frame():
    # Cerrar frame anterior
    if 'ventana_frame' in globals():
        ventana_frame.destroy()

def verifica_login():
    global usuario1
    usuario1 = verifica_usuario.get()
    clave1 = verifica_clave.get()
    entrada_login_usuario.delete(0, END)
    entrada_login_clave.delete(0, END)
    dao = DAO()
    resultado = dao.validar_credenciales(usuario1, clave1)
    if resultado and dao.validar_permisos(usuario1) == 1:
        mostrar_menuadmin()
    elif resultado and dao.validar_permisos(usuario1) == 2:
        mostrar_menubodeguero()
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


def registro_categoria():
    dao = DAO()
    nombre = nombre_categoria.get()
    categoria = Categoria("", nombre)
    dao.registrarCategoria(categoria)

def registro_autor():
    dao = DAO()
    nombre = entrada_autor.get()
    autor = Autor("", nombre)
    dao.registrarAutor(autor)

def registro_tipoproducto():
    dao = DAO()
    nombre = nombre_tipo.get()
    tipo = Tipo_producto("",nombre)
    dao.registrarTipoproducto(tipo)

def registro_productos():
    dao = DAO()
    categoria = entry_cat.get()
    tipos = entry_tipo.get()
    descripcion = info_descripcion.get()
    idcategoria = dao.obtener_idcategorias(categoria)
    idtipo = dao.obtener_idtipoproducto(tipos)
    producto = Producto("",descripcion,idcategoria,idtipo)
    dao.registrarProducto(producto)
    
def registro_bodega():
    dao = DAO()
    nombre = nombrebodega.get()
    ubicacion = ubicacionbodega.get()
    bodega = Bodega("",nombre,ubicacion)
    dao.registrarBodega(bodega)

def asignar_autor():
    dao = DAO()
    producto = entry_producto.get()
    autorr = autores.get()
    print('AUTORES SELECCIONADOS: ')
    print(autorr) #('yo','pablo neruda','b')
    idproducto =  dao.obtener_idproductos(producto)
    autorr = eval(autorr)
    print('CONVERSION A TUPLA: ')
    print(autorr)
    for a in autorr:
        print('AUTOR: ')
        print(a)
        idautor = dao.obtener_idautor(a)
        producto_autor = Producto_Autor("",idproducto,idautor)
        dao.asignarAutor(producto_autor)

def asignar_bodega():
    dao = DAO()
    usuario = usuarios.get()
    bodega = bodegas.get()
    print('BODEGA SELECCIONADA: ')
    print(bodega)
    bodegatupla = eval(bodega)
    
    

    idbodega = dao.obtener_idbodega(bodegatupla[0])
    usuario = eval(usuario)

    for user in usuario:
        idusuario = dao.obtener_idusuario(user)
        bodega_usuario = Bodega_usuario("",idusuario,idbodega)
        dao.asignarBodega(bodega_usuario)

def asignar_copia():
    dao = DAO()
    nombrecopia = nombre_copia.get()
    descripcioncopia = descripcion_copia.get()
    producto = productoscopia.get()
    bodega = bodegascopia.get()
    print('BODEGA SELECCIONADA: ')
    print('PRODUCTO SELECCIONADO: ')
    print(bodega)
    print(producto)

    productotupla = eval(producto)
    bodegatupla = eval(bodega)

    print(productotupla[0],bodegatupla[0])
    idproducto = dao.obtener_idproductos(productotupla[0])
    idbodega = dao.obtener_idbodega(bodegatupla[0])

    cantidad = cantidad_copia.get()
  

    limite = 0
    while(cantidad-1 >= limite):
        copia = Copia("",nombrecopia,descripcioncopia,idproducto,idbodega)
        dao.asignarCopia(copia)
        limite+=1

def realizarmovimiento():

    #Tabla Movimiento

    dao = DAO()
    
    
    fecha_movimiento = cal.get_date()
    print(fecha_movimiento)

    print('USUARIO SELECCIONADO')
    print(usuario1)


    idusuario = dao.obtener_idusuario(usuario1)

    movimiento = Movimiento("",fecha_movimiento,idusuario)

    dao.asignarMovimiento(movimiento)


    #Tabla bodegamov
    
    bodegasalida = salida_bodega.get()
    bodegaentrada = entrada_bodega.get()

    print(f'BODEGA SALIDA {bodegasalida}')
    print(f'BODEGA ENTRADA {bodegaentrada}')

    idbodegasalida = dao.obtener_idbodega(bodegasalida)
    idbodegaentrada = dao.obtener_idbodega(bodegaentrada)
    idmovimiento = dao.obtener_ultimomov()


    print(f'ID BODEGA  SALIDA {idbodegasalida}')
    print(f'ID BODEGA  ENTRADA {idbodegaentrada}')
    print(f'ID MOVIMIENTO {idmovimiento}')
    #Ingresar movimiento de bodega de salida

    bodegamovsalida = BodegaMov("",0,idmovimiento,idbodegasalida)

    dao.registrarBodegamov(bodegamovsalida)


    #Ingresar movimiento de bodega de entrada

    bodegamoventrada = BodegaMov("",1,idmovimiento,idbodegaentrada)

    dao.registrarBodegamov(bodegamoventrada)


    #Ingresar copia_movimiento 

    copia = copiamovimiento.get()
    print(f'COPIA MOVIMIENTO: {copia}')
    copiatupla = eval(copia)

    print(copiatupla)


    idcopia = dao.obtener_idcopia(copiatupla[0])

    copia_movimiento = CopiaMovimiento("",idcopia,idmovimiento)

    dao.registrarCopiamovimiento(copia_movimiento)


def frame_registrarbodega():
    global nombrebodega
    global ubicacionbodega

    global ventana_frame
    nombrebodega = StringVar()
    ubicacionbodega = StringVar()

    # Cerrar frame anterior
    cerrar_frame()

    ventana_frame = Frame(ventana_admin, width=400, height=400)

    Label(ventana_frame, text='Introduzca datos de bodega', bg='LightGreen').pack()
    Label(ventana_frame, text="").pack()

    etiqueta_nombrebodega = Label(ventana_frame, text='Nombre de bodega *')
    etiqueta_nombrebodega.pack()
    entrada_nombrebodega = Entry(ventana_frame, textvariable=nombrebodega)
    entrada_nombrebodega.pack()

    etiqueta_ubicacionbodega = Label(ventana_frame, text ='Ubicacion de la bodega *')
    etiqueta_ubicacionbodega.pack()
    entrada_ubicacionbodega = Entry(ventana_frame, textvariable=ubicacionbodega)
    entrada_ubicacionbodega.pack()

    Label(ventana_frame, text="").pack()

    Button(ventana_frame, text="Registrar bodega", width=20, height=1, bg="LightGreen", command=registro_bodega).pack()

    ventana_frame.pack(fill='both', expand=1)

def frame_registrarproducto():


    global info_descripcion
    global entry_tipo
    global entry_cat

    info_descripcion = StringVar()
    global ventana_frame
    # Cerrar frame anterior 
    cerrar_frame()
    tipoproducto_lb = TipoproductoListBox()

    categorias_lb = CategoriasListBox()

    ventana_frame = Frame(ventana_admin, width=400, height=400)


    Label(ventana_frame, text="Introduzca los datos del producto", bg="LightGreen").pack()
    Label(ventana_frame, text="").pack()

    etiqueta_descripcion = Label(ventana_frame,text='Descripcion *')
    etiqueta_descripcion.pack()
    entrada_descripcion = Entry(ventana_frame, textvariable=info_descripcion)
    entrada_descripcion.pack()

    Label(ventana_frame, text="").pack()

    etiqueta_categoria = Label(ventana_frame,text='Categoria *')
    etiqueta_categoria.pack()

    categorias_s = categorias_lb.obtener_categorias_seleccionadas()
    
    
    entry_cat = Entry(ventana_frame,textvariable=categorias_s)
    entry_cat.pack()


    Button(ventana_frame, text='Categorias', width=20,height=1,bg='LightGreen', command=categorias_lb.mostrar_ventana).pack()

    Label(ventana_frame, text="").pack()

    tipos_seleccionados = tipoproducto_lb.obtener_tipos_seleccionados()


    etiqueta_tipoproducto = Label(ventana_frame,text='Tipo de producto *')
    etiqueta_tipoproducto.pack()

    
    
    entry_tipo = Entry(ventana_frame,textvariable=tipos_seleccionados)
    entry_tipo.pack()

    Button(ventana_frame,text='Tipos de producto', width=20,height=1,bg='LightGreen', command=tipoproducto_lb.mostrar_ventana).pack()


    Label(ventana_frame, text="").pack()
    
    btnregistrar = Button(ventana_frame, text="Registrar producto", width=20, height=1, bg="LightGreen", command=registro_productos)
    btnregistrar.pack()

    ventana_frame.pack(fill='both', expand=1)

def frame_registrartipoproducto():
    global nombre_tipo

    nombre_tipo = StringVar()
    global ventana_frame
    # Cerrar frame anterior 
    cerrar_frame()

    ventana_frame = Frame(ventana_admin, width=400, height=400)

    Label(ventana_frame, text="Introduzca tipo", bg="LightGreen").pack()
    Label(ventana_frame, text="").pack()

    etiqueta_tipo = Label(ventana_frame,text='Tipo de producto *')
    etiqueta_tipo.pack()
    entrada_tipo = Entry(ventana_frame, textvariable=nombre_tipo)
    entrada_tipo.pack()

    Label(ventana_frame, text="").pack()
    Button(ventana_frame, text="Registrar tipo de producto", width=20, height=1, bg="LightGreen", command=registro_tipoproducto).pack()

    ventana_frame.pack(fill='both', expand=1)

def frame_registrarautor():
    global autor
    global entrada_autor
 
    global ventana_frame
    autor = StringVar()

    # Cerrar frame anterior
    cerrar_frame()

    ventana_frame = Frame(ventana_admin, width=400, height=400)

    Label(ventana_frame, text='Introduzca autor', bg='LightGreen').pack()
    Label(ventana_frame, text="").pack()

    etiqueta_autor = Label(ventana_frame, text='Nombre del autor *')
    etiqueta_autor.pack()
    entrada_autor = Entry(ventana_frame, textvariable=autor)
    entrada_autor.pack()

    Button(ventana_frame, text="Registrarse", width=10, height=1, bg="LightGreen", command=registro_autor).pack()

    ventana_frame.pack(fill='both', expand=1)


def frame_registrarcategoria():
    global nombre_categoria

    nombre_categoria = StringVar()
    global ventana_frame
    # Cerrar frame anterior 
    cerrar_frame()

    ventana_frame = Frame(ventana_admin, width=400, height=400)

    Label(ventana_frame, text="Introduzca categoria", bg="LightGreen").pack()
    Label(ventana_frame, text="").pack()

    etiqueta_categoria = Label(ventana_frame,text='Categoria *')
    etiqueta_categoria.pack()
    entrada_categoria = Entry(ventana_frame, textvariable=nombre_categoria)
    entrada_categoria.pack()

    Label(ventana_frame, text="").pack()
    Button(ventana_frame, text="Registrar categoria", width=15, height=1, bg="LightGreen", command=registro_categoria).pack()

    ventana_frame.pack(fill='both', expand=1)

def frame_registrarusuario():
    global ventana_frame
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

def frame_asignarautor():
    global productoid
    global autorid 
    global ventana_frame
    global entry_producto
    global autores

    autor_lb = ListboxAutor()
    producto_lb = ListboxProductos()

    productoid = StringVar()
    autorid = StringVar()

    #Cerrar frame anterior
    cerrar_frame()

    ventana_frame = Frame(ventana_admin, width=400, height=400)


    Label(ventana_frame, text="Introduzca datos", bg="LightGreen").pack()
    Label(ventana_frame, text="").pack()

    etiqueta_productos = Label(ventana_frame,text='Productos *')
    etiqueta_productos.pack()

    productos = producto_lb.obtener_tipos_seleccionados()

    entry_producto = Entry(ventana_frame,textvariable=productos,state='readonly')
    entry_producto.pack()
    Button(ventana_frame,text='Productos', width=20,height=1,bg='LightGreen', command=producto_lb.mostrar_ventana).pack()

    Label(ventana_frame, text="").pack()

    etiqueta_autores = Label(ventana_frame,text='Autores *')
    etiqueta_autores.pack()

    autores = autor_lb.obtener_tipos_seleccionados()

    autor_lb.mostrar_ventana(ventana_frame)

    # entry_autor = Entry(ventana_frame,textvariable=autores)
    # entry_autor.pack()
    # Button(ventana_frame,text='Autores', width=20,height=1,bg='LightGreen', command=autor_lb.mostrar_ventana).pack()

    Label(ventana_frame, text="").pack()

    Button(ventana_frame, text='Asignar Autor', width=20, height=1, bg='LightGreen',command=asignar_autor).pack()
    ventana_frame.pack(fill='both', expand=1)


def frame_asignarbodega():
    global ventana_frame
    global bodegas
    global usuarios
    bodega_lb = ListboxBodega()
    usuario_lb = ListboxUsuario()

    # Cerrar frame anterior
    cerrar_frame()

    ventana_frame = tk.Frame(ventana_admin)

    etiqueta_seleccione_datos = tk.Label(ventana_frame, text="Seleccione datos", bg="LightGreen")
    etiqueta_seleccione_datos.grid(row=0, column=0, columnspan=2, pady=10)

    bodega_lb.mostrar_ventana(ventana_frame)
    bodegas = bodega_lb.obtener_bodegas_seleccionadas()

    usuario_lb.mostrar_ventana(ventana_frame)
    usuarios = usuario_lb.obtener_usuario_seleccionados()

    boton_asignar_usuarios = tk.Button(ventana_frame, text='Asignar Usuarios', width=20, height=1, bg='LightGreen',command=asignar_bodega)
                                      
    boton_asignar_usuarios.grid(row=8, column=0, columnspan=2, pady=10)

    ventana_frame.pack()


def frame_asignar_copia():
    global ventana_frame
    global bodegascopia
    global productoscopia
    global nombre_copia
    global descripcion_copia
    global cantidad_copia

    cantidad_copia = tk.IntVar()
    nombre_copia = tk.StringVar()
    descripcion_copia = tk.StringVar()

    producto_lb = ListboxProductos()
    bodega_lb = ListboxBodega()
    # Cerrar frame anterior
    cerrar_frame()

    ventana_frame = tk.Frame(ventana_admin)

    etiqueta_seleccione_datos = tk.Label(ventana_frame, text="Ingrese datos", bg="LightGreen")
    etiqueta_seleccione_datos.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    etiqueta_nombrecopia = tk.Label(ventana_frame, text="Nombre: *" )
    etiqueta_nombrecopia.grid(row=1, column=0, sticky="e", padx=10, pady=5)
    entrada_nombrecopia = tk.Entry(ventana_frame, textvariable=nombre_copia, )
    entrada_nombrecopia.grid(row=1, column=1, padx=10, pady=5)

    etiqueta_descripcioncopia = tk.Label(ventana_frame, text="Descripción: *" )
    etiqueta_descripcioncopia.grid(row=2, column=0, sticky="e", padx=10, pady=5)
    entrada_descripcioncopia = tk.Entry(ventana_frame, textvariable=descripcion_copia, )
    entrada_descripcioncopia.grid(row=2, column=1, padx=10, pady=5)

    etiqueta_cantidadcopia = tk.Label(ventana_frame, text="Cantidad: *")
    etiqueta_cantidadcopia.grid(row=3, column=0, sticky="e", padx=10, pady=5)
    entrada_cantidadcopia = tk.Entry(ventana_frame, textvariable=cantidad_copia )
    entrada_cantidadcopia.grid(row=3, column=1, padx=10, pady=5)

    productoscopia = producto_lb.obtener_tipos_seleccionados()
    etiqueta_productocopia = tk.Label(ventana_frame, text="Producto: *" )
    etiqueta_productocopia.grid(row=4, column=0, sticky="e", padx=10, pady=5)
    entry_productocopia = tk.Entry(ventana_frame, textvariable=productoscopia, state='readonly' )
    entry_productocopia.grid(row=4, column=1, padx=10, pady=5)
    tk.Button(ventana_frame, text='Seleccionar', width=20, height=1, bg='LightGreen', command=producto_lb.mostrar_ventana, ).grid(row=4, column=2, padx=10, pady=5)

    bodega_frame = tk.Frame(ventana_frame)
    bodega_lb.mostrar_ventana(bodega_frame)
    bodega_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    bodegascopia = bodega_lb.obtener_bodegas_seleccionadas()

    boton_asignar_copia = tk.Button(ventana_frame, text='Asignar Copias', width=20, height=1, bg='LightGreen',command=asignar_copia)
    boton_asignar_copia.grid(row=6, column=0, columnspan=2,padx=10,pady=10)
                                      

    ventana_frame.pack()

def frame_realizarmov():
    dao = DAO()
    #verifica usuario se saca el usuario

    global copiamovimiento
    global ventana_frame
    global cal
    global entrada_bodega
    global salida_bodega
    
    copias_lb = ListboxCopia()


    # Cerrar frame anterior
    cerrar_frame()

    ventana_frame = tk.Frame(ventana_bodeguero)

    etiqueta_seleccione_datos = tk.Label(ventana_frame, text="Ingrese datos", bg="LightGreen")
    etiqueta_seleccione_datos.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    datos_frame = tk.Frame(ventana_frame)
    datos_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)  # Posición del marco

    etiqueta_fechamovimiento = tk.Label(datos_frame, text="Fecha: *")
    etiqueta_fechamovimiento.grid(row=0, column=0, padx=10, pady=5)

    cal = DateEntry(datos_frame, width=12, background='LightGreen', foreground='white', borderwidth=2)
    cal.grid(row=1, column=0, padx=10, pady=5)

   

    bodegas = dao.obtener_bodegas()

    bodega_frame = tk.Frame(ventana_frame)

    # entrada_rol = Combobox(ventana_frame, values=roles, state='readonly')
    # entrada_rol.pack()

    etiqueta_bodegasalida = tk.Label(bodega_frame,text='Bodega salida')
    etiqueta_bodegasalida.grid(row=2,column=0,padx=10,pady=5)
    salida_bodega = Combobox(bodega_frame, values = bodegas, state='readonly')
    salida_bodega.grid(row=3,column=0,columnspan=2,padx=10,pady=5)

    etiqueta_bodegaentrada = tk.Label(bodega_frame,text='Bodega entrada')
    etiqueta_bodegaentrada.grid(row=4,column=0,padx=10,pady=5)
    entrada_bodega= Combobox(bodega_frame,values=bodegas,state='readonly')
    entrada_bodega.grid(row=5,column=0,columnspan=2,padx=10,pady=5)


    bodega_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=5)


    copias_frame = tk.Frame(ventana_frame)

    etiqueta_copias = tk.Label(copias_frame,text='Seleccione producto')
    etiqueta_copias.grid(row=0,column=0,columnspan=2,padx=10,pady=5)

    copias_lb.mostrar_ventana(copias_frame)

    copiamovimiento = copias_lb.obtener_copias_seleccionadas()
    copias_frame.grid(row=4,column=0,columnspan=2,padx=10,pady=5)
    # productos_frame = tk.Frame(ventana_frame)

    # productos= productos_lb.obtener_tipos_seleccionados()

    # productos_lb.mostrar_ventana(productos_frame)


    # productos_frame.grid(row=4,column=0,columnspan=2,padx=10,pady=5)

    btn = tk.Button(ventana_frame,text='Realizar movimiento',width=20, height=1, bg='LightGreen',command=realizarmovimiento)
    btn.grid(row=7,column=0,columnspan=2,padx=10,pady=10)
    ventana_frame.pack()

def mostrar_menuadmin():
    ventana_principal.destroy()
    global ventana_admin
    ventana_admin = Tk()
    ventana_admin.title("Menú Admin")

    menu_admin = Menu(ventana_admin)
    opciones_registrar = Menu(menu_admin)
    opciones_registrar.add_command(label='Registrar usuario', command=frame_registrarusuario)
    opciones_registrar.add_command(label='Registrar producto', command=frame_registrarproducto)
    opciones_registrar.add_command(label='Registrar categoría', command=frame_registrarcategoria)
    opciones_registrar.add_command(label='Registrar autor', command=frame_registrarautor)
    opciones_registrar.add_command(label='Registrar tipo de producto', command=frame_registrartipoproducto)
    opciones_registrar.add_command(label='Registrar bodega', command=frame_registrarbodega)

    opciones_eliminar = Menu(menu_admin)
    opciones_eliminar.add_command(label='Eliminar productos')
    opciones_eliminar.add_command(label='Eliminar editorial')
    opciones_eliminar.add_command(label='Eliminar bodega')

    opciones_asignar = Menu(menu_admin)
    opciones_asignar.add_command(label='Asignar Autor',command=frame_asignarautor)
    opciones_asignar.add_command(label='Asignar Bodega', command=frame_asignarbodega)
    opciones_asignar.add_command(label='Asignar Copia', command=frame_asignar_copia)


    
    menu_admin.add_cascade(label='Registrar', menu=opciones_registrar)
    menu_admin.add_cascade(label='Eliminar', menu=opciones_eliminar)
    menu_admin.add_cascade(label='Asignar', menu =opciones_asignar)

    ventana_admin.config(menu=menu_admin)

    ventana_admin.mainloop()

def mostrar_menubodeguero():
    ventana_principal.destroy()
    global ventana_bodeguero
    ventana_bodeguero = Tk()
    ventana_bodeguero.title('Menú Bodeguero')

    menu_bodeguero = Menu(ventana_bodeguero)
    opcion_realizarmov = Menu(menu_bodeguero)
    opcion_realizarmov.add_command(label='Realizar movimiento',command=frame_realizarmov)

    opcion_gestionar= Menu(menu_bodeguero)
    opcion_gestionar.add_command(label='Gestionar bodegas',command="")

    menu_bodeguero.add_cascade(label='Realizar movimiento',menu=opcion_realizarmov)
    menu_bodeguero.add_cascade(label='Gestionar bodegas',menu=opcion_gestionar)


    ventana_bodeguero.config(menu=menu_bodeguero)
    ventana_bodeguero.mainloop()
    
global verifica_usuario

ventana_principal = Tk()
ventana_principal.geometry("300x250")
ventana_principal.title("Login con tkinter")
Label(text="").pack()


verifica_usuario = StringVar()
verifica_clave = StringVar()


Label(ventana_principal, text="Nombre de usuario * ").pack()

entrada_login_usuario = Entry(ventana_principal, textvariable=verifica_usuario)
entrada_login_usuario.pack()

Label(ventana_principal, text="").pack()
Label(ventana_principal, text="Contraseña * ").pack()

entrada_login_clave = Entry(ventana_principal, textvariable=verifica_clave, show='*')
entrada_login_clave.pack()

Label(ventana_principal, text="").pack()
Button(ventana_principal, text="Acceder", width=10, height=1, command=verifica_login).pack()

ventana_principal.mainloop()