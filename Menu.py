from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tkinter.font as tkFont
import json
from PIL import ImageTk, Image

nuevoJuego = {
        "Matriz": {"Columnas": None,"Filas": None, "matrizJ1": [], "matrizJ2": []},
        "NombrePartida": None,
        "Jugador 1": {
            "Nombre": None,
            "Nickname": None,
            "Puntaje": 0
        },
        
        "Jugador 2": {
            "Nombre":  None,
            "Nickname": None,
            "Puntaje": 0
        },
        
        "BarcosJ1": {
            "Destructor1J1": {"vida": True, "x1": None, "y1": None ,"orientacion": None} ,
            "Destructor2J1": {"vida": True, "x1": None, "y1": None ,"orientacion": None} ,
            "Destructor3J1": {"vida": True, "x1": None, "y1": None ,"orientacion": None} ,
            "Destructor4J1": {"vida": True, "x1": None, "y1": None ,"orientacion": None} ,
            "Destructor5J1": {"vida": True, "x1": None, "y1": None ,"orientacion": None} ,
            "Destructor6J1": {"vida": True, "x1": None, "y1": None ,"orientacion": None} ,

            "Crucero1J1":  {"vida": True, "x1": None, "y1": None, "x2": None , "y2": None, "orientacion": None},
            "Crucero2J1":  {"vida": True, "x1": None, "y1": None, "x2": None , "y2": None, "orientacion": None},
            "Crucero3J1":  {"vida": True, "x1": None, "y1": None, "x2": None , "y2": None, "orientacion": None},
            "Crucero4J1":  {"vida": True, "x1": None, "y1": None, "x2": None , "y2": None, "orientacion": None},

            "Acorazado1J1": {"vida": True, "x1": None, "y1": None,"x2": None, "y2": None,"x3": None, "y3": None, "orientacion": None},
            "Acorazado2J1": {"vida": True, "x1": None, "y1": None,"x2": None, "y2": None,"x3": None, "y3": None, "orientacion": None}
            },

        "BarcosJ2": {                   
            "Destructor1J2": {"vida": True, "x1": None, "y1": None ,"orientacion": None} ,
            "Destructor2J2": {"vida": True, "x1": None, "y1": None ,"orientacion": None} ,
            "Destructor3J2": {"vida": True, "x1": None, "y1": None ,"orientacion": None} ,
            "Destructor4J2": {"vida": True, "x1": None, "y1": None ,"orientacion": None} ,
            "Destructor5J2": {"vida": True, "x1": None, "y1": None ,"orientacion": None} ,
            "Destructor6J2": {"vida": True, "x1": None, "y1": None ,"orientacion": None} ,

            "Crucero1J2": {"vida": True, "x1": None, "y1": None,"x2": None, "y2": None, "orientacion": None},
            "Crucero2J2": {"vida": True, "x1": None, "y1": None,"x2": None, "y2": None, "orientacion": None},
            "Crucero3J2": {"vida": True, "x1": None, "y1": None,"x2": None, "y2": None, "orientacion": None},
            "Crucero4J2": {"vida": True, "x1": None, "y1": None,"x2": None, "y2": None, "orientacion": None},

            "Acorazado1J2": {"vida": True, "x1": None, "y1": None,"x2": None, "y2": None, "x3": None, "y3": None, "orientacion": None},
            "Acorazado2J2": {"vida": True, "x1": None, "y1": None,"x2": None, "y2": None, "x3": None, "y3": None, "orientacion": None},
            }
    }

menu = Tk()
style = ttk.Style() 
style.configure('C.TButton', font=("Bauhaus 93", 18))
style.configure('C.TButton', relief="ridge")
style.configure('C.TButton', width=3)
style.configure('C.TButton', bd=1)
fontStyle = tkFont.Font(family="Lucida Grande", size=40)
matriz=[]
resultadoX=0
resultadoY=0

def crearPartida():
    global nuevoJuego

    ventana=Toplevel()
    ventana.title("Datos de partida")
    ventana.geometry("410x250+380+280")

    partidaLabel= Label(ventana, text="Inserte el nombre de la partida:")
    partidaLabel.place(x=1,y=1)
    nombrePartidaE= Entry(ventana)
    nombrePartidaE.place(x=270,y=1)

    jugador1Label= Label(ventana, text="Inserte el nombre del primer jugador:")
    jugador1Label.place(x=1,y=30)
    nombreJugador1E= Entry(ventana)
    nombreJugador1E.place(x=270,y=30)

    nickname1Label= Label(ventana, text="Inserte el nombre del primer jugador:")
    nickname1Label.place(x=1,y=60)
    nickName1E= Entry(ventana)
    nickName1E.place(x=270,y=60)  

    jugador2Label= Label(ventana, text="Inserte el nombre del segundo jugador:")
    jugador2Label.place(x=1,y=90)
    nombreJugador2E= Entry(ventana)
    nombreJugador2E.place(x=270,y=90)

    nickname2Label= Label(ventana, text="Inserte el nombre del segundo jugador:")
    nickname2Label.place(x=1,y=120)
    nickName2E= Entry(ventana)
    nickName2E.place(x=270,y=120)

    columnaLabel= Label(ventana, text="Columnas:")
    columnaLabel.place(x=1,y=150)
    seleccionColumnaE= Spinbox(ventana, from_=20, to=40, increment=2)
    seleccionColumnaE.place(x=270,y=150)

    filaLabel= Label(ventana, text="Fila:")
    filaLabel.place(x=1,y=180)
    seleccionFilaE= Spinbox(ventana, from_=10, to=40)
    seleccionFilaE.place(x=270, y=180)

    botonEmpezar=Button(ventana, text="Empezar",command=lambda:validarDatos(nombrePartidaE.get(),nombreJugador1E.get(),nickName1E.get(),nombreJugador2E.get(),nickName2E.get(),seleccionFilaE.get(),seleccionColumnaE.get(), ventana)
                        and mensaje() and generarMatriz( seleccionColumnaE.get(),seleccionFilaE.get()) and 
                        ubicarDestructor1J1(seleccionColumnaE.get(), seleccionFilaE.get()))
    botonEmpezar.place(x=310, y=210)

def validarDatos(nombrePartida,nombreJugador1,nickname1,nombreJugador2,nickname2,fila,columna,ventana):
    if len(nombrePartida)==0:
        messagebox.showerror("Error", "Verifica que ningun campo este vacio, intenta de nuevo")
        ventana.destroy()
        return False
    if len(nombreJugador1)==0:
        messagebox.showerror("Error", "Verifica que ningun campo este vacio, intenta de nuevo")
        ventana.destroy()
        return False
    if len(nickname1)==0:
        messagebox.showerror("Error", "Verifica que ningun campo este vacio, intenta de nuevo")
        ventana.destroy()
        return False
    if len(nombreJugador2)==0:
        messagebox.showerror("Error", "Verifica que ningun campo este vacio, intenta de nuevo")
        ventana.destroy()
        return False 
    if nombreJugador1==nombreJugador2:
            messagebox.showerror("Error", "El nombre de los jugadores no puede ser igual")
            ventana.destroy()
            return False   
    if len(nickname1)==0:
        messagebox.showerror("Error", "Verifica que ningun campo este vacio, intenta de nuevo")
        ventana.destroy()
        return False
    if len(nickname2)==0:
        messagebox.showerror("Error", "Verifica que ningun campo este vacio, intenta de nuevo")
        ventana.destroy()
        return False
    if nickname1==nickname2:
            messagebox.showerror("Error", "El nickname de los jugadores no puede ser igual")
            ventana.destroy()
            return False
    if not fila.isdigit():
        messagebox.showerror("Error", "El numero de filas debe ser un numero, intenta de nuevo")
        ventana.destroy()
        return False    
    if not columna.isdigit():
        messagebox.showerror("Error", "El numero de columnas debe ser un numero, intenta de nuevo")
        ventana.destroy()
        return False  
    if int(fila) < 10:
        messagebox.showerror("Error", "El numero de filas debe ser mayor o igual a 10, intenta de nuevo")
        ventana.destroy()
        return False
    if int(columna) < 20:    
        messagebox.showerror("Error", "El numero de columnas debe ser mayor o igual a 20, intenta de nuevo")
        ventana.destroy()
        return False    
    actualizarDatos(nombrePartida,nombreJugador1,nickname1,nombreJugador2,nickname2,fila,columna)
    return True

def actualizarDatos(nombrePartida,nombreJugador1,nickname1,nombreJugador2,nickname2,fila,columna):
    global nuevoJuego
    nuevoJuego["NombrePartida"]=nombrePartida
    nuevoJuego["Jugador 1"]["Nombre"]=nombreJugador1
    nuevoJuego["Jugador 1"]["Nickname"]=nickname1
    nuevoJuego["Jugador 2"]["Nombre"]=nombreJugador2
    nuevoJuego["Jugador 2"]["Nickname"]=nickname2
    nuevoJuego["Matriz"]["Columnas"]=columna
    nuevoJuego["Matriz"]["Filas"]=fila
    return True

def guardarDatos(nombrePartida):
    global nuevoJuego
    try:
        with open("partidas.json", "r") as archivoJson:
            datosExistentes = json.load(archivoJson)
    except FileNotFoundError:
        datosExistentes = {}

    datosExistentes[nombrePartida] = nuevoJuego

    with open("partidas.json", "w") as archivoJson:
        json.dump(datosExistentes, archivoJson, indent=4)

def cargarPartidas():
    listaPartidas=[]
    try:
        with open("partidas.json", "r") as archivoJson:
            partidasGuardadas = json.load(archivoJson)
    except FileNotFoundError:
        with open("partidas.json", "w") as archivoJson:
            json.dump({}, archivoJson)
        partidasGuardadas = {}

    for p in partidasGuardadas.keys():
        listaPartidas.append(p)

    ventana= Toplevel()
    ventana.title("Partidas guardadas")
    ventana.geometry("300x100+380+280")
    letrero= Label(ventana, text="Seleccione la partida que desees jugar:")
    letrero.place(x=1, y=1)
    seleccionPartida= ttk.Combobox(ventana, values=listaPartidas)
    seleccionPartida.place(x=50, y=30)
    botonGuardar=Button(ventana, text="Seleccionar",command= ventana.destroy)
    botonGuardar.place(x=220, y=70)

def borrarPartidas():
    with open("partidas.json", "r") as archivoJson:
        partidasGuardadas = json.load(archivoJson)
    partidasGuardadas.clear()
    with open("partidas.json", "w") as archivoJson:
        json.dump(partidasGuardadas, archivoJson, indent=4)

menu.attributes('-fullscreen', True)
menu.configure(bg="Yellow")
menu.title("Battleship")

titulo= Label(menu, text="Battleship", font=fontStyle)
titulo.place(x=660,y=1)

boton1=ttk.Button(menu, text= "Crear partida", command=crearPartida, style='C.TButton')
boton1.place(x=80 , y=220, width=200, height=130)

boton2=ttk.Button(menu, text= "Cargar partida", command= cargarPartidas, style='C.TButton')
boton2.place(x=80 , y=430, width=200, height=130)

boton2=ttk.Button(menu, text= "Borrar partidas", command=borrarPartidas, style='C.TButton')
boton2.place(x=80 , y=640, width=200, height=130)

