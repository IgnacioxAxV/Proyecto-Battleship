from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter.font as tkFont
import json

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

def datosPartida():
    global nuevoJuego

    ventana=Toplevel()
    ventana.title("Datos de partida")
    ventana.geometry("410x250+380+280")

    partidaLabel= Label(ventana, text="Inserte el nombre de la partida:")
    partidaLabel.place(x=1,y=1)
    nombrePartidaE= Entry(ventana)
    nombrePartidaE.place(x=270,y=1)
    nuevoJuego["NombrePartida"]=nombrePartidaE.get()

    jugador1Label= Label(ventana, text="Inserte el nombre del primer jugador:")
    jugador1Label.place(x=1,y=30)
    nombreJugador1E= Entry(ventana)
    nombreJugador1E.place(x=270,y=30)
    nuevoJuego["Jugador 1"]["Nombre"]=nombreJugador1E.get()

    nickname1Label= Label(ventana, text="Inserte el nombre del primer jugador:")
    nickname1Label.place(x=1,y=60)
    nickName1E= Entry(ventana)
    nickName1E.place(x=270,y=60)
    nuevoJuego["Jugador 1"]["Nickname"]=nickName1E.get()    

    jugador2Label= Label(ventana, text="Inserte el nombre del segundo jugador:")
    jugador2Label.place(x=1,y=90)
    nombreJugador2E= Entry(ventana)
    nombreJugador2E.place(x=270,y=90)
    nuevoJuego["Jugador 2"]["Nombre"]=nombreJugador2E.get() 

    nickname2Label= Label(ventana, text="Inserte el nombre del segundo jugador:")
    nickname2Label.place(x=1,y=120)
    nickName2E= Entry(ventana)
    nickName2E.place(x=270,y=120)
    nuevoJuego["Jugador 2"]["Nickname"]=nickName2E.get()    

    columnaLabel= Label(ventana, text="Columnas:")
    columnaLabel.place(x=1,y=150)
    seleccionColumnaE= Spinbox(ventana, from_=20, to=40, increment=2)
    seleccionColumnaE.place(x=270,y=150)
    nuevoJuego["Matriz"]["Columnas"]=seleccionColumnaE.get()

    filaLabel= Label(ventana, text="Fila:")
    filaLabel.place(x=1,y=180)
    seleccionFilaE= Spinbox(ventana, from_=10, to=40)
    seleccionFilaE.place(x=270, y=180)
    nuevoJuego["Matriz"]["Filas"]=seleccionFilaE.get()

    botonEmpezar=Button(ventana, text="Empezar",command=lambda: mensaje() and generarMatriz( seleccionColumnaE.get(),seleccionFilaE.get()) and 
                        ubicarDestructor1J1(seleccionColumnaE.get(), seleccionFilaE.get()) and 
                        ventana.destroy())
    botonEmpezar.place(x=310, y=210)

def cargarPartidas():
    listaPartidas=[]
    with open("partidas.json", "r") as archivoJson:
        partidasGuardadas = json.load(archivoJson)

    for p in partidasGuardadas.keys():
        listaPartidas.append(p)

    ventana= Toplevel()
    ventana.title("Partidas guardadas")
    ventana.geometry("300x100+380+280")
    letrero= Label(ventana, text="Seleccione la partida que desees jugar:")
    letrero.place(x=1, y=1)
    seleccionPartida= ttk.Combobox(ventana, values=listaPartidas)
    seleccionPartida.place(x=50, y=30)
    botonGuardar=Button(ventana, text="Seleccionar",command= ventana.destroy())
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

boton1=ttk.Button(menu, text= "Crear partida", command=datosPartida(), style='C.TButton')
boton1.place(x=80 , y=220, width=200, height=130)

boton2=ttk.Button(menu, text= "Cargar partida", command=cargarPartidas(), style='C.TButton')
boton2.place(x=80 , y=430, width=200, height=130)

boton2=ttk.Button(menu, text= "Borrar partidas", command=borrarPartidas(), style='C.TButton')
boton2.place(x=80 , y=640, width=200, height=130)

boton4=ttk.Button(menu, text="Salir", command=menu.destroy, style='C.TButton')
boton4.place(x=1330 , y=30, width=120, height=80)

punto= Label(menu, text="#")
punto.place(x=1525 , y=850)

