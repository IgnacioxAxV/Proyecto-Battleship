from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter.font as tkFont

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

menu.attributes('-fullscreen', True)
menu.configure(bg="Yellow")
menu.title("Battleship")

titulo= Label(menu, text="Battleship", font=fontStyle)
titulo.place(x=660,y=1)

boton1=ttk.Button(menu, text= "Crear partida", command="funcion", style='C.TButton')
boton1.place(x=80 , y=220, width=200, height=130)

boton2=ttk.Button(menu, text= "Cargar partida", command="funcion", style='C.TButton')
boton2.place(x=80 , y=430, width=200, height=130)

boton2=ttk.Button(menu, text= "Borrar partidas", command="funcion", style='C.TButton')
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