boton4=ttk.Button(menu, text="Salir", command=menu.destroy, style='C.TButton')
boton4.place(x=1330 , y=30, width=120, height=80)

punto= Label(menu, text="#")
punto.place(x=1525 , y=850)

def mensaje():
    messagebox.showinfo("Battleship", "Tus datos han sido ingresados correctamente")
    return True 

def generarMatriz(x,y):
    x=int(x)
    y=int(y)
    global nuevoJuego
    nuevoJuego["Matriz"]["matrizJ1"]=[[0 for c in range(x//2)] for f in range(y)]
    nuevoJuego["Matriz"]["matrizJ2"]=[[0 for c in range(x//2)] for f in range(y)]
    return True

def cambiarCursor(event):
    menu.config(cursor="hand2")

def restaurarCursor(event):
    menu.config(cursor="")

menu.bind("<Enter>", cambiarCursor)

menu.bind("<Leave>", restaurarCursor)

def accion(x,y):
    #print (f"x={x},y={y}")
    global resultadoX
    global resultadoY
    resultadoX=x
    resultadoY=y  


def configurarBoton(btn, num):
    if num == 0:
        btn.configure(bg="blue")
    elif num == 1:
        btn.configure(image=imagen1)
    elif num == 2:
        btn.configure(image=imagen2)
    elif num == 3:
        btn.configure(image=imagen3)
    elif num == 4:
        btn.configure(image=imagen4)
    elif num == 5:
        btn.configure(image=imagen5)
    elif num == 6:
        btn.configure(image=imagen6)
    elif num == 7:
        btn.configure(image=imagen7)
    elif num == 8:
        btn.configure(image=imagen8)
    elif num == 9:
        btn.configure(image=imagen9)
    elif num == 10:
        btn.configure(image=imagen10)
    elif num == 11:
        btn.configure(image=imagen11)  
    elif num == 12:
        btn.configure(image=imagen12)
    elif num == 13:
        btn.configure(image=imagen13)
    elif num == 14:
        btn.configure(image=imagen14)
    elif num == 15:
        btn.configure(image=imagen15)
    elif num == 16:
        btn.configure(image=imagen16)
    elif num == 17:
        btn.configure(image=imagen17)
    elif num == 18:
        btn.configure(image=imagen18)
    elif num == 19:
        btn.configure(image=imagen19)
    elif num == 20:
        btn.configure(image=imagen20)
    elif num == 21:
        btn.configure(image=imagen21)
    elif num == 22:
        btn.configure(image=imagen22)
    elif num == 23:
        btn.configure(image=imagen23)
    elif num == 24:
        btn.configure(image=imagen24)


def imprimirMatrizJ1(x,y,tablero):
    matrizBotonesJ1=[[Button(tablero, command=lambda x=c,y=f:accion(x,y)) 
            for c in range(x//2)] for f in range(y)]
    global nuevoJuego
    posicionXmatriz=10
    posicionYmatriz=200
    for fila_botones,fila in zip(matrizBotonesJ1, nuevoJuego["Matriz"]["matrizJ1"]):
        posicionXmatriz=10
        for btn, num in zip(fila_botones,fila):
            configurarBoton(btn, num)
            btn.place(x=posicionXmatriz,y=posicionYmatriz,height=30,width=30)
            posicionXmatriz+=32
            
        posicionYmatriz+=36

    
    matrizReferencia=[[Button(tablero,bg="gray") 
            for c in range(x//2)] for f in range(y)]
    
    posicionXmatrizCopia=posicionXmatriz+10
    posicionYmatrizCopia=200

    for fila_botones in matrizReferencia:
        posicionXmatrizCopia=posicionXmatriz+10
        for btn in fila_botones:
            btn.place(x=posicionXmatrizCopia,y=posicionYmatrizCopia,height=30,width=30)
            posicionXmatrizCopia+=32
        posicionYmatrizCopia+=36

def imprimirMatrizJ2(x,y,tablero):
    matrizReferencia=[[Button(tablero,bg="gray") 
            for c in range(x//2)] for f in range(y)]
    
    posicionXmatrizCopia=10
    posicionYmatrizCopia=200
    for fila_botones in matrizReferencia:
        posicionXmatrizCopia=10
        for btn in fila_botones:
            btn.place(x=posicionXmatrizCopia,y=posicionYmatrizCopia,height=30,width=30)
            posicionXmatrizCopia+=32
        posicionYmatrizCopia+=36

    matrizBotonesJ2=[[Button(tablero, command=lambda x=co,y=fi:accion(x,y)) 
            for co in range(x//2)] for fi in range(y)]
    global nuevoJuego

    posicionXmatriz=posicionXmatrizCopia+10
    posicionYmatriz=200
    for fila_botones,fila in zip(matrizBotonesJ2, nuevoJuego["Matriz"]["matrizJ2"]):
        posicionXmatriz=posicionXmatrizCopia+10
        for btn, num in zip(fila_botones,fila):
            configurarBoton(btn, num)
            btn.place(x=posicionXmatriz,y=posicionYmatriz,height=30,width=30)
            posicionXmatriz+=32
        posicionYmatriz+=36

def ubicarDestructor1J1(x,y):
    x=int(x)
    y=int(y)
    global matriz
    tablero=tk.Toplevel()
    tablero.title("Tablero")
    tablero.attributes("-fullscreen", True)

    tableroLabel= Label(tablero, text="Inserte la ubicacion del barco:")
    tableroLabel.place(x=1,y=10)

    orientacion= tk.IntVar()

    botonGuardarPosicion=Button(tablero, text="Guardar",command= lambda: validarUbicacionDestructorJ1(resultadoX,resultadoY,orientacion.get()) and guardarDestructor1J1(resultadoX,resultadoY,orientacion.get (),x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    orientacionLabel= Label(tablero, text="Orientacion del barco:")
    orientacionLabel.place(x=500,y=40)

    orientacionIzquierda=ttk.Radiobutton(tablero, text="Derecha", value= 1, variable=orientacion)
    orientacionIzquierda.place(x=600, y=60)
    orientacionDerecha=ttk.Radiobutton(tablero, text="Arriba", value=2, variable=orientacion)
    orientacionDerecha.place(x=800, y=60)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=900, y=60)
    
    imprimirMatrizJ1(x,y,tablero) 

def guardarDestructor1J1(x,y,orientacion,co,fi):
    global nuevoJuego
    nuevoJuego["BarcosJ1"]["Destructor1J1"]["x1"]=x
    nuevoJuego["BarcosJ1"]["Destructor1J1"]["y1"]=y
    nuevoJuego["BarcosJ1"]["Destructor1J1"]["vida"]=True
    nuevoJuego["BarcosJ1"]["Destructor1J1"]["orientacion"]=orientacion

    if orientacion==1:
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=1

    elif orientacion==2:
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=2

    elif orientacion==3:
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=3

    elif orientacion==4:
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=4
    
    ubicarDestructor2J1(co,fi)
    
    return True

def ubicarDestructor2J1(x,y):
    x=int(x)
    y=int(y)
    global matriz
    tablero=tk.Toplevel()
    tablero.title("Tablero")
    tablero.attributes("-fullscreen", True)

    tableroLabel= Label(tablero, text="Inserte la ubicacion del barco:")
    tableroLabel.place(x=1,y=10)

    orientacion= tk.IntVar()

    botonGuardarPosicion=Button(tablero, text="Guardar",command= lambda:  validarUbicacionDestructorJ1(resultadoX,resultadoY,orientacion.get()) and guardarDestructor2J1(resultadoX,resultadoY,orientacion.get (),x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    orientacionLabel= Label(tablero, text="Orientacion del barco:")
    orientacionLabel.place(x=500,y=40)

    orientacionIzquierda=ttk.Radiobutton(tablero, text="Derecha", value= 1, variable=orientacion)
    orientacionIzquierda.place(x=600, y=60)
    orientacionDerecha=ttk.Radiobutton(tablero, text="Arriba", value=2, variable=orientacion)
    orientacionDerecha.place(x=800, y=60)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=900, y=60)

    imprimirMatrizJ1(x,y,tablero)

def guardarDestructor2J1(x,y,orientacion,co,fi):
    global nuevoJuego
    nuevoJuego["BarcosJ1"]["Destructor2J1"]["x1"]=x
    nuevoJuego["BarcosJ1"]["Destructor2J1"]["y1"]=y
    nuevoJuego["BarcosJ1"]["Destructor2J1"]["vida"]=True
    nuevoJuego["BarcosJ1"]["Destructor2J1"]["orientacion"]=orientacion
    
    if orientacion==1:
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=1

    elif orientacion==2:
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=2

    elif orientacion==3:
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=3

    elif orientacion==4:
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=4
    
    
    ubicarDestructor3J1(co,fi)
      
    return True

def ubicarDestructor3J1(x,y):
    x=int(x)
    y=int(y)
    global matriz
    tablero=tk.Toplevel()
    tablero.title("Tablero")
    tablero.attributes("-fullscreen", True)

    tableroLabel= Label(tablero, text="Inserte la ubicacion del barco:")
    tableroLabel.place(x=1,y=10)

    orientacion= tk.IntVar()

    botonGuardarPosicion=Button(tablero, text="Guardar",command= lambda: validarUbicacionDestructorJ1(resultadoX,resultadoY,orientacion.get()) and guardarDestructor3J1(resultadoX,resultadoY,orientacion.get(),x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    orientacionLabel= Label(tablero, text="Orientacion del barco:")
    orientacionLabel.place(x=500,y=40)

    orientacionIzquierda=ttk.Radiobutton(tablero, text="Derecha", value= 1, variable=orientacion)
    orientacionIzquierda.place(x=600, y=60)
    orientacionDerecha=ttk.Radiobutton(tablero, text="Arriba", value=2, variable=orientacion)
    orientacionDerecha.place(x=800, y=60)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=900, y=60)

    imprimirMatrizJ1(x,y,tablero)

def guardarDestructor3J1(x,y,orientacion,co,fi):
    global nuevoJuego
    nuevoJuego["BarcosJ1"]["Destructor3J1"]["x1"]=x
    nuevoJuego["BarcosJ1"]["Destructor3J1"]["y1"]=y
    nuevoJuego["BarcosJ1"]["Destructor3J1"]["vida"]=True
    nuevoJuego["BarcosJ1"]["Destructor3J1"]["orientacion"]=orientacion
    
    if orientacion==1:
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=1

    elif orientacion==2:
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=2

    elif orientacion==3:
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=3

    elif orientacion==4:
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=4

    ubicarDestructor4J1(co,fi)
    
    return True

def ubicarDestructor4J1(x,y):
    x=int(x)
    y=int(y)
    global matriz
    tablero=tk.Toplevel()
    tablero.title("Tablero")
    tablero.attributes("-fullscreen", True)

    tableroLabel= Label(tablero, text="Inserte la ubicacion del barco:")
    tableroLabel.place(x=1,y=10)

    orientacion= tk.IntVar()

    botonGuardarPosicion=Button(tablero, text="Guardar",command= lambda:  validarUbicacionDestructorJ1(resultadoX,resultadoY,orientacion.get()) and guardarDestructor4J1(resultadoX,resultadoY,orientacion.get (),x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    orientacionLabel= Label(tablero, text="Orientacion del barco:")
    orientacionLabel.place(x=500,y=40)

    orientacionIzquierda=ttk.Radiobutton(tablero, text="Derecha", value= 1, variable=orientacion)
    orientacionIzquierda.place(x=600, y=60)
    orientacionDerecha=ttk.Radiobutton(tablero, text="Arriba", value=2, variable=orientacion)
    orientacionDerecha.place(x=800, y=60)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=900, y=60)

    imprimirMatrizJ1(x,y,tablero)

def guardarDestructor4J1(x,y,orientacion,co,fi):
    global nuevoJuego
    nuevoJuego["BarcosJ1"]["Destructor4J1"]["x1"]=x
    nuevoJuego["BarcosJ1"]["Destructor4J1"]["y1"]=y
    nuevoJuego["BarcosJ1"]["Destructor4J1"]["vida"]=True
    nuevoJuego["BarcosJ1"]["Destructor4J1"]["orientacion"]=orientacion
    
    if orientacion==1:
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=1

    elif orientacion==2:
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=2

    elif orientacion==3:
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=3

    elif orientacion==4:
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=4

    ubicarDestructor5J1(co,fi)
    return True

def ubicarDestructor5J1(x,y):
    x=int(x)
    y=int(y)
    global matriz
    tablero=tk.Toplevel()
    tablero.title("Tablero")
    tablero.attributes("-fullscreen", True)

    tableroLabel= Label(tablero, text="Inserte la ubicacion del barco:")
    tableroLabel.place(x=1,y=10)

    orientacion= tk.IntVar()

    botonGuardarPosicion=Button(tablero, text="Guardar",command= lambda:  validarUbicacionDestructorJ1(resultadoX,resultadoY,orientacion.get()) and guardarDestructor5J1(resultadoX,resultadoY,orientacion.get (),x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    orientacionLabel= Label(tablero, text="Orientacion del barco:")
    orientacionLabel.place(x=500,y=40)    

    orientacionIzquierda=ttk.Radiobutton(tablero, text="Derecha", value= 1, variable=orientacion)
    orientacionIzquierda.place(x=600, y=60)
    orientacionDerecha=ttk.Radiobutton(tablero, text="Arriba", value=2, variable=orientacion)
    orientacionDerecha.place(x=800, y=60)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=900, y=60)

    imprimirMatrizJ1(x,y,tablero)

def guardarDestructor5J1(x,y,orientacion,co,fi):
    global nuevoJuego
    nuevoJuego["BarcosJ1"]["Destructor5J1"]["x1"]=x
    nuevoJuego["BarcosJ1"]["Destructor5J1"]["y1"]=y
    nuevoJuego["BarcosJ1"]["Destructor5J1"]["vida"]=True
    nuevoJuego["BarcosJ1"]["Destructor5J1"]["orientacion"]=orientacion
    
    if orientacion==1:
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=1

    elif orientacion==2:
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=2

    elif orientacion==3:
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=3

    elif orientacion==4:
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=4

    ubicarDestructor6J1(co,fi)
    return True

def ubicarDestructor6J1(x,y):
    x=int(x)
    y=int(y)
    global matriz
    tablero=tk.Toplevel()
    tablero.title("Tablero")
    tablero.attributes("-fullscreen", True)

    tableroLabel= Label(tablero, text="Inserte la ubicacion del barco:")
    tableroLabel.place(x=1,y=10)

    orientacion= tk.IntVar()

    botonGuardarPosicion=Button(tablero, text="Guardar",command= lambda:  validarUbicacionDestructorJ1(resultadoX,resultadoY,orientacion.get()) and guardarDestructor6J1(resultadoX,resultadoY,orientacion.get (),x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    orientacionLabel= Label(tablero, text="Orientacion del barco:")
    orientacionLabel.place(x=500,y=40)

    orientacionIzquierda=ttk.Radiobutton(tablero, text="Derecha", value= 1, variable=orientacion)
    orientacionIzquierda.place(x=600, y=60)
    orientacionDerecha=ttk.Radiobutton(tablero, text="Arriba", value=2, variable=orientacion)
    orientacionDerecha.place(x=800, y=60)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=900, y=60)

    imprimirMatrizJ1(x,y,tablero)

def guardarDestructor6J1(x,y,orientacion,co,fi):
    global nuevoJuego
    nuevoJuego["BarcosJ1"]["Destructor6J1"]["x1"]=x
    nuevoJuego["BarcosJ1"]["Destructor6J1"]["y1"]=y
    nuevoJuego["BarcosJ1"]["Destructor6J1"]["vida"]=True
    nuevoJuego["BarcosJ1"]["Destructor6J1"]["orientacion"]=orientacion
    
    if orientacion==1:
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=1

    elif orientacion==2:
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=2

    elif orientacion==3:
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=3

    elif orientacion==4:
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=4

    ubicarCrucero1J1(co,fi)
    return True

def ubicarCrucero1J1(x,y):
    x=int(x)
    y=int(y)
    global matriz
    tablero=tk.Toplevel()
    tablero.title("Tablero")
    tablero.attributes("-fullscreen", True)

    tableroLabel= Label(tablero, text="Inserte la ubicacion del barco:")
    tableroLabel.place(x=1,y=10)

    orientacion= tk.IntVar()

    botonGuardarPosicion=Button(tablero, text="Guardar",command= lambda: validarUbicacionCruceroJ1(resultadoX,resultadoY,orientacion.get(),x,y) and guardarCrucero1J1(resultadoX,resultadoY,orientacion.get (),x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    orientacionLabel= Label(tablero, text="Orientacion del barco:")
    orientacionLabel.place(x=500,y=40)

    orientacionIzquierda=ttk.Radiobutton(tablero, text="Derecha", value= 1, variable=orientacion)
    orientacionIzquierda.place(x=600, y=60)
    orientacionDerecha=ttk.Radiobutton(tablero, text="Arriba", value=2, variable=orientacion)
    orientacionDerecha.place(x=800, y=60)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=900, y=60)

    matrizBotonesJ1=[[Button(tablero, command=lambda x=c,y=f:accion(x,y)) 
            for c in range(x//2)] for f in range(y)]
    global nuevoJuego
    posicionXmatriz=10
    posicionYmatriz=200
    for fila_botones,fila in zip(matrizBotonesJ1, nuevoJuego["Matriz"]["matrizJ1"]):
        posicionXmatriz=10
        for btn, num in zip(fila_botones,fila):
            configurarBoton(btn, num)
            btn.place(x=posicionXmatriz,y=posicionYmatriz,height=30,width=30)
            posicionXmatriz+=32
            
        posicionYmatriz+=36

    
    imprimirMatrizJ1(x,y,tablero)

def guardarCrucero1J1(x,y,orientacion,co,fi):
    global nuevoJuego
    nuevoJuego["BarcosJ1"]["Crucero1J1"]["x1"]=x
    nuevoJuego["BarcosJ1"]["Crucero1J1"]["y1"]=y

    if orientacion==1:
        nuevoJuego["BarcosJ1"]["Crucero1J1"]["x2"]=x-1
        nuevoJuego["BarcosJ1"]["Crucero1J1"]["y2"]=y
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=5
        nuevoJuego["Matriz"]["matrizJ1"][y][x-1]=9

    elif orientacion==2:
        nuevoJuego["BarcosJ1"]["Crucero1J1"]["x2"]=x+1
        nuevoJuego["BarcosJ1"]["Crucero1J1"]["y2"]=y
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=6
        nuevoJuego["Matriz"]["matrizJ1"][y+1][x]=10

    elif orientacion==3:
        nuevoJuego["BarcosJ1"]["Crucero1J1"]["y2"]=y+1
        nuevoJuego["BarcosJ1"]["Crucero1J1"]["x2"]=x
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=7
        nuevoJuego["Matriz"]["matrizJ1"][y][x+1]=11

    elif orientacion==4:
        nuevoJuego["BarcosJ1"]["Crucero1J1"]["y2"]=y-1
        nuevoJuego["BarcosJ1"]["Crucero1J1"]["x2"]=x
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=8
        nuevoJuego["Matriz"]["matrizJ1"][y-1][x]=12

    nuevoJuego["BarcosJ1"]["Crucero1J1"]["vida"]=True
    nuevoJuego["BarcosJ1"]["Crucero1J1"]["orientacion"]=orientacion
     
    ubicarCrucero2J1(co,fi) 
    return True

def ubicarCrucero2J1(x,y):
    x=int(x)
    y=int(y)
    global matriz
    tablero=tk.Toplevel()
    tablero.title("Tablero")
    tablero.attributes("-fullscreen", True)

    tableroLabel= Label(tablero, text="Inserte la ubicacion del barco:")
    tableroLabel.place(x=1,y=10)

    orientacion= tk.IntVar()

    botonGuardarPosicion=Button(tablero, text="Guardar",command=lambda: validarUbicacionCruceroJ1(resultadoX,resultadoY,orientacion.get(),x,y) and guardarCrucero2J1(resultadoX,resultadoY,orientacion.get (),x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    orientacionLabel= Label(tablero, text="Orientacion del barco:")
    orientacionLabel.place(x=500,y=40)

    orientacionIzquierda=ttk.Radiobutton(tablero, text="Derecha", value= 1, variable=orientacion)
    orientacionIzquierda.place(x=600, y=60)
    orientacionDerecha=ttk.Radiobutton(tablero, text="Arriba", value=2, variable=orientacion)
    orientacionDerecha.place(x=800, y=60)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=900, y=60)

    imprimirMatrizJ1(x,y,tablero)

def guardarCrucero2J1(x,y,orientacion,co,fi):
    global nuevoJuego
    nuevoJuego["BarcosJ1"]["Crucero2J1"]["x1"]=x
    nuevoJuego["BarcosJ1"]["Crucero2J1"]["y1"]=y

    if orientacion==1:
        nuevoJuego["BarcosJ1"]["Crucero2J1"]["x2"]=x-1
        nuevoJuego["BarcosJ1"]["Crucero2J1"]["y2"]=y
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=5
        nuevoJuego["Matriz"]["matrizJ1"][y][x-1]=9

    elif orientacion==2:
        nuevoJuego["BarcosJ1"]["Crucero2J1"]["x2"]=x+1
        nuevoJuego["BarcosJ1"]["Crucero2J1"]["y2"]=y
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=6
        nuevoJuego["Matriz"]["matrizJ1"][y+1][x]=10

    elif orientacion==3:
        nuevoJuego["BarcosJ1"]["Crucero2J1"]["y2"]=y+1
        nuevoJuego["BarcosJ1"]["Crucero2J1"]["x2"]=x
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=7
        nuevoJuego["Matriz"]["matrizJ1"][y][x+1]=11

    elif orientacion==4:
        nuevoJuego["BarcosJ1"]["Crucero2J1"]["y2"]=y-1
        nuevoJuego["BarcosJ1"]["Crucero2J1"]["x2"]=x
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=8 
        nuevoJuego["Matriz"]["matrizJ1"][y-1][x]=12

    nuevoJuego["BarcosJ1"]["Crucero2J1"]["vida"]=True
    nuevoJuego["BarcosJ1"]["Crucero2J1"]["orientacion"]=orientacion

    ubicarCrucero3J1(co,fi) 
    return True

def ubicarCrucero3J1(x,y):
    x=int(x)
    y=int(y)
    global matriz
    tablero=tk.Toplevel()
    tablero.title("Tablero")
    tablero.attributes("-fullscreen", True)

    tableroLabel= Label(tablero, text="Inserte la ubicacion del barco:")
    tableroLabel.place(x=1,y=10)
    
    orientacion= tk.IntVar()

    botonGuardarPosicion=Button(tablero, text="Guardar",command= lambda:validarUbicacionCruceroJ1(resultadoX,resultadoY,orientacion.get(),x,y) and guardarCrucero3J1(resultadoX,resultadoY,orientacion.get (),x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    orientacionLabel= Label(tablero, text="Orientacion del barco:")
    orientacionLabel.place(x=500,y=40)

    orientacionIzquierda=ttk.Radiobutton(tablero, text="Derecha", value= 1, variable=orientacion)
    orientacionIzquierda.place(x=600, y=60)
    orientacionDerecha=ttk.Radiobutton(tablero, text="Arriba", value=2, variable=orientacion)
    orientacionDerecha.place(x=800, y=60)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=900, y=60)

    imprimirMatrizJ1(x,y,tablero)

def guardarCrucero3J1(x,y,orientacion,co,fi):
    global nuevoJuego
    nuevoJuego["BarcosJ1"]["Crucero3J1"]["x1"]=x
    nuevoJuego["BarcosJ1"]["Crucero3J1"]["y1"]=y

    if orientacion==1:
        nuevoJuego["BarcosJ1"]["Crucero3J1"]["x2"]=x-1
        nuevoJuego["BarcosJ1"]["Crucero3J1"]["y2"]=y
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=5
        nuevoJuego["Matriz"]["matrizJ1"][y][x-1]=9

    elif orientacion==2:
        nuevoJuego["BarcosJ1"]["Crucero3J1"]["x2"]=x+1
        nuevoJuego["BarcosJ1"]["Crucero3J1"]["y2"]=y
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=6
        nuevoJuego["Matriz"]["matrizJ1"][y+1][x]=10

    elif orientacion==3:
        nuevoJuego["BarcosJ1"]["Crucero3J1"]["y2"]=y+1
        nuevoJuego["BarcosJ1"]["Crucero3J1"]["x2"]=x
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=7
        nuevoJuego["Matriz"]["matrizJ1"][y][x+1]=11

    elif orientacion==4:
        nuevoJuego["BarcosJ1"]["Crucero3J1"]["y2"]=y-1
        nuevoJuego["BarcosJ1"]["Crucero3J1"]["x2"]=x
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=8
        nuevoJuego["Matriz"]["matrizJ1"][y-1][x]=12

    nuevoJuego["BarcosJ1"]["Crucero3J1"]["vida"]=True
    nuevoJuego["BarcosJ1"]["Crucero3J1"]["orientacion"]=orientacion

    ubicarCrucero4J1(co,fi)
    return True

def ubicarCrucero4J1(x,y):
    x=int(x)
    y=int(y)
    global matriz
    tablero=tk.Toplevel()
    tablero.title("Tablero")
    tablero.attributes("-fullscreen", True)

    tableroLabel= Label(tablero, text="Inserte la ubicacion del barco:")
    tableroLabel.place(x=1,y=10)

    orientacion= tk.IntVar()

    botonGuardarPosicion=Button(tablero, text="Guardar",command= lambda:validarUbicacionCruceroJ1(resultadoX,resultadoY,orientacion.get(),x,y) and guardarCrucero4J1(resultadoX,resultadoY,orientacion.get (),x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    orientacionLabel= Label(tablero, text="Orientacion del barco:")
    orientacionLabel.place(x=500,y=40)

    orientacionIzquierda=ttk.Radiobutton(tablero, text="Derecha", value= 1, variable=orientacion)
    orientacionIzquierda.place(x=600, y=60)
    orientacionDerecha=ttk.Radiobutton(tablero, text="Arriba", value=2, variable=orientacion)
    orientacionDerecha.place(x=800, y=60)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=900, y=60)

    imprimirMatrizJ1(x,y,tablero)

def guardarCrucero4J1(x,y,orientacion,co,fi):
    global nuevoJuego
    nuevoJuego["BarcosJ1"]["Crucero4J1"]["x1"]=x
    nuevoJuego["BarcosJ1"]["Crucero4J1"]["y1"]=y

    if orientacion==1:
        nuevoJuego["BarcosJ1"]["Crucero4J1"]["x2"]=x-1
        nuevoJuego["BarcosJ1"]["Crucero4J1"]["y2"]=y
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=5
        nuevoJuego["Matriz"]["matrizJ1"][y][x-1]=9

    elif orientacion==2:
        nuevoJuego["BarcosJ1"]["Crucero4J1"]["x2"]=x+1
        nuevoJuego["BarcosJ1"]["Crucero4J1"]["y2"]=y
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=6
        nuevoJuego["Matriz"]["matrizJ1"][y+1][x]=10

    elif orientacion==3:
        nuevoJuego["BarcosJ1"]["Crucero4J1"]["y2"]=y+1
        nuevoJuego["BarcosJ1"]["Crucero4J1"]["x2"]=x
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=7
        nuevoJuego["Matriz"]["matrizJ1"][y][x+1]=11

    elif orientacion==4:
        nuevoJuego["BarcosJ1"]["Crucero4J1"]["y2"]=y-1
        nuevoJuego["BarcosJ1"]["Crucero4J1"]["x2"]=x
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=8 
        nuevoJuego["Matriz"]["matrizJ1"][y-1][x]=12

    nuevoJuego["BarcosJ1"]["Crucero4J1"]["vida"]=True
    nuevoJuego["BarcosJ1"]["Crucero4J1"]["orientacion"]=orientacion
    ubicarAcorazado1J1(co,fi)
    return True

def ubicarAcorazado1J1(x,y):
    x=int(x)
    y=int(y)
    global matriz
    tablero=tk.Toplevel()
    tablero.title("Tablero")
    tablero.attributes("-fullscreen", True)

    tableroLabel= Label(tablero, text="Inserte la ubicacion del barco:")
    tableroLabel.place(x=1,y=10)

    orientacion= tk.IntVar()

    botonGuardarPosicion=Button(tablero, text="Guardar",command= lambda: validarUbicacionAcorazadoJ1(resultadoX,resultadoY,orientacion.get(),x,y) and guardarAcorazado1J1(resultadoX,resultadoY,orientacion.get (),x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    orientacionLabel= Label(tablero, text="Orientacion del barco:")
    orientacionLabel.place(x=500,y=40)

    orientacionIzquierda=ttk.Radiobutton(tablero, text="Derecha", value= 1, variable=orientacion)
    orientacionIzquierda.place(x=600, y=60)
    orientacionDerecha=ttk.Radiobutton(tablero, text="Arriba", value=2, variable=orientacion)
    orientacionDerecha.place(x=800, y=60)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=900, y=60)

    imprimirMatrizJ1(x,y,tablero)

def guardarAcorazado1J1(x,y,orientacion,co,fi):
    global nuevoJuego
    nuevoJuego["BarcosJ1"]["Acorazado1J1"]["x1"]=x
    nuevoJuego["BarcosJ1"]["Acorazado1J1"]["y1"]=y

    if orientacion==1:
        nuevoJuego["BarcosJ1"]["Acorazado1J1"]["x2"]=x-1
        nuevoJuego["BarcosJ1"]["Acorazado1J1"]["y2"]=y
        nuevoJuego["BarcosJ1"]["Acorazado1J1"]["x3"]=x-2
        nuevoJuego["BarcosJ1"]["Acorazado1J1"]["y3"]=y
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=13
        nuevoJuego["Matriz"]["matrizJ1"][y][x-1]=17
        nuevoJuego["Matriz"]["matrizJ1"][y][x-2]=21

    elif orientacion==2:
        nuevoJuego["BarcosJ1"]["Acorazado1J1"]["x2"]=x+1
        nuevoJuego["BarcosJ1"]["Acorazado1J1"]["y2"]=y
        nuevoJuego["BarcosJ1"]["Acorazado1J1"]["x3"]=x+2
        nuevoJuego["BarcosJ1"]["Acorazado1J1"]["y3"]=y
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=14
        nuevoJuego["Matriz"]["matrizJ1"][y+1][x]=18
        nuevoJuego["Matriz"]["matrizJ1"][y+2][x]=22

    elif orientacion==3:
        nuevoJuego["BarcosJ1"]["Acorazado1J1"]["y2"]=y+1
        nuevoJuego["BarcosJ1"]["Acorazado1J1"]["x2"]=x
        nuevoJuego["BarcosJ1"]["Acorazado1J1"]["y3"]=y+2
        nuevoJuego["BarcosJ1"]["Acorazado1J1"]["x3"]=x
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=15
        nuevoJuego["Matriz"]["matrizJ1"][y][x+1]=19
        nuevoJuego["Matriz"]["matrizJ1"][y][x+2]=23
        
    elif orientacion==4:
        nuevoJuego["BarcosJ1"]["Acorazado1J1"]["y2"]=y-1
        nuevoJuego["BarcosJ1"]["Acorazado1J1"]["x2"]=x
        nuevoJuego["BarcosJ1"]["Acorazado1J1"]["y3"]=y-2
        nuevoJuego["BarcosJ1"]["Acorazado1J1"]["x3"]=x
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=16
        nuevoJuego["Matriz"]["matrizJ1"][y-1][x]=20
        nuevoJuego["Matriz"]["matrizJ1"][y-2][x]=24

    nuevoJuego["BarcosJ1"]["Acorazado1J1"]["vida"]=True
    nuevoJuego["BarcosJ1"]["Acorazado1J1"]["orientacion"]=orientacion
    ubicarAcorazado2J1(co,fi)   
    return True

def ubicarAcorazado2J1(x,y):
    x=int(x)
    y=int(y)
    global matriz
    tablero=tk.Toplevel()
    tablero.title("Tablero")
    tablero.attributes("-fullscreen", True)

    tableroLabel= Label(tablero, text="Inserte la ubicacion del barco:")
    tableroLabel.place(x=1,y=10)

    orientacion= tk.IntVar()

    botonGuardarPosicion=Button(tablero, text="Guardar",command= lambda:validarUbicacionAcorazadoJ1(resultadoX,resultadoY,orientacion.get(),x,y) and guardarAcorazado2J1(resultadoX,resultadoY,orientacion.get (),x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    orientacionLabel= Label(tablero, text="Orientacion del barco:")
    orientacionLabel.place(x=500,y=40)

    orientacionIzquierda=ttk.Radiobutton(tablero, text="Derecha", value= 1, variable=orientacion)
    orientacionIzquierda.place(x=600, y=60)
    orientacionDerecha=ttk.Radiobutton(tablero, text="Arriba", value=2, variable=orientacion)
    orientacionDerecha.place(x=800, y=60)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=900, y=60)

    imprimirMatrizJ1(x,y,tablero)

def guardarAcorazado2J1(x,y,orientacion,co,fi):
    global nuevoJuego
    nuevoJuego["BarcosJ1"]["Acorazado2J1"]["x1"]=x
    nuevoJuego["BarcosJ1"]["Acorazado2J1"]["y1"]=y

    if orientacion==1:
        nuevoJuego["BarcosJ1"]["Acorazado2J1"]["x2"]=x-1
        nuevoJuego["BarcosJ1"]["Acorazado2J1"]["y2"]=y
        nuevoJuego["BarcosJ1"]["Acorazado2J1"]["x3"]=x-2
        nuevoJuego["BarcosJ1"]["Acorazado2J1"]["y3"]=y
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=13
        nuevoJuego["Matriz"]["matrizJ1"][y][x-1]=17
        nuevoJuego["Matriz"]["matrizJ1"][y][x-2]=21

    elif orientacion==2:
        nuevoJuego["BarcosJ1"]["Acorazado2J1"]["x2"]=x+1
        nuevoJuego["BarcosJ1"]["Acorazado2J1"]["y2"]=y
        nuevoJuego["BarcosJ1"]["Acorazado2J1"]["x3"]=x+2
        nuevoJuego["BarcosJ1"]["Acorazado2J1"]["y3"]=y
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=14
        nuevoJuego["Matriz"]["matrizJ1"][y+1][x]=18
        nuevoJuego["Matriz"]["matrizJ1"][y+2][x]=22

    elif orientacion==3:
        nuevoJuego["BarcosJ1"]["Acorazado2J1"]["y2"]=y+1
        nuevoJuego["BarcosJ1"]["Acorazado2J1"]["x2"]=x
        nuevoJuego["BarcosJ1"]["Acorazado2J1"]["y3"]=y+2
        nuevoJuego["BarcosJ1"]["Acorazado2J1"]["x3"]=x
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=15
        nuevoJuego["Matriz"]["matrizJ1"][y][x+1]=19
        nuevoJuego["Matriz"]["matrizJ1"][y][x+2]=23

    elif orientacion==4:
        nuevoJuego["BarcosJ1"]["Acorazado2J1"]["y2"]=y-1
        nuevoJuego["BarcosJ1"]["Acorazado2J1"]["x2"]=x
        nuevoJuego["BarcosJ1"]["Acorazado2J1"]["y3"]=y-2
        nuevoJuego["BarcosJ1"]["Acorazado2J1"]["x3"]=x
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=16
        nuevoJuego["Matriz"]["matrizJ1"][y-1][x]=20
        nuevoJuego["Matriz"]["matrizJ1"][y-2][x]=24

    nuevoJuego["BarcosJ1"]["Acorazado2J1"]["vida"]=True
    nuevoJuego["BarcosJ1"]["Acorazado2J1"]["orientacion"]=orientacion
    pantallaBarcosJ1(co,fi)
    return True

def pantallaBarcosJ1(x,y):
    x=int(x)
    y=int(y)
    global matriz
    tablero=tk.Toplevel()
    tablero.title("Tablero")
    tablero.attributes("-fullscreen", True)

    tableroLabel= Label(tablero, text="Barcos del jugador 1")
    tableroLabel.place(x=1,y=10)

    botonGuardarPosicion=Button(tablero, text="Continuar",command= lambda:ubicarDestructor1J2(x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    imprimirMatrizJ1(x,y,tablero)
    print(nuevoJuego["BarcosJ1"])




def ubicarDestructor1J2(x,y):
    x=int(x)
    y=int(y)
    global matriz
    tablero=tk.Toplevel()
    tablero.title("Tablero")
    tablero.attributes("-fullscreen", True)

    tableroLabel= Label(tablero, text="Inserte la ubicacion del barco:")
    tableroLabel.place(x=1,y=10)

    orientacion= tk.IntVar()

    botonGuardarPosicion=Button(tablero, text="Guardar",command= lambda: validarUbicacionDestructorJ2(resultadoX,resultadoY,orientacion.get()) and guardarDestructor1J2(resultadoX,resultadoY,orientacion.get (),x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    orientacionIzquierda=ttk.Radiobutton(tablero, text="Derecha", value= 1, variable=orientacion)
    orientacionIzquierda.place(x=600, y=60)
    orientacionDerecha=ttk.Radiobutton(tablero, text="Arriba", value=2, variable=orientacion)
    orientacionDerecha.place(x=800, y=60)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=900, y=60)
    
    imprimirMatrizJ2(x,y,tablero)

    return True

def guardarDestructor1J2(x,y,orientacion,co,fi):
    global nuevoJuego
    nuevoJuego["BarcosJ2"]["Destructor1J2"]["x1"]=x
    nuevoJuego["BarcosJ2"]["Destructor1J2"]["y1"]=y
    nuevoJuego["BarcosJ2"]["Destructor1J2"]["vida"]=True
    nuevoJuego["BarcosJ2"]["Destructor1J2"]["orientacion"]=orientacion
    
    if orientacion==1:
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=1

    elif orientacion==2:
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=2
    
    elif orientacion==3:
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=3
    
    elif orientacion==4:
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=4
        
    ubicarDestructor2J2(co,fi)
    return True

def ubicarDestructor2J2(x,y):
    x=int(x)
    y=int(y)
    global matriz
    tablero=tk.Toplevel()
    tablero.title("Tablero")
    tablero.attributes("-fullscreen", True)

    tableroLabel= Label(tablero, text="Inserte la ubicacion del barco:")
    tableroLabel.place(x=1,y=10)

    orientacion= tk.IntVar()

    botonGuardarPosicion=Button(tablero, text="Guardar",command= lambda: validarUbicacionDestructorJ2(resultadoX,resultadoY,orientacion.get()) and guardarDestructor2J2(resultadoX,resultadoY,orientacion.get (),x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    orientacionLabel= Label(tablero, text="Orientacion del barco:")
    orientacionLabel.place(x=500,y=40)

    orientacionIzquierda=ttk.Radiobutton(tablero, text="Derecha", value= 1, variable=orientacion)
    orientacionIzquierda.place(x=600, y=60)
    orientacionDerecha=ttk.Radiobutton(tablero, text="Arriba", value=2, variable=orientacion)
    orientacionDerecha.place(x=800, y=60)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=900, y=60)

    imprimirMatrizJ2(x,y,tablero)

def guardarDestructor2J2(x,y,orientacion,co,fi):
    global nuevoJuego
    nuevoJuego["BarcosJ2"]["Destructor2J2"]["x1"]=x
    nuevoJuego["BarcosJ2"]["Destructor2J2"]["y1"]=y
    nuevoJuego["BarcosJ2"]["Destructor2J2"]["vida"]=True
    nuevoJuego["BarcosJ2"]["Destructor2J2"]["orientacion"]=orientacion

    if orientacion==1:
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=1

    elif orientacion==2:
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=2
    
    elif orientacion==3:
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=3
    
    elif orientacion==4:
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=4
        
    ubicarDestructor3J2(co,fi)
    return True

def ubicarDestructor3J2(x,y):
    x=int(x)
    y=int(y)
    global matriz
    tablero=tk.Toplevel()
    tablero.title("Tablero")
    tablero.attributes("-fullscreen", True)

    tableroLabel= Label(tablero, text="Inserte la ubicacion del barco:")
    tableroLabel.place(x=1,y=10)

    orientacion= tk.IntVar()

    botonGuardarPosicion=Button(tablero, text="Guardar",command= lambda:validarUbicacionDestructorJ2(resultadoX,resultadoY,orientacion.get()) and guardarDestructor3J2(resultadoX,resultadoY,orientacion.get(),x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    orientacionLabel= Label(tablero, text="Orientacion del barco:")
    orientacionLabel.place(x=500,y=40)

    orientacionIzquierda=ttk.Radiobutton(tablero, text="Derecha", value= 1, variable=orientacion)
    orientacionIzquierda.place(x=600, y=60)
    orientacionDerecha=ttk.Radiobutton(tablero, text="Arriba", value=2, variable=orientacion)
    orientacionDerecha.place(x=800, y=60)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=900, y=60)

    imprimirMatrizJ2(x,y,tablero)

def guardarDestructor3J2(x,y,orientacion,co,fi):
    global nuevoJuego
    nuevoJuego["BarcosJ2"]["Destructor3J2"]["x1"]=x
    nuevoJuego["BarcosJ2"]["Destructor3J2"]["y1"]=y
    nuevoJuego["BarcosJ2"]["Destructor3J2"]["vida"]=True
    nuevoJuego["BarcosJ2"]["Destructor3J2"]["orientacion"]=orientacion
    
    if orientacion==1:
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=1

    elif orientacion==2:
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=2
    
    elif orientacion==3:
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=3
    
    elif orientacion==4:
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=4
        
    ubicarDestructor4J2(co,fi)
    return True

def ubicarDestructor4J2(x,y):
    x=int(x)
    y=int(y)
    global matriz
    tablero=tk.Toplevel()
    tablero.title("Tablero")
    tablero.attributes("-fullscreen", True)

    tableroLabel= Label(tablero, text="Inserte la ubicacion del barco:")
    tableroLabel.place(x=1,y=10)

    orientacion= tk.IntVar()

    botonGuardarPosicion=Button(tablero, text="Guardar",command= lambda:validarUbicacionDestructorJ2(resultadoX,resultadoY,orientacion.get()) and guardarDestructor4J2(resultadoX,resultadoY,orientacion.get(),x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    orientacionLabel= Label(tablero, text="Orientacion del barco:")
    orientacionLabel.place(x=500,y=40)

    orientacionIzquierda=ttk.Radiobutton(tablero, text="Derecha", value= 1, variable=orientacion)
    orientacionIzquierda.place(x=600, y=60)
    orientacionDerecha=ttk.Radiobutton(tablero, text="Arriba", value=2, variable=orientacion)
    orientacionDerecha.place(x=800, y=60)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=900, y=60)

    imprimirMatrizJ2(x,y,tablero)

def guardarDestructor4J2(x,y,orientacion,co,fi):
    global nuevoJuego
    nuevoJuego["BarcosJ2"]["Destructor4J2"]["x1"]=x
    nuevoJuego["BarcosJ2"]["Destructor4J2"]["y1"]=y
    nuevoJuego["BarcosJ2"]["Destructor4J2"]["vida"]=True
    nuevoJuego["BarcosJ2"]["Destructor4J2"]["orientacion"]=orientacion
    
    if orientacion==1:
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=1

    elif orientacion==2:
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=2
    
    elif orientacion==3:
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=3
    
    elif orientacion==4:
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=4
        
    ubicarDestructor5J2(co,fi)
    return True

def ubicarDestructor5J2(x,y):
    x=int(x)
    y=int(y)
    global matriz
    tablero=tk.Toplevel()
    tablero.title("Tablero")
    tablero.attributes("-fullscreen", True)

    tableroLabel= Label(tablero, text="Inserte la ubicacion del barco:")
    tableroLabel.place(x=1,y=10)

    orientacion= tk.IntVar()

    botonGuardarPosicion=Button(tablero, text="Guardar",command= lambda:validarUbicacionDestructorJ2(resultadoX,resultadoY,orientacion.get()) and guardarDestructor5J2(resultadoX,resultadoY,orientacion.get (),x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    orientacionLabel= Label(tablero, text="Orientacion del barco:")
    orientacionLabel.place(x=500,y=40)    

    orientacionIzquierda=ttk.Radiobutton(tablero, text="Derecha", value= 1, variable=orientacion)
    orientacionIzquierda.place(x=600, y=60)
    orientacionDerecha=ttk.Radiobutton(tablero, text="Arriba", value=2, variable=orientacion)
    orientacionDerecha.place(x=800, y=60)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=900, y=60)

    imprimirMatrizJ2(x,y,tablero)

def guardarDestructor5J2(x,y,orientacion,co,fi):
    global nuevoJuego
    nuevoJuego["BarcosJ2"]["Destructor5J2"]["x1"]=x
    nuevoJuego["BarcosJ2"]["Destructor5J2"]["y1"]=y
    nuevoJuego["BarcosJ2"]["Destructor5J2"]["vida"]=True
    nuevoJuego["BarcosJ2"]["Destructor5J2"]["orientacion"]=orientacion
    
    if orientacion==1:
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=1

    elif orientacion==2:
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=2
    
    elif orientacion==3:
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=3
    
    elif orientacion==4:
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=4

    ubicarDestructor6J2(co,fi)
    return True

def ubicarDestructor6J2(x,y):
    x=int(x)
    y=int(y)
    global matriz
    tablero=tk.Toplevel()
    tablero.title("Tablero")
    tablero.attributes("-fullscreen", True)

    tableroLabel= Label(tablero, text="Inserte la ubicacion del barco:")
    tableroLabel.place(x=1,y=10)

    orientacion= tk.IntVar()

    botonGuardarPosicion=Button(tablero, text="Guardar",command= lambda: validarUbicacionDestructorJ2(resultadoX,resultadoY,orientacion.get()) and guardarDestructor6J2(resultadoX,resultadoY,orientacion.get (),x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    orientacionLabel= Label(tablero, text="Orientacion del barco:")
    orientacionLabel.place(x=500,y=40)

    orientacionIzquierda=ttk.Radiobutton(tablero, text="Derecha", value= 1, variable=orientacion)
    orientacionIzquierda.place(x=600, y=60)
    orientacionDerecha=ttk.Radiobutton(tablero, text="Arriba", value=2, variable=orientacion)
    orientacionDerecha.place(x=800, y=60)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=900, y=60)

    imprimirMatrizJ2(x,y,tablero)

def guardarDestructor6J2(x,y,orientacion,co,fi):
    global nuevoJuego
    nuevoJuego["BarcosJ2"]["Destructor6J2"]["x1"]=x
    nuevoJuego["BarcosJ2"]["Destructor6J2"]["y1"]=y
    nuevoJuego["BarcosJ2"]["Destructor6J2"]["vida"]=True
    nuevoJuego["BarcosJ2"]["Destructor6J2"]["orientacion"]=orientacion
    
    if orientacion==1:
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=1

    elif orientacion==2:
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=2
    
    elif orientacion==3:
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=3
    
    elif orientacion==4:
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=4

    ubicarCrucero1J2(co,fi)
    return True

def ubicarCrucero1J2(x,y):
    x=int(x)
    y=int(y)
    global matriz
    tablero=tk.Toplevel()
    tablero.title("Tablero")
    tablero.attributes("-fullscreen", True)

    tableroLabel= Label(tablero, text="Inserte la ubicacion del barco:")
    tableroLabel.place(x=1,y=10)

    orientacion= tk.IntVar()

    botonGuardarPosicion=Button(tablero, text="Guardar",command= lambda: validarUbicacionCruceroJ2(resultadoX,resultadoY,orientacion.get(),x,y) and guardarCrucero1J2(resultadoX,resultadoY,orientacion.get (),x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    orientacionLabel= Label(tablero, text="Orientacion del barco:")
    orientacionLabel.place(x=500,y=40) 

    orientacionIzquierda=ttk.Radiobutton(tablero, text="Derecha", value= 1, variable=orientacion)
    orientacionIzquierda.place(x=600, y=60)
    orientacionDerecha=ttk.Radiobutton(tablero, text="Arriba", value=2, variable=orientacion)
    orientacionDerecha.place(x=800, y=60)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=900, y=60)
    
    imprimirMatrizJ2(x,y,tablero)

def guardarCrucero1J2(x,y,orientacion,co,fi):
    global nuevoJuego
    nuevoJuego["BarcosJ2"]["Crucero1J2"]["x1"]=x
    nuevoJuego["BarcosJ2"]["Crucero1J2"]["y1"]=y

    if orientacion==1:
        nuevoJuego["BarcosJ2"]["Crucero1J2"]["x2"]=x-1
        nuevoJuego["BarcosJ2"]["Crucero1J2"]["y2"]=y
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=5
        nuevoJuego["Matriz"]["matrizJ2"][y][x-1]=9

    elif orientacion==2:
        nuevoJuego["BarcosJ2"]["Crucero1J2"]["x2"]=x+1
        nuevoJuego["BarcosJ2"]["Crucero1J2"]["y2"]=y
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=6
        nuevoJuego["Matriz"]["matrizJ2"][y+1][x]=10

    elif orientacion==3:
        nuevoJuego["BarcosJ2"]["Crucero1J2"]["y2"]=y+1
        nuevoJuego["BarcosJ2"]["Crucero1J2"]["x2"]=x
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=7
        nuevoJuego["Matriz"]["matrizJ2"][y][x+1]=11

    elif orientacion==4:
        nuevoJuego["BarcosJ2"]["Crucero1J2"]["y2"]=y-1
        nuevoJuego["BarcosJ2"]["Crucero1J2"]["x2"]=x
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=8
        nuevoJuego["Matriz"]["matrizJ2"][y-1][x]=12

    nuevoJuego["BarcosJ2"]["Crucero1J2"]["vida"]=True
    nuevoJuego["BarcosJ2"]["Crucero1J2"]["horientacion"]=orientacion
    
    ubicarCrucero2J2(co,fi) 
    return True

def ubicarCrucero2J2(x,y):
    x=int(x)
    y=int(y)
    global matriz
    tablero=tk.Toplevel()
    tablero.title("Tablero")
    tablero.attributes("-fullscreen", True)

    tableroLabel= Label(tablero, text="Inserte la ubicacion del barco:")
    tableroLabel.place(x=1,y=10)

    orientacion= tk.IntVar()

    botonGuardarPosicion=Button(tablero, text="Guardar",command=lambda: validarUbicacionCruceroJ2(resultadoX,resultadoY,orientacion.get(),x,y) and guardarCrucero2J2(resultadoX,resultadoY,orientacion.get (),x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    orientacionLabel= Label(tablero, text="Orientacion del barco:")
    orientacionLabel.place(x=500,y=40)

    orientacionIzquierda=ttk.Radiobutton(tablero, text="Derecha", value= 1, variable=orientacion)
    orientacionIzquierda.place(x=600, y=60)
    orientacionDerecha=ttk.Radiobutton(tablero, text="Arriba", value=2, variable=orientacion)
    orientacionDerecha.place(x=800, y=60)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=900, y=60)

    imprimirMatrizJ2(x,y,tablero)

def guardarCrucero2J2(x,y,orientacion,co,fi):
    global nuevoJuego
    nuevoJuego["BarcosJ2"]["Crucero2J2"]["x1"]=x
    nuevoJuego["BarcosJ2"]["Crucero2J2"]["y1"]=y

    if orientacion==1:
        nuevoJuego["BarcosJ2"]["Crucero2J2"]["x2"]=x-1
        nuevoJuego["BarcosJ2"]["Crucero2J2"]["y2"]=y
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=5
        nuevoJuego["Matriz"]["matrizJ2"][y][x-1]=9

    elif orientacion==2:
        nuevoJuego["BarcosJ2"]["Crucero2J2"]["x2"]=x+1
        nuevoJuego["BarcosJ2"]["Crucero2J2"]["y2"]=y
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=6
        nuevoJuego["Matriz"]["matrizJ2"][y+1][x]=10

    elif orientacion==3:
        nuevoJuego["BarcosJ2"]["Crucero2J2"]["y2"]=y+1
        nuevoJuego["BarcosJ2"]["Crucero2J2"]["x2"]=x
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=7
        nuevoJuego["Matriz"]["matrizJ2"][y][x+1]=11

    elif orientacion==4:
        nuevoJuego["BarcosJ2"]["Crucero2J2"]["y2"]=y-1
        nuevoJuego["BarcosJ2"]["Crucero2J2"]["x2"]=x
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=8
        nuevoJuego["Matriz"]["matrizJ2"][y-1][x]=12

    nuevoJuego["BarcosJ2"]["Crucero2J2"]["vida"]=True
    nuevoJuego["BarcosJ2"]["Crucero2J2"]["orientacion"]=orientacion
    ubicarCrucero3J2(co,fi) 
    return True

def ubicarCrucero3J2(x,y):
    x=int(x)
    y=int(y)
    global matriz
    tablero=tk.Toplevel()
    tablero.title("Tablero")
    tablero.attributes("-fullscreen", True)

    tableroLabel= Label(tablero, text="Inserte la ubicacion del barco:")
    tableroLabel.place(x=1,y=10)
    
    orientacion= tk.IntVar()

    botonGuardarPosicion=Button(tablero, text="Guardar",command= lambda:validarUbicacionCruceroJ2(resultadoX,resultadoY,orientacion.get(),x,y) and guardarCrucero3J2(resultadoX,resultadoY,orientacion.get (),x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    orientacionLabel= Label(tablero, text="Orientacion del barco:")
    orientacionLabel.place(x=500,y=40)

    orientacionIzquierda=ttk.Radiobutton(tablero, text="Derecha", value= 1, variable=orientacion)
    orientacionIzquierda.place(x=600, y=60)
    orientacionDerecha=ttk.Radiobutton(tablero, text="Arriba", value=2, variable=orientacion)
    orientacionDerecha.place(x=800, y=60)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=900, y=60)

    imprimirMatrizJ2(x,y,tablero)

def guardarCrucero3J2(x,y,orientacion,co,fi):
    global nuevoJuego
    nuevoJuego["BarcosJ2"]["Crucero3J2"]["x1"]=x
    nuevoJuego["BarcosJ2"]["Crucero3J2"]["y1"]=y

    if orientacion==1:
        nuevoJuego["BarcosJ2"]["Crucero3J2"]["x2"]=x-1
        nuevoJuego["BarcosJ2"]["Crucero3J2"]["y2"]=y
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=5
        nuevoJuego["Matriz"]["matrizJ2"][y][x-1]=9

    elif orientacion==2:
        nuevoJuego["BarcosJ2"]["Crucero3J2"]["x2"]=x+1
        nuevoJuego["BarcosJ2"]["Crucero3J2"]["y2"]=y
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=6
        nuevoJuego["Matriz"]["matrizJ2"][y+1][x]=10

    elif orientacion==3:
        nuevoJuego["BarcosJ2"]["Crucero3J2"]["y2"]=y+1
        nuevoJuego["BarcosJ2"]["Crucero3J2"]["x2"]=x
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=7
        nuevoJuego["Matriz"]["matrizJ2"][y][x+1]=11

    elif orientacion==4:
        nuevoJuego["BarcosJ2"]["Crucero3J2"]["y2"]=y-1
        nuevoJuego["BarcosJ2"]["Crucero3J2"]["x2"]=x
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=8
        nuevoJuego["Matriz"]["matrizJ2"][y-1][x]=12

    nuevoJuego["BarcosJ2"]["Crucero3J2"]["vida"]=True
    nuevoJuego["BarcosJ2"]["Crucero3J2"]["orientacion"]=orientacion
    ubicarCrucero4J2(co,fi)
    return True

def ubicarCrucero4J2(x,y):
    x=int(x)
    y=int(y)
    global matriz
    tablero=tk.Toplevel()
    tablero.title("Tablero")
    tablero.attributes("-fullscreen", True)

    tableroLabel= Label(tablero, text="Inserte la ubicacion del barco:")
    tableroLabel.place(x=1,y=10)

    orientacion= tk.IntVar()

    botonGuardarPosicion=Button(tablero, text="Guardar",command= lambda:validarUbicacionCruceroJ2(resultadoX,resultadoY,orientacion.get(),x,y) and guardarCrucero4J2(resultadoX,resultadoY,orientacion.get (),x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    orientacionLabel= Label(tablero, text="Orientacion del barco:")
    orientacionLabel.place(x=500,y=40)

    orientacionIzquierda=ttk.Radiobutton(tablero, text="Derecha", value= 1, variable=orientacion)
    orientacionIzquierda.place(x=600, y=60)
    orientacionDerecha=ttk.Radiobutton(tablero, text="Arriba", value=2, variable=orientacion)
    orientacionDerecha.place(x=800, y=60)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=900, y=60)

    imprimirMatrizJ2(x,y,tablero)

def guardarCrucero4J2(x,y,orientacion,co,fi):
    global nuevoJuego
    nuevoJuego["BarcosJ2"]["Crucero4J2"]["x1"]=x
    nuevoJuego["BarcosJ2"]["Crucero4J2"]["y1"]=y

    if orientacion==1:
        nuevoJuego["BarcosJ2"]["Crucero4J2"]["x2"]=x-1
        nuevoJuego["BarcosJ2"]["Crucero4J2"]["y2"]=y
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=5
        nuevoJuego["Matriz"]["matrizJ2"][y][x-1]=9

    elif orientacion==2:
        nuevoJuego["BarcosJ2"]["Crucero4J2"]["x2"]=x+1
        nuevoJuego["BarcosJ2"]["Crucero4J2"]["y2"]=y
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=6
        nuevoJuego["Matriz"]["matrizJ2"][y+1][x]=10

    elif orientacion==3:
        nuevoJuego["BarcosJ2"]["Crucero4J2"]["y2"]=y+1
        nuevoJuego["BarcosJ2"]["Crucero4J2"]["x2"]=x
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=7
        nuevoJuego["Matriz"]["matrizJ2"][y][x+1]=11

    elif orientacion==4:
        nuevoJuego["BarcosJ2"]["Crucero4J2"]["y2"]=y-1
        nuevoJuego["BarcosJ2"]["Crucero4J2"]["x2"]=x
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=8
        nuevoJuego["Matriz"]["matrizJ2"][y-1][x]=12

    nuevoJuego["BarcosJ2"]["Crucero4J2"]["vida"]=True
    nuevoJuego["BarcosJ2"]["Crucero4J2"]["orientacion"]=orientacion
   
    ubicarAcorazado1J2(co,fi)
    return True

def ubicarAcorazado1J2(x,y):
    x=int(x)
    y=int(y)
    global matriz
    tablero=tk.Toplevel()
    tablero.title("Tablero")
    tablero.attributes("-fullscreen", True)

    tableroLabel= Label(tablero, text="Inserte la ubicacion del barco:")
    tableroLabel.place(x=1,y=10)

    orientacion= tk.IntVar()

    botonGuardarPosicion=Button(tablero, text="Guardar",command= lambda: validarUbicacionAcorazadoJ2(resultadoX,resultadoY,orientacion.get(),x,y) and guardarAcorazado1J2(resultadoX,resultadoY,orientacion.get (),x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    orientacionLabel= Label(tablero, text="Orientacion del barco:")
    orientacionLabel.place(x=500,y=40)

    orientacionIzquierda=ttk.Radiobutton(tablero, text="Derecha", value= 1, variable=orientacion)
    orientacionIzquierda.place(x=600, y=60)
    orientacionDerecha=ttk.Radiobutton(tablero, text="Arriba", value=2, variable=orientacion)
    orientacionDerecha.place(x=800, y=60)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=900, y=60)

    imprimirMatrizJ2(x,y,tablero)

def guardarAcorazado1J2(x,y,orientacion,co,fi):
    global nuevoJuego
    nuevoJuego["BarcosJ2"]["Acorazado1J2"]["x1"]=x
    nuevoJuego["BarcosJ2"]["Acorazado1J2"]["y1"]=y

    if orientacion==1:
        nuevoJuego["BarcosJ2"]["Acorazado1J2"]["x2"]=x-1
        nuevoJuego["BarcosJ2"]["Acorazado1J2"]["y2"]=y
        nuevoJuego["BarcosJ2"]["Acorazado1J2"]["x3"]=x-2
        nuevoJuego["BarcosJ2"]["Acorazado1J2"]["y3"]=y
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=13
        nuevoJuego["Matriz"]["matrizJ2"][y][x-1]=17
        nuevoJuego["Matriz"]["matrizJ2"][y][x-2]=21

    elif orientacion==2:
        nuevoJuego["BarcosJ2"]["Acorazado1J2"]["x2"]=x+1
        nuevoJuego["BarcosJ2"]["Acorazado1J2"]["y2"]=y
        nuevoJuego["BarcosJ2"]["Acorazado1J2"]["x3"]=x+2
        nuevoJuego["BarcosJ2"]["Acorazado1J2"]["y3"]=y
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=14
        nuevoJuego["Matriz"]["matrizJ2"][y+1][x]=18
        nuevoJuego["Matriz"]["matrizJ2"][y+2][x]=22

    elif orientacion==3:
        nuevoJuego["BarcosJ2"]["Acorazado1J2"]["y2"]=y+1
        nuevoJuego["BarcosJ2"]["Acorazado1J2"]["x2"]=x
        nuevoJuego["BarcosJ2"]["Acorazado1J2"]["y3"]=y+2
        nuevoJuego["BarcosJ2"]["Acorazado1J2"]["x3"]=x
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=15
        nuevoJuego["Matriz"]["matrizJ2"][y][x+1]=19
        nuevoJuego["Matriz"]["matrizJ2"][y][x+2]=23

    elif orientacion==4:
        nuevoJuego["BarcosJ2"]["Acorazado1J2"]["y2"]=y-1
        nuevoJuego["BarcosJ2"]["Acorazado1J2"]["x2"]=x
        nuevoJuego["BarcosJ2"]["Acorazado1J2"]["y3"]=y-2
        nuevoJuego["BarcosJ2"]["Acorazado1J2"]["x3"]=x
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=16
        nuevoJuego["Matriz"]["matrizJ2"][y-1][x]=20
        nuevoJuego["Matriz"]["matrizJ2"][y-2][x]=24

    nuevoJuego["BarcosJ2"]["Acorazado1J2"]["vida"]=True
    nuevoJuego["BarcosJ2"]["Acorazado1J2"]["orientacion"]=orientacion
    ubicarAcorazado2J2(co,fi)   
    return True

def ubicarAcorazado2J2(x,y):
    x=int(x)
    y=int(y)
    global matriz
    tablero=tk.Toplevel()
    tablero.title("Tablero")
    tablero.attributes("-fullscreen", True)

    tableroLabel= Label(tablero, text="Inserte la ubicacion del barco:")
    tableroLabel.place(x=1,y=10)

    orientacion= tk.IntVar()

    botonGuardarPosicion=Button(tablero, text="Guardar",command= lambda:validarUbicacionAcorazadoJ1(resultadoX,resultadoY,orientacion.get(),x,y) and guardarAcorazado2J2(resultadoX,resultadoY,orientacion.get (),x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    orientacionLabel= Label(tablero, text="Orientacion del barco:")
    orientacionLabel.place(x=500,y=40)

    orientacionIzquierda=ttk.Radiobutton(tablero, text="Derecha", value= 1, variable=orientacion)
    orientacionIzquierda.place(x=600, y=60)
    orientacionDerecha=ttk.Radiobutton(tablero, text="Arriba", value=2, variable=orientacion)
    orientacionDerecha.place(x=800, y=60)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=900, y=60)

    imprimirMatrizJ2(x,y,tablero)

def guardarAcorazado2J2(x,y,orientacion,co,fi):
    global nuevoJuego
    nuevoJuego["BarcosJ2"]["Acorazado2J2"]["x1"]=x
    nuevoJuego["BarcosJ2"]["Acorazado2J2"]["y1"]=y

    if orientacion==1:
        nuevoJuego["BarcosJ2"]["Acorazado2J2"]["x2"]=x-1
        nuevoJuego["BarcosJ2"]["Acorazado2J2"]["y2"]=y
        nuevoJuego["BarcosJ2"]["Acorazado2J2"]["x3"]=x-2
        nuevoJuego["BarcosJ2"]["Acorazado2J2"]["y3"]=y
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=13
        nuevoJuego["Matriz"]["matrizJ2"][y][x-1]=17
        nuevoJuego["Matriz"]["matrizJ2"][y][x-2]=21

    elif orientacion==2:
        nuevoJuego["BarcosJ2"]["Acorazado2J2"]["x2"]=x+1
        nuevoJuego["BarcosJ2"]["Acorazado2J2"]["y2"]=y
        nuevoJuego["BarcosJ2"]["Acorazado2J2"]["x3"]=x+2
        nuevoJuego["BarcosJ2"]["Acorazado2J2"]["y3"]=y
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=14
        nuevoJuego["Matriz"]["matrizJ2"][y+1][x]=18
        nuevoJuego["Matriz"]["matrizJ2"][y+2][x]=22

    elif orientacion==3:
        nuevoJuego["BarcosJ2"]["Acorazado2J2"]["y2"]=y+1
        nuevoJuego["BarcosJ2"]["Acorazado2J2"]["x2"]=x
        nuevoJuego["BarcosJ2"]["Acorazado2J2"]["y3"]=y+2
        nuevoJuego["BarcosJ2"]["Acorazado2J2"]["x3"]=x
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=15
        nuevoJuego["Matriz"]["matrizJ2"][y][x+1]=19
        nuevoJuego["Matriz"]["matrizJ2"][y][x+2]=23

    elif orientacion==4:
        nuevoJuego["BarcosJ2"]["Acorazado2J2"]["y2"]=y-1
        nuevoJuego["BarcosJ2"]["Acorazado2J2"]["x2"]=x
        nuevoJuego["BarcosJ2"]["Acorazado2J2"]["y3"]=y-2
        nuevoJuego["BarcosJ2"]["Acorazado2J2"]["x3"]=x
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=16
        nuevoJuego["Matriz"]["matrizJ2"][y-1][x]=20
        nuevoJuego["Matriz"]["matrizJ2"][y-2][x]=24

    nuevoJuego["BarcosJ2"]["Acorazado2J2"]["vida"]=True
    nuevoJuego["BarcosJ2"]["Acorazado2J2"]["orientacion"]=orientacion 
    pantallaBarcosJ2(co,fi)  
    return True

def pantallaBarcosJ2(x,y):
    x=int(x)
    y=int(y)
    global matriz
    tablero=tk.Toplevel()
    tablero.title("Tablero")
    tablero.attributes("-fullscreen", True)

    tableroLabel= Label(tablero, text="Barcos del jugador 2")
    tableroLabel.place(x=1,y=10)

    botonGuardarPosicion=Button(tablero, text="Continuar",command= lambda:"Funcion" and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    imprimirMatrizJ2(x,y,tablero)

    print(nuevoJuego["BarcosJ2"])
#Destructor
imagenDestructor = Image.open("b1.png")                 #Esto, todo el destructor                       
imagenDestructor = imagenDestructor.resize((40, 40))    #Revisar el tamañqo de la imagen

imagen1 = imagenDestructor                              #Derecha
imagen1 = ImageTk.PhotoImage(imagen1)

imagen2 = imagenDestructor.rotate(90)                   #Arriba
imagen2 = ImageTk.PhotoImage(imagen2)

imagen3 = imagenDestructor.rotate(180)                  #Izquierda
imagen3 = ImageTk.PhotoImage(imagen3)

imagen4 = imagenDestructor.rotate(270)                  #Abajo
imagen4 = ImageTk.PhotoImage(imagen4)


#Crucero
imagenCrucero1 = Image.open("b21.png")                  #Esto, frente del crucero
imagenCrucero1 = imagenCrucero1.resize((50, 50))        #Revisar el tamaño de la imagen

imagen5 = imagenCrucero1                                #Derecha
imagen5 = ImageTk.PhotoImage(imagen5)

imagen6 = imagenCrucero1.rotate(90)                     #Arriba
imagen6 = ImageTk.PhotoImage(imagen6)

imagen7 = imagenCrucero1.rotate(180)                    #Izquierda
imagen7 = ImageTk.PhotoImage(imagen7)

imagen8 = imagenCrucero1.rotate(270)                    #Abajo
imagen8 = ImageTk.PhotoImage(imagen8)

imagenCrucero2 = Image.open("b22.png")                  #Esto, parte trasera del crucero
imagenCrucero2 = imagenCrucero2.resize((50, 50))        #Revisar el tamaño de la imagen

imagen9 = imagenCrucero2                                #Derecha
imagen9 = ImageTk.PhotoImage(imagen9)

imagen10 = imagenCrucero2.rotate(90)                    #Arriba
imagen10 = ImageTk.PhotoImage(imagen10)

imagen11 = imagenCrucero2.rotate(180)                   #Izquierda
imagen11 = ImageTk.PhotoImage(imagen11)

imagen12 = imagenCrucero2.rotate(270)                   #Abajo
imagen12 = ImageTk.PhotoImage(imagen12)



#Acorazado
imagenAcorazado1 = Image.open("b31.png")                #Esto, frente del acorazado
imagenAcorazado1 = imagenAcorazado1.resize((50, 50))    #Revisar el tamaño de la imagen

imagen13 = imagenAcorazado1                             #Derecha
imagen13 = ImageTk.PhotoImage(imagen13)

imagen14 = imagenAcorazado1.rotate(90)                  #Arriba
imagen14 = ImageTk.PhotoImage(imagen14)

imagen15 = imagenAcorazado1.rotate(180)                 #Izquierda
imagen15 = ImageTk.PhotoImage(imagen15)

imagen16 = imagenAcorazado1.rotate(270)                 #Abajo
imagen16 = ImageTk.PhotoImage(imagen16)

imagenAcorazado2 = Image.open("b32.png")                #Esto, parte trasera del medio del acorazado
imagenAcorazado2 = imagenAcorazado2.resize((50, 50))    #Revisar el tamaño de la imagen

imagen17 = imagenAcorazado2                             #Derecha
imagen17 = ImageTk.PhotoImage(imagen17)

imagen18 = imagenAcorazado2.rotate(90)                  #Arriba
imagen18 = ImageTk.PhotoImage(imagen18)

imagen19 = imagenAcorazado2.rotate(180)                 #Izquierda
imagen19 = ImageTk.PhotoImage(imagen19)

imagen20 = imagenAcorazado2.rotate(270)                 #Abajo
imagen20 = ImageTk.PhotoImage(imagen20)

imagenAcorazado3 = Image.open("b33.png")                #Esto, parte trasera del acorazado
imagenAcorazado3 = imagenAcorazado3.resize((50, 50))    #Revisar el tamaño de la imagen

imagen21 = imagenAcorazado3                             #Derecha
imagen21 = ImageTk.PhotoImage(imagen21)

imagen22 = imagenAcorazado3.rotate(90)                  #Arriba
imagen22 = ImageTk.PhotoImage(imagen22)

imagen23 = imagenAcorazado3.rotate(180)                 #Izquierda
imagen23 = ImageTk.PhotoImage(imagen23)

imagen24 = imagenAcorazado3.rotate(270)                 #Abajo
imagen24 = ImageTk.PhotoImage(imagen24)

def validarUbicacionDestructorJ1(x,y,orientacion):
    global nuevoJuego
    if orientacion==1:
        if nuevoJuego["Matriz"]["matrizJ1"][y][x]!=0:
            return False
        else:
            return True

    elif orientacion==2:
        if nuevoJuego["Matriz"]["matrizJ1"][y][x]!=0:
            return False
        else:
            return True

    elif orientacion==3:
        if nuevoJuego["Matriz"]["matrizJ1"][y][x] !=0:
            return False
        else:
            return True
    
    elif orientacion==4:
        if nuevoJuego["Matriz"]["matrizJ1"][y][x] !=0:
            return False
        else:
            return True

def validarUbicacionCruceroJ1(x, y, orientacion, filas, columnas):
    global nuevoJuego
    if orientacion == 1:
        if x < 1 or nuevoJuego["Matriz"]["matrizJ1"][y][x] != 0 or nuevoJuego["Matriz"]["matrizJ1"][y][x-1] != 0:
            return False
        else:
            return True
    elif orientacion == 2:
        if y > filas - 2 or nuevoJuego["Matriz"]["matrizJ1"][y][x] != 0 or nuevoJuego["Matriz"]["matrizJ1"][y+1][x] != 0:
            return False
        else:
            return True
    elif orientacion == 3:
        if x > columnas - 2 or nuevoJuego["Matriz"]["matrizJ1"][y][x] != 0 or nuevoJuego["Matriz"]["matrizJ1"][y][x+1] != 0:
            return False
        else:
            return True
    elif orientacion == 4:
        if y < 1 or nuevoJuego["Matriz"]["matrizJ1"][y][x] != 0 or nuevoJuego["Matriz"]["matrizJ1"][y-1][x] != 0:
            return False
        else:
            return True
       
def validarUbicacionAcorazadoJ1(x, y, orientacion, filas, columnas):
    global nuevoJuego
    if orientacion == 1:
        if x < 2 or nuevoJuego["Matriz"]["matrizJ1"][y][x] != 0 or nuevoJuego["Matriz"]["matrizJ1"][y][x-1] != 0 or nuevoJuego["Matriz"]["matrizJ1"][y][x-2] != 0:
            return False
        else:
            return True
    elif orientacion == 2:
        if y > filas - 3 or nuevoJuego["Matriz"]["matrizJ1"][y][x] != 0 or nuevoJuego["Matriz"]["matrizJ1"][y+1][x] != 0 or nuevoJuego["Matriz"]["matrizJ1"][y+2][x] != 0:
            return False
        else:
            return True
    elif orientacion == 3:
        if x > columnas - 3 or nuevoJuego["Matriz"]["matrizJ1"][y][x] != 0 or nuevoJuego["Matriz"]["matrizJ1"][y][x+1] != 0 or nuevoJuego["Matriz"]["matrizJ1"][y][x+2] != 0:
            return False
        else:
            return True
    elif orientacion == 4:
        if y < 2 or nuevoJuego["Matriz"]["matrizJ1"][y][x] != 0 or nuevoJuego["Matriz"]["matrizJ1"][y-1][x] != 0 or nuevoJuego["Matriz"]["matrizJ1"][y-2][x] != 0:
            return False
        else:
            return True
        
def validarUbicacionDestructorJ2(x,y,orientacion):
    global nuevoJuego
    if orientacion==1:
        if nuevoJuego["Matriz"]["matrizJ2"][y][x]!=0:
            return False
        else:
            return True

    elif orientacion==2:
        if nuevoJuego["Matriz"]["matrizJ2"][y][x]!=0:
            return False
        else:
            return True

    elif orientacion==3:
        if nuevoJuego["Matriz"]["matrizJ2"][y][x] !=0:
            return False
        else:
            return True
    
    elif orientacion==4:
        if nuevoJuego["Matriz"]["matrizJ2"][y][x] !=0:
            return False
        else:
            return True
    
def validarUbicacionCruceroJ2(x,y,orientacion, fila, columnas):
    global nuevoJuego
    if orientacion == 1:
        if x < 1 or nuevoJuego["Matriz"]["matrizJ2"][y][x] != 0 or nuevoJuego["Matriz"]["matrizJ2"][y][x-1] != 0:
            return False
        else:
            return True
    elif orientacion == 2:
        if y > fila - 2 or nuevoJuego["Matriz"]["matrizJ2"][y][x] != 0 or nuevoJuego["Matriz"]["matrizJ2"][y+1][x] != 0:
            return False
        else:
            return True
    elif orientacion == 3:
        if x > columnas - 2 or nuevoJuego["Matriz"]["matrizJ2"][y][x] != 0 or nuevoJuego["Matriz"]["matrizJ2"][y][x+1] != 0:
            return False
        else:
            return True
    elif orientacion == 4:
        if y < 1 or nuevoJuego["Matriz"]["matrizJ2"][y][x] != 0 or nuevoJuego["Matriz"]["matrizJ2"][y-1][x] != 0:
            return False
        else:
            return True

def validarUbicacionAcorazadoJ2(x,y,orientacion, fila, columna):
    global nuevoJuego
    if orientacion == 1:
        if x < 2 or nuevoJuego["Matriz"]["matrizJ2"][y][x] != 0 or nuevoJuego["Matriz"]["matrizJ2"][y][x-1] != 0 or nuevoJuego["Matriz"]["matrizJ2"][y][x-2] != 0:
            return False
        else:
            return True
    elif orientacion == 2:
        if y > fila - 3 or nuevoJuego["Matriz"]["matrizJ2"][y][x] != 0 or nuevoJuego["Matriz"]["matrizJ2"][y+1][x] != 0 or nuevoJuego["Matriz"]["matrizJ2"][y+2][x] != 0:
            return False
        else:
            return True
    elif orientacion == 3:
        if x > columna - 3 or nuevoJuego["Matriz"]["matrizJ2"][y][x] != 0 or nuevoJuego["Matriz"]["matrizJ2"][y][x+1] != 0 or nuevoJuego["Matriz"]["matrizJ2"][y][x+2] != 0:
            return False
        else:
            return True
    elif orientacion == 4:
        if y < 2 or nuevoJuego["Matriz"]["matrizJ2"][y][x] != 0 or nuevoJuego["Matriz"]["matrizJ2"][y-1][x] != 0 or nuevoJuego["Matriz"]["matrizJ2"][y-2][x] != 0:
            return False
        else:
            return True
        
menu.mainloop()