def datosPartida():
    global nuevoJuego

    ventana=Toplevel()
    ventana.title("Datos de partida")
    ventana.geometry("410x250+380+280")

    partidaLabel= Label(ventana, text="Inserte el nombre de la partida:")
    partidaLabel.place(x=1,y=1)
    nombrePartidaE= Entry(ventana)
    nombrePartidaE.place(x=270,y=1)
    nuevoJuego["NombrePartida"]=nombrePartidaE.get()

    jugador1Label= Label(ventana, text="Inserte el nombre del primer jugador:")
    jugador1Label.place(x=1,y=30)
    nombreJugador1E= Entry(ventana)
    nombreJugador1E.place(x=270,y=30)
    nuevoJuego["Jugador 1"]["Nombre"]=nombreJugador1E.get()

    nickname1Label= Label(ventana, text="Inserte el nombre del primer jugador:")
    nickname1Label.place(x=1,y=60)
    nickName1E= Entry(ventana)
    nickName1E.place(x=270,y=60)
    nuevoJuego["Jugador 1"]["Nickname"]=nickName1E.get()    

    jugador2Label= Label(ventana, text="Inserte el nombre del segundo jugador:")
    jugador2Label.place(x=1,y=90)
    nombreJugador2E= Entry(ventana)
    nombreJugador2E.place(x=270,y=90)
    nuevoJuego["Jugador 2"]["Nombre"]=nombreJugador2E.get() 

    nickname2Label= Label(ventana, text="Inserte el nombre del segundo jugador:")
    nickname2Label.place(x=1,y=120)
    nickName2E= Entry(ventana)
    nickName2E.place(x=270,y=120)
    nuevoJuego["Jugador 2"]["Nickname"]=nickName2E.get()    

    columnaLabel= Label(ventana, text="Columnas:")
    columnaLabel.place(x=1,y=150)
    seleccionColumnaE= Spinbox(ventana, from_=20, to=40, increment=2)
    seleccionColumnaE.place(x=270,y=150)
    nuevoJuego["Matriz"]["Columnas"]=seleccionColumnaE.get()

    filaLabel= Label(ventana, text="Fila:")
    filaLabel.place(x=1,y=180)
    seleccionFilaE= Spinbox(ventana, from_=10, to=40)
    seleccionFilaE.place(x=270, y=180)
    nuevoJuego["Matriz"]["Filas"]=seleccionFilaE.get()

    botonEmpezar=Button(ventana, text="Empezar",command=lambda: mensaje() and generarMatriz( seleccionColumnaE.get(),seleccionFilaE.get()) and
                        ventana.destroy())
    botonEmpezar.place(x=310, y=210)

def mensaje():
    messagebox.showinfo("Battleship", "Ubique los barcos en el tablero.")
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
    print (f"x={x},y={y}")
    global resultadoX
    global resultadoY
    resultadoX=x
    resultadoY=y  

def ubicarDestructor1J1(x,y):
    x=int(x)
    y=int(y)
    global matriz
    tablero=Toplevel()
    tablero.title("Tablero")
    tablero.attributes("-fullscreen", True)

    tableroLabel= Label(tablero, text="Inserte la ubicacion del barco:")
    tableroLabel.place(x=1,y=10)

    orientacion= IntVar()

    botonGuardarPosicion=Button(tablero, text="Guardar",command= lambda: guardarDestructor1J1(resultadoX,resultadoY,orientacion.get (),x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    orientacionLabel= Label(tablero, text="Orientacion del barco:")
    orientacionLabel.place(x=500,y=40)

    orientacionIzquierda=ttk.Radiobutton(tablero, text="Izquierda", value= 1, variable=orientacion)
    orientacionIzquierda.place(x=600, y=60)
    orientacionDerecha=ttk.Radiobutton(tablero, text="Derecha", value=2, variable=orientacion)
    orientacionDerecha.place(x=700, y=60)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Abajo", value=3, variable=orientacion)
    orientacioAbajo.place(x=800, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Arriba", value=4, variable=orientacion)
    orientacionArriba.place(x=900, y=60)

    matriz=[[Button(tablero,bg="blue", command= accion(x,y)) 
            for c in range(x//2)] for f in range(y)]
    
    posicionXmatriz=10
    posicionYmatriz=200
    for fila_botones in matriz:
        posicionXmatriz=10
        for btn in fila_botones:
            btn.place(x=posicionXmatriz,y=posicionYmatriz)
            btn.configure(height=2, width=3)
            posicionXmatriz+=32
        posicionYmatriz+=35
    
    matrizReferencia=[[Button(tablero,bg="yellow") 
            for c in range(x//2)] for f in range(y)]
    
    posicionXmatrizCopia=posicionXmatriz+10
    posicionYmatrizCopia=200

    for fila_botones in matrizReferencia:
        posicionXmatrizCopia=posicionXmatriz+10
        for btn in fila_botones:
            btn.place(x=posicionXmatrizCopia,y=posicionYmatrizCopia)
            btn.configure(height=2, width=3)
            posicionXmatrizCopia+=32
        posicionYmatrizCopia+=35 

def guardarDestructor1J1(x,y,orientacion,co,fi):
    nuevoJuego["BarcosJ1"]["Destructor1J1"]["x1"]=x
    nuevoJuego["BarcosJ1"]["Destructor1J1"]["y1"]=y
    nuevoJuego["BarcosJ1"]["Destructor1J1"]["vida"]=True
    nuevoJuego["BarcosJ1"]["Destructor1J1"]["orientacion"]=orientacion
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

    botonGuardarPosicion=Button(tablero, text="Guardar",command= lambda: guardarDestructor2J1(resultadoX,resultadoY,orientacion.get (),x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    orientacionLabel= Label(tablero, text="Orientacion del barco:")
    orientacionLabel.place(x=500,y=40)

    orientacionIzquierda=ttk.Radiobutton(tablero, text="Izquierda", value= 1, variable=orientacion)
    orientacionIzquierda.place(x=600, y=60)
    orientacionDerecha=ttk.Radiobutton(tablero, text="Derecha", value=2, variable=orientacion)
    orientacionDerecha.place(x=700, y=60)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Abajo", value=3, variable=orientacion)
    orientacioAbajo.place(x=800, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Arriba", value=4, variable=orientacion)
    orientacionArriba.place(x=900, y=60)

    matriz=[[tk.Button(tablero,bg="blue", command=lambda x=c,y=f:accion(x,y)) 
            for c in range(x//2)] for f in range(y)]
    
    posicionXmatriz=10
    posicionYmatriz=200
    for fila_botones in matriz:
        posicionXmatriz=10
        for btn in fila_botones:
            btn.place(x=posicionXmatriz,y=posicionYmatriz)
            btn.configure(height=2, width=3)
            posicionXmatriz+=32
        posicionYmatriz+=35
    
    matrizReferencia=[[tk.Button(tablero,bg="yellow") 
            for c in range(x//2)] for f in range(y)]
    
    posicionXmatrizCopia=posicionXmatriz+10
    posicionYmatrizCopia=200

    for fila_botones in matrizReferencia:
        posicionXmatrizCopia=posicionXmatriz+10
        for btn in fila_botones:
            btn.place(x=posicionXmatrizCopia,y=posicionYmatrizCopia)
            btn.configure(height=2, width=3)
            posicionXmatrizCopia+=32
        posicionYmatrizCopia+=35
    #return True

def guardarDestructor2J1(x,y,orientaciubicarDestructor2J1(co,fi)on,co,fi):
    nuevoJuego["BarcosJ1"]["Destructor2J1"]["x1"]=x
    nuevoJuego["BarcosJ1"]["Destructor2J1"]["y1"]=y
    nuevoJuego["BarcosJ1"]["Destructor2J1"]["vida"]=True
    nuevoJuego["BarcosJ1"]["Destructor2J1"]["orientacion"]=orientacion
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

    botonGuardarPosicion=Button(tablero, text="Guardar",command= lambda:guardarDestructor3J1(resultadoX,resultadoY,orientacion.get(),x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    orientacionLabel= Label(tablero, text="Orientacion del barco:")
    orientacionLabel.place(x=500,y=40)

    orientacionIzquierda=ttk.Radiobutton(tablero, text="Izquierda", value= 1, variable=orientacion)
    orientacionIzquierda.place(x=600, y=60)
    orientacionDerecha=ttk.Radiobutton(tablero, text="Derecha", value=2, variable=orientacion)
    orientacionDerecha.place(x=700, y=60)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Abajo", value=3, variable=orientacion)
    orientacioAbajo.place(x=800, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Arriba", value=4, variable=orientacion)
    orientacionArriba.place(x=900, y=60)

    matriz=[[tk.Button(tablero,bg="blue", command=lambda x=c,y=f:accion(x,y) ) 
            for c in range(x//2)] for f in range(y)]
    
    posicionXmatriz=10
    posicionYmatriz=200
    for fila_botones in matriz:
        posicionXmatriz=10
        for btn in fila_botones:
            btn.place(x=posicionXmatriz,y=posicionYmatriz)
            btn.configure(height=2, width=3)
            posicionXmatriz+=32
        posicionYmatriz+=35
    
    matrizReferencia=[[tk.Button(tablero,bg="yellow") 
            for c in range(x//2)] for f in range(y)]
    
    posicionXmatrizCopia=posicionXmatriz+10
    posicionYmatrizCopia=200

    for fila_botones in matrizReferencia:
        posicionXmatrizCopia=posicionXmatriz+10
        for btn in fila_botones:
            btn.place(x=posicionXmatrizCopia,y=posicionYmatrizCopia)
            btn.configure(height=2, width=3)
            posicionXmatrizCopia+=32
        posicionYmatrizCopia+=35
    return True

def guardarDestructor3J1(x,y,orientacion,co,fi):
    nuevoJuego["BarcosJ1"]["Destructor3J1"]["x1"]=x
    nuevoJuego["BarcosJ1"]["Destructor3J1"]["y1"]=y
    nuevoJuego["BarcosJ1"]["Destructor3J1"]["vida"]=True
    nuevoJuego["BarcosJ1"]["Destructor3J1"]["orientacion"]=orientacion
    ubicarDestructor4J1(co,fi)
    print(nuevoJuego.items())
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

    botonGuardarPosicion=Button(tablero, text="Guardar",command= lambda: guardarDestructor4J1(x,y,orientacion.get ()) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    orientacionLabel= Label(tablero, text="Orientacion del barco:")
    orientacionLabel.place(x=500,y=40)

    orientacionIzquierda=ttk.Radiobutton(tablero, text="Izquierda", value= 1, variable=orientacion)
    orientacionIzquierda.place(x=600, y=60)
    orientacionDerecha=ttk.Radiobutton(tablero, text="Derecha", value=2, variable=orientacion)
    orientacionDerecha.place(x=700, y=60)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Abajo", value=3, variable=orientacion)
    orientacioAbajo.place(x=800, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Arriba", value=4, variable=orientacion)
    orientacionArriba.place(x=900, y=60)

    matriz=[[tk.Button(tablero,bg="blue", command=lambda x=c,y=f:accion(x,y)) 
            for c in range(x//2)] for f in range(y)]
    
    posicionXmatriz=10
    posicionYmatriz=200
    for fila_botones in matriz:
        posicionXmatriz=10
        for btn in fila_botones:
            btn.place(x=posicionXmatriz,y=posicionYmatriz)
            btn.configure(height=2, width=3)
            posicionXmatriz+=32
        posicionYmatriz+=35
    
    matrizReferencia=[[tk.Button(tablero,bg="yellow") 
            for c in range(x//2)] for f in range(y)]
    
    posicionXmatrizCopia=posicionXmatriz+10
    posicionYmatrizCopia=200

    for fila_botones in matrizReferencia:
        posicionXmatrizCopia=posicionXmatriz+10
        for btn in fila_botones:
            btn.place(x=posicionXmatrizCopia,y=posicionYmatrizCopia)
            btn.configure(height=2, width=3)
            posicionXmatrizCopia+=32
        posicionYmatrizCopia+=35
    #return True

def guardarDestructor4J1(x,y,orientacion):
    nuevoJuego["BarcosJ1"]["Destructor4J1"]["x1"]=x
    nuevoJuego["BarcosJ1"]["Destructor4J1"]["y1"]=y
    nuevoJuego["BarcosJ1"]["Destructor4J1"]["vida"]=True
    nuevoJuego["BarcosJ1"]["Destructor4J1"]["orientacion"]=orientacion
    ubicarDestructor5J1(x,y)
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

    botonGuardarPosicion=Button(tablero, text="Guardar",command= lambda:guardarDestructor5J1(resultadoX,resultadoY,orientacion.get (),x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    orientacionLabel= Label(tablero, text="Orientacion del barco:")
    orientacionLabel.place(x=500,y=40)    

    orientacionIzquierda=ttk.Radiobutton(tablero, text="Izquierda", value= 1, variable=orientacion)
    orientacionIzquierda.place(x=600, y=60)
    orientacionDerecha=ttk.Radiobutton(tablero, text="Derecha", value=2, variable=orientacion)
    orientacionDerecha.place(x=700, y=60)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Abajo", value=3, variable=orientacion)
    orientacioAbajo.place(x=800, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Arriba", value=4, variable=orientacion)
    orientacionArriba.place(x=900, y=60)

    matriz=[[tk.Button(tablero,bg="blue", command=lambda x=c,y=f:accion(x,y)) 
            for c in range(x//2)] for f in range(y)]
    
    posicionXmatriz=10
    posicionYmatriz=200
    for fila_botones in matriz:
        posicionXmatriz=10
        for btn in fila_botones:
            btn.place(x=posicionXmatriz,y=posicionYmatriz)
            btn.configure(height=2, width=3)
            posicionXmatriz+=32
        posicionYmatriz+=35
    
    matrizReferencia=[[tk.Button(tablero,bg="yellow") 
            for c in range(x//2)] for f in range(y)]
    
    posicionXmatrizCopia=posicionXmatriz+10
    posicionYmatrizCopia=200

    for fila_botones in matrizReferencia:
        posicionXmatrizCopia=posicionXmatriz+10
        for btn in fila_botones:
            btn.place(x=posicionXmatrizCopia,y=posicionYmatrizCopia)
            btn.configure(height=2, width=3)
            posicionXmatrizCopia+=32
        posicionYmatrizCopia+=35
    return True

def guardarDestructor5J1(x,y,orientacion,co,fi):
    nuevoJuego["BarcosJ1"]["Destructor5J1"]["x1"]=x
    nuevoJuego["BarcosJ1"]["Destructor5J1"]["y1"]=y
    nuevoJuego["BarcosJ1"]["Destructor5J1"]["vida"]=True
    nuevoJuego["BarcosJ1"]["Destructor5J1"]["orientacion"]=orientacion
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

    botonGuardarPosicion=Button(tablero, text="Guardar",command= lambda: guardarDestructor6J1(resultadoX,resultadoY,orientacion.get (),x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    orientacionLabel= Label(tablero, text="Orientacion del barco:")
    orientacionLabel.place(x=500,y=40)

    orientacionIzquierda=ttk.Radiobutton(tablero, text="Izquierda", value= 1, variable=orientacion)
    orientacionIzquierda.place(x=600, y=60)
    orientacionDerecha=ttk.Radiobutton(tablero, text="Derecha", value=2, variable=orientacion)
    orientacionDerecha.place(x=700, y=60)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Abajo", value=3, variable=orientacion)
    orientacioAbajo.place(x=800, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Arriba", value=4, variable=orientacion)
    orientacionArriba.place(x=900, y=60)

    matriz=[[tk.Button(tablero,bg="blue", command=lambda x=c,y=f:accion(x,y))
            for c in range(x//2)] for f in range(y)]
    
    posicionXmatriz=10
    posicionYmatriz=200
    for fila_botones in matriz:
        posicionXmatriz=10
        for btn in fila_botones:
            btn.place(x=posicionXmatriz,y=posicionYmatriz)
            btn.configure(height=2, width=3)
            posicionXmatriz+=32
        posicionYmatriz+=35
    
    matrizReferencia=[[tk.Button(tablero,bg="yellow") 
            for c in range(x//2)] for f in range(y)]
    
    posicionXmatrizCopia=posicionXmatriz+10
    posicionYmatrizCopia=200

    for fila_botones in matrizReferencia:
        posicionXmatrizCopia=posicionXmatriz+10
        for btn in fila_botones:
            btn.place(x=posicionXmatrizCopia,y=posicionYmatrizCopia)
            btn.configure(height=2, width=3)
            posicionXmatrizCopia+=32
        posicionYmatrizCopia+=35
    return True

def guardarDestructor6J1(x,y,orientacion,co,fi):
    nuevoJuego["BarcosJ1"]["Destructor6J1"]["x1"]=x
    nuevoJuego["BarcosJ1"]["Destructor6J1"]["y1"]=y
    nuevoJuego["BarcosJ1"]["Destructor6J1"]["vida"]=True
    nuevoJuego["BarcosJ1"]["Destructor6J1"]["orientacion"]=orientacion
    ubicarCrucero1J1(co,fi)
    return True

print(nuevoJuego.items())
menu.mainloop()