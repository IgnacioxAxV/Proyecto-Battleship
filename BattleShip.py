from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tkinter.font as tkFont
import json
from PIL import ImageTk, Image

                                                                                            #Diccionario destinado a almacenar todos los datos de la partida
nuevoJuego = {                                          
        "Matriz": {"Columnas": None,"Filas": None, "matrizJ1": [], "matrizJ2": []},
        "NombrePartida": None,
        "Pantalla": 1,
        "Jugador 1": {
            "Nombre": None,
            "Nickname": None,
            "Puntaje": 0,
            "Cantidad Barcos": 12
        },
        
        "Jugador 2": {
            "Nombre":  None,
            "Nickname": None,
            "Puntaje": 0,
            "Cantidad Barcos": 12
        },
        
        "BarcosJ1": {
            "Destructor1J1": {"vida": 1, "x1": None, "y1": None ,"orientacion": None, "disparos":0, "movimiento":1,} ,
            "Destructor2J1": {"vida": 1, "x1": None, "y1": None ,"orientacion": None, "disparos":0, "movimiento":1,} ,
            "Destructor3J1": {"vida": 1, "x1": None, "y1": None ,"orientacion": None, "disparos":0, "movimiento":1,} ,
            "Destructor4J1": {"vida": 1, "x1": None, "y1": None ,"orientacion": None, "disparos":0, "movimiento":1,} ,
            "Destructor5J1": {"vida": 1, "x1": None, "y1": None ,"orientacion": None, "disparos":0, "movimiento":1,} ,
            "Destructor6J1": {"vida": 1, "x1": None, "y1": None ,"orientacion": None, "disparos":0, "movimiento":1,} ,

            "Crucero1J1":  {"vida": 1, "x1": None, "y1": None, "x2": None , "y2": None, "orientacion": None, "disparos":0, "xy1":0, "xy2":0, "movimiento":1,},
            "Crucero2J1":  {"vida": 1, "x1": None, "y1": None, "x2": None , "y2": None, "orientacion": None, "disparos":0, "xy1":0, "xy2":0, "movimiento":1,},
            "Crucero3J1":  {"vida": 1, "x1": None, "y1": None, "x2": None , "y2": None, "orientacion": None, "disparos":0, "xy1":0, "xy2":0, "movimiento":1,},
            "Crucero4J1":  {"vida": 1, "x1": None, "y1": None, "x2": None , "y2": None, "orientacion": None, "disparos":0, "xy1":0, "xy2":0, "movimiento":1,},

            "Acorazado1J1": {"vida": 1, "x1": None, "y1": None,"x2": None, "y2": None,"x3": None, "y3": None, "orientacion": None, "disparos":0, "xy1":0, "xy2":0, "xy3":0, "movimiento":1,},
            "Acorazado2J1": {"vida": 1, "x1": None, "y1": None,"x2": None, "y2": None,"x3": None, "y3": None, "orientacion": None, "disparos":0, "xy1":0, "xy2":0, "xy3":0, "movimiento":1,}
            },

        "BarcosJ2": {                   
            "Destructor1J2": {"vida": 1, "x1": None, "y1": None ,"orientacion": None, "disparos":0, "movimiento":1,},
            "Destructor2J2": {"vida": 1, "x1": None, "y1": None ,"orientacion": None, "disparos":0, "movimiento":1,},
            "Destructor3J2": {"vida": 1, "x1": None, "y1": None ,"orientacion": None, "disparos":0, "movimiento":1,},
            "Destructor4J2": {"vida": 1, "x1": None, "y1": None ,"orientacion": None, "disparos":0, "movimiento":1,},
            "Destructor5J2": {"vida": 1, "x1": None, "y1": None ,"orientacion": None, "disparos":0, "movimiento":1,},
            "Destructor6J2": {"vida": 1, "x1": None, "y1": None ,"orientacion": None, "disparos":0, "movimiento":1,},

            "Crucero1J2":  {"vida": 1, "x1": None, "y1": None, "x2": None , "y2": None, "orientacion": None, "disparos":0, "xy1":0, "xy2":0, "movimiento":1,},
            "Crucero2J2":  {"vida": 1, "x1": None, "y1": None, "x2": None , "y2": None, "orientacion": None, "disparos":0, "xy1":0, "xy2":0, "movimiento":1,},
            "Crucero3J2":  {"vida": 1, "x1": None, "y1": None, "x2": None , "y2": None, "orientacion": None, "disparos":0, "xy1":0, "xy2":0, "movimiento":1,},
            "Crucero4J2":  {"vida": 1, "x1": None, "y1": None, "x2": None , "y2": None, "orientacion": None, "disparos":0, "xy1":0, "xy2":0, "movimiento":1,},

            "Acorazado1J2": {"vida": 1, "x1": None, "y1": None,"x2": None, "y2": None,"x3": None, "y3": None, "orientacion": None, "disparos":0, "xy1":0, "xy2":0, "xy3":0, "movimiento":1,},
            "Acorazado2J2": {"vida": 1, "x1": None, "y1": None,"x2": None, "y2": None,"x3": None, "y3": None, "orientacion": None, "disparos":0, "xy1":0, "xy2":0, "xy3":0, "movimiento":1,},
            }
    }

menu = Tk()                                                                 #Ventana principal
style = ttk.Style()                                                         #Estilos para los botones
style.configure('C.TButton', font=("Bauhaus 93", 18))
style.configure('C.TButton', relief="ridge")
style.configure('C.TButton', width=3)
style.configure('C.TButton', bd=1)
fontStyle = tkFont.Font(family="Lucida Grande", size=40)
                                                                 
resultadoX=0                                                                #Variables globales para almacenar las coordenadas de los botones
resultadoY=0                                                                #Variables globales para almacenar las coordenadas de los botones

matrizJ1 =[]                                                                #Matriz de botones para el jugador 1
matrizJ2 = []                                                               #Matriz de botones para el jugador 2
matrizDisparosJ1 = []                                                       #Matriz de botones para los disparos del jugador 1
matrizDisparosJ2 = []                                                       #Matriz de botones para los disparos del jugador 2
celdasRojasJ1=[]                                                            #Lista para almacenar las tuplas de las celdas rojas del tablero de disparo del jugador 1
celdasRojasJ2=[]                                                            #Lista para almacenar las tuplas de las celdas rojas del tablero de disparo del jugador 2

limitesTablero = []                                                         #Lista para almacenar los limites del tablero

izquierda= 3                                                                #Constantes para las orientaciones de los barcos
derecha= 1
arriba= 2
abajo= 4

def crearPartida():
    """Funcion que solicita los datos iniciales de la partida por medio de widget de la biblioteca tkinter
    """
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

    nickname1Label= Label(ventana, text="Inserte el nickname del primer jugador:")
    nickname1Label.place(x=1,y=60)
    nickName1E= Entry(ventana)
    nickName1E.place(x=270,y=60)  

    jugador2Label= Label(ventana, text="Inserte el nombre del segundo jugador:")
    jugador2Label.place(x=1,y=90)
    nombreJugador2E= Entry(ventana)
    nombreJugador2E.place(x=270,y=90)

    nickname2Label= Label(ventana, text="Inserte el nickname del segundo jugador:")
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
    """Funcion encargada de validar que todos los datos ingresados por el usario sean correctos y no signifiquen problemas mas adelante

    Args:
        nombrePartida (_type_): Nombre de la partida
        nombreJugador1 (_type_): Nombre del jugador 1
        nickname1 (_type_): Nickname del jugador 1
        nombreJugador2 (_type_): Nombre del jugador 2
        nickname2 (_type_): Nickname del jugador 2
        fila (_type_): Cantidad de filas que poseera el tablero de juego
        columna (_type_): Cantidad de columnas que poseera el tablero de juego
        ventana (_type_): Ventana emergente de la funcion anterior

    Returns:
        bool: Retorna un valor booleano para dirigir el avance del proceso de juego
    """
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
    
    if nombrePartida in listaPartidas:                                                              #Mensajes que le dicen al usario por qué el ingreso de datos a tenido problemas
        messagebox.showerror("Error", "El nombre de la partida ya existe, intenta de nuevo")
        ventana.destroy()
        return False
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
    """Funcion que actualiza los valores de las claves del diccionario

    Args:
        nombrePartida (_type_): Nombre de la partida
        nombreJugador1 (_type_): Nombre del jugador 1
        nickname1 (_type_): Nickname del jugador 1
        nombreJugador2 (_type_): Nombre del jugador 2
        nickname2 (_type_): Nickname del jugador 2
        fila (_type_): Cantidad de filas que poseera el tablero de juego
        columna (_type_): Cantidad de columnas que poseera el tablero de juego

    Returns:
        bool: Retorna un valor booleano para dirigir el avance del proceso de juego
    """
    global nuevoJuego
    nuevoJuego["NombrePartida"]=nombrePartida
    nuevoJuego["Jugador 1"]["Nombre"]=nombreJugador1
    nuevoJuego["Jugador 1"]["Nickname"]=nickname1
    nuevoJuego["Jugador 2"]["Nombre"]=nombreJugador2
    nuevoJuego["Jugador 2"]["Nickname"]=nickname2
    nuevoJuego["Matriz"]["Columnas"]=int(columna)
    nuevoJuego["Matriz"]["Filas"]=int(fila)
    return True

def guardarDatos(nombrePartida):
    """Funcion que actualiza los datos que posee el archivo json que se utilizo para el almacenado de los datos del juego

    Args:
        nombrePartida (_type_): Nombre clave que se le asignara al diccionario que almacenará todos los datos del juego

    Returns:
        bool: Retorna un valor booleano para dirigir el avance del proceso de juego
    """
    global nuevoJuego
    
    try:
        with open("partidas.json", "r") as archivoJson:
            datosExistentes = json.load(archivoJson)
    except FileNotFoundError:
        datosExistentes = {}

    datosExistentes[nombrePartida] = nuevoJuego

    with open("partidas.json", "w") as archivoJson:
        json.dump(datosExistentes, archivoJson, indent=4)
    
    return True

def cargarPartidas():
    """Funcion que le muestra las partidas almacenadas del juego a los usarios, dando disponibilidad a seleccionar una de estas para cargarlas
    """
    listaPartidas=[]                                                    #Lista que se le ingresaran el nombre de partidas almacenadas
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
    botonGuardar=Button(ventana, text="Seleccionar",command= lambda: sobreEscribirDiccionario(seleccionPartida.get()) and pantallaDoble() and ventana.destroy())
    botonGuardar.place(x=220, y=70)

def sobreEscribirDiccionario(seleccionPartida):
    """Funcion que reasigna todos los valores del diccionario de la partida por datos almacenados de una partida pasada dentro de un archivo json, estas partidas las puede seleccionar el jugador a criterio propio

    Args:
        seleccionPartida (_type_): Partida seleccionada por los jugadores

    Returns:
        bool: Retorna un valor booleano para dirigir el avance del proceso de juego
    """
    global nuevoJuego
    
    try:
        with open("partidas.json", "r") as archivoJson:
            partidasGuardadas = json.load(archivoJson)
    except FileNotFoundError:
        with open("partidas.json", "w") as archivoJson:
            json.dump({}, archivoJson)
        partidasGuardadas = {}

    nuevoJuego=partidasGuardadas[seleccionPartida]
    
    
    return True

def borrarPartidas():
    """Funcion que limpia el archivo json que almacena datos de partidas pasadas
    """
    with open("partidas.json", "r") as archivoJson:
        partidasGuardadas = json.load(archivoJson)
    partidasGuardadas.clear()
    with open("partidas.json", "w") as archivoJson:
        json.dump(partidasGuardadas, archivoJson, indent=4)

menu.attributes('-fullscreen', True)                                                    #Se define la ventana del menu para pantalla completa
menu.configure(bg="Yellow")

menu.title("Battleship")                                                                #Se define el fondo de la ventana de menu

titulo= Label(menu, text="Battleship", font=fontStyle)                                  
titulo.place(x=660,y=1)

boton1=ttk.Button(menu, text= "Crear partida", command=crearPartida, style='C.TButton') #Se asignan diversos botones al menu
boton1.place(x=80 , y=220, width=200, height=130)

boton2=ttk.Button(menu, text= "Cargar partida", command= cargarPartidas, style='C.TButton')
boton2.place(x=80 , y=430, width=200, height=130)

boton2=ttk.Button(menu, text= "Borrar partidas", command=borrarPartidas, style='C.TButton')
boton2.place(x=80 , y=640, width=200, height=130)

boton4=ttk.Button(menu, text="Salir", command=menu.destroy, style='C.TButton')
boton4.place(x=1330 , y=30, width=120, height=80)

punto= Label(menu, text="#")
punto.place(x=1525 , y=850)

def borrarClave(nombrePartida:str):
    """Funcion que borra la partida finalizada del archivo json

    Args:
        nombrePartida (str): nombre de la partida que se borrará
    """
    try:
        with open("partidas.json", "r") as archivoJson:
            partidasGuardadas = json.load(archivoJson)
    except FileNotFoundError:
        with open("partidas.json", "w") as archivoJson:
            json.dump({}, archivoJson)
        partidasGuardadas = {}

    if nombrePartida in partidasGuardadas:
        del partidasGuardadas[nombrePartida]

        with open("partidas.json", "w") as archivoJson:  # Escribir los cambios de vuelta al archivo
            json.dump(partidasGuardadas, archivoJson)
        return True
    return True

    

def mensaje():
    """Mensaje emergente que le indica al jugador que su datos han sido ingresados correctamente

    Returns:
        bool: Retorna un valor booleano para dirigir el avance del proceso de juego
    """
    messagebox.showinfo("Battleship", "Tus datos han sido ingresados correctamente")
    return True 

def generarMatriz(x,y):
    """Genera una matriz de ceros que se tomara como referencia en el ingreso de barcos de los jugadores

    Args:
        x (_type_): recorrido por columnas en la matriz
        y (_type_): recorrido por filas en la matriz

    Returns:
        bool:Retorna un valor booleano para dirigir el avance del proceso de juego
    """
    x=int(x)
    y=int(y)
    global nuevoJuego
    nuevoJuego["Matriz"]["matrizJ1"]=[[0 for c in range(x//2)] for f in range(y)]
    nuevoJuego["Matriz"]["matrizJ2"]=[[0 for c in range(x//2)] for f in range(y)]
    return True

def cambiarCursor(event):
    """Funcion que cambia el puntero del mouse si esta dentro de la ventana

    Args:
        event (_type_): _description_
    """
    menu.config(cursor="hand2")

def restaurarCursor(event):
    """Funcion que cambia el puntero del mouse al salir de la ventana menu

    Args:
        event (_type_): _description_
    """
    menu.config(cursor="")

menu.bind("<Enter>", cambiarCursor)

menu.bind("<Leave>", restaurarCursor)

def accion(x,y):
    """Funcion que reasiga los valores de una variable, estas sirven para el ingreso de los barcos del juego

    Args:
        x (_type_): Valor de la columna del boton
        y (_type_): Valor de la fila del boton
    """
    global resultadoX
    global resultadoY
    resultadoX=x
    resultadoY=y  


def configurarBoton(btn, num):
    """Funcion que configura la imagen de los botones de las matrices de los jugadores segun un numero que indica la orientacion de las naves de los jugadoes

    Args:
        btn (_type_): boton de tk
        num (_type_): numero que representa la orientacion del barco
    """
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
    """Funcion que imprime el tablero que servira de ayuda para que el jugador 1 ingrese sus barcos a los tableros

    Args:
        x (_type_): Largo de ccolumnas
        y (_type_): Largo de filas
        tablero (_type_): ventana que llega por parametro
    """
    labelGuia= Label(tablero, text="Guia de colocación de barcos")
    labelGuia.place(x=800,y=10)

    labelGuia1= Label(tablero, image= imagenGuia1)
    labelGuia1.place(x=800,y=30)

    LabelGuia2= Label(tablero, image= imagenGuia2)
    LabelGuia2.place(x=950,y=30)

    labelGuia3= Label(tablero, image= imagenGuia3)
    labelGuia3.place(x=1100,y=30)

    labelGuia4= Label(tablero, image= imagenGuia4)
    labelGuia4.place(x=1250,y=30)

    matrizBotonesJ1=[[Button(tablero,bg="blue", command=lambda x=c,y=f:accion(x,y)) 
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

    global matrizJ1 
    matrizJ1=matrizBotonesJ1

def imprimirMatrizJ2(x,y,tablero):
    """Funcion que imprime el tablero que servira de ayuda para que el jugador 2 ingrese sus barcos a los tableros

    Args:
        x (_type_): Largo de ccolumnas
        y (_type_): Largo de filas
        tablero (_type_): ventana que llega por parametro
        """
    labelGuia= Label(tablero, text="Guia de colocación de barcos")
    labelGuia.place(x=800,y=10)

    labelGuia1= Label(tablero, image= imagenGuia1)
    labelGuia1.place(x=800,y=30)

    labelGuia2= Label(tablero, image= imagenGuia2)
    labelGuia2.place(x=950,y=30)

    labelGuia3= Label(tablero, image= imagenGuia3)
    labelGuia3.place(x=1100,y=30)

    labelGuia4= Label(tablero, image= imagenGuia4)
    labelGuia4.place(x=1250,y=30)

    
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

    matrizBotonesJ2=[[Button(tablero, bg="blue", command=lambda x=co,y=fi:accion(x,y)) 
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
    
    global matrizJ2
    matrizJ2=matrizBotonesJ2

def ubicarDestructor1J1(x,y):
    """Funcion que solicita la ubicacion de un descructor del jugador 1

    Args:
        x (_type_): Valores del numero de columnas
        y (_type_): Valores del numero de filas
    """
    x=int(x)
    y=int(y)
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
    orientacionDerecha.place(x=600, y=90)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=700, y=90)
    
    imprimirMatrizJ1(x,y,tablero) 

def guardarDestructor1J1(x,y,orientacion,co,fi):
    """Funcion que guarda en el diccionario la ubicacion del desctructor del jugador 1

    Args:
        x (_type_): ubicacion del elemento dentro de las columnas
        y (_type_): _description_ ubicacion del elemento de las filas
        orientacion (_type_): orientacion del barco
        co (_type_): Valores del numero de columnas
        fi (_type_): Valores del numero de filas

    Returns:
        bool:Retorna un valor booleano para dirigir el avance del proceso de juego
    """
    global nuevoJuego
    nuevoJuego["BarcosJ1"]["Destructor1J1"]["x1"]=x
    nuevoJuego["BarcosJ1"]["Destructor1J1"]["y1"]=y
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
    """Funcion que solicita la ubicacion de un descructor del jugador 1

    Args:
        x (_type_): Valores del numero de columnas
        y (_type_): Valores del numero de filas
    """
    x=int(x)
    y=int(y)
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
    orientacionDerecha.place(x=600, y=90)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=700, y=90)

    imprimirMatrizJ1(x,y,tablero)

def guardarDestructor2J1(x,y,orientacion,co,fi):
    """Funcion que guarda en el diccionario la ubicacion del desctructor del jugador 1

    Args:
        x (_type_): ubicacion del elemento dentro de las columnas
        y (_type_): _description_ ubicacion del elemento de las filas
        orientacion (_type_): orientacion del barco
        co (_type_): Valores del numero de columnas
        fi (_type_): Valores del numero de filas

    Returns:
        bool:Retorna un valor booleano para dirigir el avance del proceso de juego
    """
    global nuevoJuego
    nuevoJuego["BarcosJ1"]["Destructor2J1"]["x1"]=x
    nuevoJuego["BarcosJ1"]["Destructor2J1"]["y1"]=y
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
    """Funcion que solicita la ubicacion de un descructor del jugador 1

    Args:
        x (_type_): Valores del numero de columnas
        y (_type_): Valores del numero de filas
    """
    x=int(x)
    y=int(y)
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
    orientacionDerecha.place(x=600, y=90)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=700, y=90)
    
    imprimirMatrizJ1(x,y,tablero)

def guardarDestructor3J1(x,y,orientacion,co,fi):
    """Funcion que guarda en el diccionario la ubicacion del desctructor del jugador 1

    Args:
        x (_type_): ubicacion del elemento dentro de las columnas
        y (_type_): _description_ ubicacion del elemento de las filas
        orientacion (_type_): orientacion del barco
        co (_type_): Valores del numero de columnas
        fi (_type_): Valores del numero de filas

    Returns:
        bool:Retorna un valor booleano para dirigir el avance del proceso de juego
    """
    global nuevoJuego
    nuevoJuego["BarcosJ1"]["Destructor3J1"]["x1"]=x
    nuevoJuego["BarcosJ1"]["Destructor3J1"]["y1"]=y
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
    """Funcion que solicita la ubicacion de un descructor del jugador 1

    Args:
        x (_type_): Valores del numero de columnas
        y (_type_): Valores del numero de filas
    """
    x=int(x)
    y=int(y)
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
    orientacionDerecha.place(x=600, y=90)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=700, y=90)
    
    imprimirMatrizJ1(x,y,tablero)

def guardarDestructor4J1(x,y,orientacion,co,fi):
    """Funcion que guarda en el diccionario la ubicacion del desctructor del jugador 1

    Args:
        x (_type_): ubicacion del elemento dentro de las columnas
        y (_type_): _description_ ubicacion del elemento de las filas
        orientacion (_type_): orientacion del barco
        co (_type_): Valores del numero de columnas
        fi (_type_): Valores del numero de filas

    Returns:
        bool:Retorna un valor booleano para dirigir el avance del proceso de juego
    """
    global nuevoJuego
    nuevoJuego["BarcosJ1"]["Destructor4J1"]["x1"]=x
    nuevoJuego["BarcosJ1"]["Destructor4J1"]["y1"]=y
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
    """Funcion que solicita la ubicacion de un descructor del jugador 1

    Args:
        x (_type_): Valores del numero de columnas
        y (_type_): Valores del numero de filas
    """
    x=int(x)
    y=int(y)
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
    orientacionDerecha.place(x=600, y=90)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=700, y=90)
    
    imprimirMatrizJ1(x,y,tablero)

def guardarDestructor5J1(x,y,orientacion,co,fi):
    """Funcion que guarda en el diccionario la ubicacion del desctructor del jugador 1

    Args:
        x (_type_): ubicacion del elemento dentro de las columnas
        y (_type_): _description_ ubicacion del elemento de las filas
        orientacion (_type_): orientacion del barco
        co (_type_): Valores del numero de columnas
        fi (_type_): Valores del numero de filas

    Returns:
        bool:Retorna un valor booleano para dirigir el avance del proceso de juego
    """
    global nuevoJuego
    nuevoJuego["BarcosJ1"]["Destructor5J1"]["x1"]=x
    nuevoJuego["BarcosJ1"]["Destructor5J1"]["y1"]=y
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
    """Funcion que solicita la ubicacion de un descructor del jugador 1

    Args:
        x (_type_): Valores del numero de columnas
        y (_type_): Valores del numero de filas
    """
    x=int(x)
    y=int(y)
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
    orientacionDerecha.place(x=600, y=90)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=700, y=90)
    
    imprimirMatrizJ1(x,y,tablero)

def guardarDestructor6J1(x,y,orientacion,co,fi):
    """Funcion que guarda en el diccionario la ubicacion del desctructor del jugador 1

    Args:
        x (_type_): ubicacion del elemento dentro de las columnas
        y (_type_): _description_ ubicacion del elemento de las filas
        orientacion (_type_): orientacion del barco
        co (_type_): Valores del numero de columnas
        fi (_type_): Valores del numero de filas

    Returns:
        bool:Retorna un valor booleano para dirigir el avance del proceso de juego
    """
    global nuevoJuego
    nuevoJuego["BarcosJ1"]["Destructor6J1"]["x1"]=x
    nuevoJuego["BarcosJ1"]["Destructor6J1"]["y1"]=y
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
    """Funcion que solicita la ubicacion de un crucero del jugador 1

    Args:
        x (_type_): Valores del numero de columnas
        y (_type_): Valores del numero de filas
    """
    x=int(x)
    y=int(y)
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
    orientacionDerecha.place(x=600, y=90)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=700, y=90)
    
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
    """Funcion que guarda en el diccionario la ubicacion del desctructor del jugador 1

    Args:
        x (_type_): ubicacion del elemento dentro de las columnas
        y (_type_): _description_ ubicacion del elemento de las filas
        orientacion (_type_): orientacion del barco
        co (_type_): Valores del numero de columnas
        fi (_type_): Valores del numero de filas

    Returns:
        bool:Retorna un valor booleano para dirigir el avance del proceso de juego
    """
    global nuevoJuego
    nuevoJuego["BarcosJ1"]["Crucero1J1"]["x1"]=x
    nuevoJuego["BarcosJ1"]["Crucero1J1"]["y1"]=y

    if orientacion==1:
        nuevoJuego["BarcosJ1"]["Crucero1J1"]["x2"]=x-1
        nuevoJuego["BarcosJ1"]["Crucero1J1"]["y2"]=y
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=5
        nuevoJuego["Matriz"]["matrizJ1"][y][x-1]=9

    elif orientacion==2:
        nuevoJuego["BarcosJ1"]["Crucero1J1"]["x2"]=x
        nuevoJuego["BarcosJ1"]["Crucero1J1"]["y2"]=y+1
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=6
        nuevoJuego["Matriz"]["matrizJ1"][y+1][x]=10

    elif orientacion==3:
        nuevoJuego["BarcosJ1"]["Crucero1J1"]["y2"]=y
        nuevoJuego["BarcosJ1"]["Crucero1J1"]["x2"]=x+1
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=7
        nuevoJuego["Matriz"]["matrizJ1"][y][x+1]=11

    elif orientacion==4:
        nuevoJuego["BarcosJ1"]["Crucero1J1"]["y2"]=y-1
        nuevoJuego["BarcosJ1"]["Crucero1J1"]["x2"]=x
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=8
        nuevoJuego["Matriz"]["matrizJ1"][y-1][x]=12

    nuevoJuego["BarcosJ1"]["Crucero1J1"]["orientacion"]=orientacion
     
    ubicarCrucero2J1(co,fi) 
    return True

def ubicarCrucero2J1(x,y):
    """Funcion que solicita la ubicacion de un crucero del jugador 1

    Args:
        x (_type_): Valores del numero de columnas
        y (_type_): Valores del numero de filas
    """
    x=int(x)
    y=int(y)
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
    orientacionDerecha.place(x=600, y=90)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=700, y=90)
    
    imprimirMatrizJ1(x,y,tablero)

def guardarCrucero2J1(x,y,orientacion,co,fi):
    """Funcion que guarda en el diccionario la ubicacion del desctructor del jugador 1

    Args:
        x (_type_): ubicacion del elemento dentro de las columnas
        y (_type_): _description_ ubicacion del elemento de las filas
        orientacion (_type_): orientacion del barco
        co (_type_): Valores del numero de columnas
        fi (_type_): Valores del numero de filas

    Returns:
        bool:Retorna un valor booleano para dirigir el avance del proceso de juego
    """
    global nuevoJuego
    nuevoJuego["BarcosJ1"]["Crucero2J1"]["x1"]=x
    nuevoJuego["BarcosJ1"]["Crucero2J1"]["y1"]=y

    if orientacion==1:
        nuevoJuego["BarcosJ1"]["Crucero2J1"]["x2"]=x-1
        nuevoJuego["BarcosJ1"]["Crucero2J1"]["y2"]=y
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=5
        nuevoJuego["Matriz"]["matrizJ1"][y][x-1]=9

    elif orientacion==2:
        nuevoJuego["BarcosJ1"]["Crucero2J1"]["x2"]=x
        nuevoJuego["BarcosJ1"]["Crucero2J1"]["y2"]=y+1
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=6
        nuevoJuego["Matriz"]["matrizJ1"][y+1][x]=10

    elif orientacion==3:
        nuevoJuego["BarcosJ1"]["Crucero2J1"]["y2"]=y
        nuevoJuego["BarcosJ1"]["Crucero2J1"]["x2"]=x+1
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=7
        nuevoJuego["Matriz"]["matrizJ1"][y][x+1]=11

    elif orientacion==4:
        nuevoJuego["BarcosJ1"]["Crucero2J1"]["y2"]=y-1
        nuevoJuego["BarcosJ1"]["Crucero2J1"]["x2"]=x
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=8 
        nuevoJuego["Matriz"]["matrizJ1"][y-1][x]=12

    nuevoJuego["BarcosJ1"]["Crucero2J1"]["orientacion"]=orientacion

    ubicarCrucero3J1(co,fi) 
    return True

def ubicarCrucero3J1(x,y):
    """Funcion que solicita la ubicacion de un crucero del jugador 1

    Args:
        x (_type_): Valores del numero de columnas
        y (_type_): Valores del numero de filas
    """
    x=int(x)
    y=int(y)
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
    orientacionDerecha.place(x=600, y=90)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=700, y=90)
    
    imprimirMatrizJ1(x,y,tablero)

def guardarCrucero3J1(x,y,orientacion,co,fi):
    """Funcion que guarda en el diccionario la ubicacion del desctructor del jugador 1

    Args:
        x (_type_): ubicacion del elemento dentro de las columnas
        y (_type_): _description_ ubicacion del elemento de las filas
        orientacion (_type_): orientacion del barco
        co (_type_): Valores del numero de columnas
        fi (_type_): Valores del numero de filas

    Returns:
        bool:Retorna un valor booleano para dirigir el avance del proceso de juego
    """
    global nuevoJuego
    nuevoJuego["BarcosJ1"]["Crucero3J1"]["x1"]=x
    nuevoJuego["BarcosJ1"]["Crucero3J1"]["y1"]=y

    if orientacion==1:
        nuevoJuego["BarcosJ1"]["Crucero3J1"]["x2"]=x-1
        nuevoJuego["BarcosJ1"]["Crucero3J1"]["y2"]=y
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=5
        nuevoJuego["Matriz"]["matrizJ1"][y][x-1]=9

    elif orientacion==2:
        nuevoJuego["BarcosJ1"]["Crucero3J1"]["x2"]=x
        nuevoJuego["BarcosJ1"]["Crucero3J1"]["y2"]=y+1
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=6
        nuevoJuego["Matriz"]["matrizJ1"][y+1][x]=10

    elif orientacion==3:
        nuevoJuego["BarcosJ1"]["Crucero3J1"]["y2"]=y
        nuevoJuego["BarcosJ1"]["Crucero3J1"]["x2"]=x+1
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=7
        nuevoJuego["Matriz"]["matrizJ1"][y][x+1]=11

    elif orientacion==4:
        nuevoJuego["BarcosJ1"]["Crucero3J1"]["y2"]=y-1
        nuevoJuego["BarcosJ1"]["Crucero3J1"]["x2"]=x
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=8
        nuevoJuego["Matriz"]["matrizJ1"][y-1][x]=12

    nuevoJuego["BarcosJ1"]["Crucero3J1"]["orientacion"]=orientacion

    ubicarCrucero4J1(co,fi)
    return True

def ubicarCrucero4J1(x,y):
    """Funcion que solicita la ubicacion de un crucero del jugador 1

    Args:
        x (_type_): Valores del numero de columnas
        y (_type_): Valores del numero de filas
    """
    x=int(x)
    y=int(y)
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
    orientacionDerecha.place(x=600, y=90)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=700, y=90)
    
    imprimirMatrizJ1(x,y,tablero)

def guardarCrucero4J1(x,y,orientacion,co,fi):
    """Funcion que guarda en el diccionario la ubicacion del desctructor del jugador 1

    Args:
        x (_type_): ubicacion del elemento dentro de las columnas
        y (_type_): _description_ ubicacion del elemento de las filas
        orientacion (_type_): orientacion del barco
        co (_type_): Valores del numero de columnas
        fi (_type_): Valores del numero de filas

    Returns:
        bool:Retorna un valor booleano para dirigir el avance del proceso de juego
    """
    global nuevoJuego
    nuevoJuego["BarcosJ1"]["Crucero4J1"]["x1"]=x
    nuevoJuego["BarcosJ1"]["Crucero4J1"]["y1"]=y

    if orientacion==1:
        nuevoJuego["BarcosJ1"]["Crucero4J1"]["x2"]=x-1
        nuevoJuego["BarcosJ1"]["Crucero4J1"]["y2"]=y
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=5
        nuevoJuego["Matriz"]["matrizJ1"][y][x-1]=9

    elif orientacion==2:
        nuevoJuego["BarcosJ1"]["Crucero4J1"]["x2"]=x
        nuevoJuego["BarcosJ1"]["Crucero4J1"]["y2"]=y+1
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=6
        nuevoJuego["Matriz"]["matrizJ1"][y+1][x]=10

    elif orientacion==3:
        nuevoJuego["BarcosJ1"]["Crucero4J1"]["y2"]=y
        nuevoJuego["BarcosJ1"]["Crucero4J1"]["x2"]=x+1
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=7
        nuevoJuego["Matriz"]["matrizJ1"][y][x+1]=11

    elif orientacion==4:
        nuevoJuego["BarcosJ1"]["Crucero4J1"]["y2"]=y-1
        nuevoJuego["BarcosJ1"]["Crucero4J1"]["x2"]=x
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=8 
        nuevoJuego["Matriz"]["matrizJ1"][y-1][x]=12

    nuevoJuego["BarcosJ1"]["Crucero4J1"]["orientacion"]=orientacion
    ubicarAcorazado1J1(co,fi)
    return True

def ubicarAcorazado1J1(x,y):
    """Funcion que solicita la ubicacion de un a del jugador 1

    Args:
        x (_type_): Valores del numero de columnas
        y (_type_): Valores del numero de filas
    """
    x=int(x)
    y=int(y)
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
    orientacionDerecha.place(x=600, y=90)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=700, y=90)
    
    imprimirMatrizJ1(x,y,tablero)

def guardarAcorazado1J1(x,y,orientacion,co,fi):
    """Funcion que guarda en el diccionario la ubicacion del desctructor del jugador 1

    Args:
        x (_type_): ubicacion del elemento dentro de las columnas
        y (_type_): _description_ ubicacion del elemento de las filas
        orientacion (_type_): orientacion del barco
        co (_type_): Valores del numero de columnas
        fi (_type_): Valores del numero de filas

    Returns:
        bool:Retorna un valor booleano para dirigir el avance del proceso de juego
    """
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
        nuevoJuego["BarcosJ1"]["Acorazado1J1"]["x2"]=x
        nuevoJuego["BarcosJ1"]["Acorazado1J1"]["y2"]=y+1
        nuevoJuego["BarcosJ1"]["Acorazado1J1"]["x3"]=x
        nuevoJuego["BarcosJ1"]["Acorazado1J1"]["y3"]=y+2
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=14
        nuevoJuego["Matriz"]["matrizJ1"][y+1][x]=18
        nuevoJuego["Matriz"]["matrizJ1"][y+2][x]=22

    elif orientacion==3:
        nuevoJuego["BarcosJ1"]["Acorazado1J1"]["y2"]=y
        nuevoJuego["BarcosJ1"]["Acorazado1J1"]["x2"]=x+1
        nuevoJuego["BarcosJ1"]["Acorazado1J1"]["y3"]=y
        nuevoJuego["BarcosJ1"]["Acorazado1J1"]["x3"]=x+2
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

    nuevoJuego["BarcosJ1"]["Acorazado1J1"]["orientacion"]=orientacion
    ubicarAcorazado2J1(co,fi)   
    return True

def ubicarAcorazado2J1(x,y):
    """Funcion que solicita la ubicacion de un acorazado del jugador 1

    Args:
        x (_type_): Valores del numero de columnas
        y (_type_): Valores del numero de filas
    """
    x=int(x)
    y=int(y)
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
    orientacionDerecha.place(x=600, y=90)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=700, y=90)
    
    imprimirMatrizJ1(x,y,tablero)

def guardarAcorazado2J1(x,y,orientacion,co,fi):
    """Funcion que guarda en el diccionario la ubicacion del desctructor del jugador 1

    Args:
        x (_type_): ubicacion del elemento dentro de las columnas
        y (_type_): _description_ ubicacion del elemento de las filas
        orientacion (_type_): orientacion del barco
        co (_type_): Valores del numero de columnas
        fi (_type_): Valores del numero de filas

    Returns:
        bool:Retorna un valor booleano para dirigir el avance del proceso de juego
    """
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
        nuevoJuego["BarcosJ1"]["Acorazado2J1"]["x2"]=x
        nuevoJuego["BarcosJ1"]["Acorazado2J1"]["y2"]=y+1
        nuevoJuego["BarcosJ1"]["Acorazado2J1"]["x3"]=x
        nuevoJuego["BarcosJ1"]["Acorazado2J1"]["y3"]=y+2
        nuevoJuego["Matriz"]["matrizJ1"][y][x]=14
        nuevoJuego["Matriz"]["matrizJ1"][y+1][x]=18
        nuevoJuego["Matriz"]["matrizJ1"][y+2][x]=22

    elif orientacion==3:
        nuevoJuego["BarcosJ1"]["Acorazado2J1"]["y2"]=y
        nuevoJuego["BarcosJ1"]["Acorazado2J1"]["x2"]=x+1
        nuevoJuego["BarcosJ1"]["Acorazado2J1"]["y3"]=y
        nuevoJuego["BarcosJ1"]["Acorazado2J1"]["x3"]=x+2
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

    nuevoJuego["BarcosJ1"]["Acorazado2J1"]["orientacion"]=orientacion
    pantallaBarcosJ1(co,fi)
    return True

def pantallaBarcosJ1(x,y):
    """Funcion que muestra la ubicacion de los barcos del jugador 1

    Args:
        x (_type_): Valores del numero de columnas
        y (_type_): Valores del numero de filas
    """
    x=int(x)
    y=int(y)
    tablero=tk.Toplevel()
    tablero.title("Tablero")
    tablero.attributes("-fullscreen", True)

    tableroLabel= Label(tablero, text="Barcos del jugador 1")
    tableroLabel.place(x=1,y=10)

    botonGuardarPosicion=Button(tablero, text="Continuar",command= lambda:ubicarDestructor1J2(x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    imprimirMatrizJ1(x,y,tablero)


def ubicarDestructor1J2(x,y):
    """Funcion que solicita la ubicacion de un descructor del jugador 2

    Args:
        x (_type_): Valores del numero de columnas
        y (_type_): Valores del numero de filas
    """
    x=int(x)
    y=int(y)
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
    orientacionDerecha.place(x=600, y=90)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=700, y=90)
        
    imprimirMatrizJ2(x,y,tablero)

    return True

def guardarDestructor1J2(x,y,orientacion,co,fi):
    """Funcion que guarda en el diccionario la ubicacion del desctructor del jugador 2

    Args:
        x (_type_): ubicacion del elemento dentro de las columnas
        y (_type_): _description_ ubicacion del elemento de las filas
        orientacion (_type_): orientacion del barco
        co (_type_): Valores del numero de columnas
        fi (_type_): Valores del numero de filas

    Returns:
        bool:Retorna un valor booleano para dirigir el avance del proceso de juego
    """
    global nuevoJuego
    nuevoJuego["BarcosJ2"]["Destructor1J2"]["x1"]=x
    nuevoJuego["BarcosJ2"]["Destructor1J2"]["y1"]=y
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
    """Funcion que solicita la ubicacion de un descructor del jugador 2

    Args:
        x (_type_): Valores del numero de columnas
        y (_type_): Valores del numero de filas
    """
    x=int(x)
    y=int(y)
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
    orientacionDerecha.place(x=600, y=90)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=700, y=90)
    
    imprimirMatrizJ2(x,y,tablero)

def guardarDestructor2J2(x,y,orientacion,co,fi):
    """Funcion que guarda en el diccionario la ubicacion del desctructor del jugador 2

    Args:
        x (_type_): ubicacion del elemento dentro de las columnas
        y (_type_): _description_ ubicacion del elemento de las filas
        orientacion (_type_): orientacion del barco
        co (_type_): Valores del numero de columnas
        fi (_type_): Valores del numero de filas

    Returns:
        bool:Retorna un valor booleano para dirigir el avance del proceso de juego
    """
    global nuevoJuego
    nuevoJuego["BarcosJ2"]["Destructor2J2"]["x1"]=x
    nuevoJuego["BarcosJ2"]["Destructor2J2"]["y1"]=y
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
    """Funcion que solicita la ubicacion de un descructor del jugador 2

    Args:
        x (_type_): Valores del numero de columnas
        y (_type_): Valores del numero de filas
    """
    x=int(x)
    y=int(y)
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
    orientacionDerecha.place(x=600, y=90)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=700, y=90)
    
    imprimirMatrizJ2(x,y,tablero)

def guardarDestructor3J2(x,y,orientacion,co,fi):
    """Funcion que guarda en el diccionario la ubicacion del desctructor del jugador 2

    Args:
        x (_type_): ubicacion del elemento dentro de las columnas
        y (_type_): _description_ ubicacion del elemento de las filas
        orientacion (_type_): orientacion del barco
        co (_type_): Valores del numero de columnas
        fi (_type_): Valores del numero de filas

    Returns:
        bool:Retorna un valor booleano para dirigir el avance del proceso de juego
    """
    global nuevoJuego
    nuevoJuego["BarcosJ2"]["Destructor3J2"]["x1"]=x
    nuevoJuego["BarcosJ2"]["Destructor3J2"]["y1"]=y
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
    """Funcion que solicita la ubicacion de un descructor del jugador 2

    Args:
        x (_type_): Valores del numero de columnas
        y (_type_): Valores del numero de filas
    """
    x=int(x)
    y=int(y)
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
    orientacionDerecha.place(x=600, y=90)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=700, y=90)
    
    imprimirMatrizJ2(x,y,tablero)

def guardarDestructor4J2(x,y,orientacion,co,fi):
    """Funcion que guarda en el diccionario la ubicacion del desctructor del jugador 2

    Args:
        x (_type_): ubicacion del elemento dentro de las columnas
        y (_type_): _description_ ubicacion del elemento de las filas
        orientacion (_type_): orientacion del barco
        co (_type_): Valores del numero de columnas
        fi (_type_): Valores del numero de filas

    Returns:
        bool:Retorna un valor booleano para dirigir el avance del proceso de juego
    """
    global nuevoJuego
    nuevoJuego["BarcosJ2"]["Destructor4J2"]["x1"]=x
    nuevoJuego["BarcosJ2"]["Destructor4J2"]["y1"]=y
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
    """Funcion que solicita la ubicacion de un descructor del jugador 2

    Args:
        x (_type_): Valores del numero de columnas
        y (_type_): Valores del numero de filas
    """
    x=int(x)
    y=int(y)
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
    orientacionDerecha.place(x=600, y=90)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=700, y=90)
    
    imprimirMatrizJ2(x,y,tablero)

def guardarDestructor5J2(x,y,orientacion,co,fi):
    """Funcion que guarda en el diccionario la ubicacion del desctructor del jugador 2

    Args:
        x (_type_): ubicacion del elemento dentro de las columnas
        y (_type_): _description_ ubicacion del elemento de las filas
        orientacion (_type_): orientacion del barco
        co (_type_): Valores del numero de columnas
        fi (_type_): Valores del numero de filas

    Returns:
        bool:Retorna un valor booleano para dirigir el avance del proceso de juego
    """
    global nuevoJuego
    nuevoJuego["BarcosJ2"]["Destructor5J2"]["x1"]=x
    nuevoJuego["BarcosJ2"]["Destructor5J2"]["y1"]=y
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
    """Funcion que solicita la ubicacion de un descructor del jugador 2

    Args:
        x (_type_): Valores del numero de columnas
        y (_type_): Valores del numero de filas
    """
    x=int(x)
    y=int(y)
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
    orientacionDerecha.place(x=600, y=90)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=700, y=90)
    
    imprimirMatrizJ2(x,y,tablero)

def guardarDestructor6J2(x,y,orientacion,co,fi):
    """Funcion que guarda en el diccionario la ubicacion del desctructor del jugador 2

    Args:
        x (_type_): ubicacion del elemento dentro de las columnas
        y (_type_): _description_ ubicacion del elemento de las filas
        orientacion (_type_): orientacion del barco
        co (_type_): Valores del numero de columnas
        fi (_type_): Valores del numero de filas

    Returns:
        bool:Retorna un valor booleano para dirigir el avance del proceso de juego
    """
    global nuevoJuego
    nuevoJuego["BarcosJ2"]["Destructor6J2"]["x1"]=x
    nuevoJuego["BarcosJ2"]["Destructor6J2"]["y1"]=y
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
    """Funcion que solicita la ubicacion de un crucero del jugador 2

    Args:
        x (_type_): Valores del numero de columnas
        y (_type_): Valores del numero de filas
    """
    x=int(x)
    y=int(y)
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
    orientacionDerecha.place(x=600, y=90)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=700, y=90)
        
    imprimirMatrizJ2(x,y,tablero)

def guardarCrucero1J2(x,y,orientacion,co,fi):
    """Funcion que guarda en el diccionario la ubicacion del crucero del jugador 2

    Args:
        x (_type_): ubicacion del elemento dentro de las columnas
        y (_type_): _description_ ubicacion del elemento de las filas
        orientacion (_type_): orientacion del barco
        co (_type_): Valores del numero de columnas
        fi (_type_): Valores del numero de filas

    Returns:
        bool:Retorna un valor booleano para dirigir el avance del proceso de juego
    """
    global nuevoJuego
    nuevoJuego["BarcosJ2"]["Crucero1J2"]["x1"]=x
    nuevoJuego["BarcosJ2"]["Crucero1J2"]["y1"]=y

    if orientacion==1:
        nuevoJuego["BarcosJ2"]["Crucero1J2"]["x2"]=x-1
        nuevoJuego["BarcosJ2"]["Crucero1J2"]["y2"]=y
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=5
        nuevoJuego["Matriz"]["matrizJ2"][y][x-1]=9

    elif orientacion==2:
        nuevoJuego["BarcosJ2"]["Crucero1J2"]["x2"]=x
        nuevoJuego["BarcosJ2"]["Crucero1J2"]["y2"]=y+1
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=6
        nuevoJuego["Matriz"]["matrizJ2"][y+1][x]=10

    elif orientacion==3:
        nuevoJuego["BarcosJ2"]["Crucero1J2"]["y2"]=y
        nuevoJuego["BarcosJ2"]["Crucero1J2"]["x2"]=x+1
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=7
        nuevoJuego["Matriz"]["matrizJ2"][y][x+1]=11

    elif orientacion==4:
        nuevoJuego["BarcosJ2"]["Crucero1J2"]["y2"]=y-1
        nuevoJuego["BarcosJ2"]["Crucero1J2"]["x2"]=x
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=8
        nuevoJuego["Matriz"]["matrizJ2"][y-1][x]=12

    nuevoJuego["BarcosJ2"]["Crucero1J2"]["orientacion"]=orientacion
    
    ubicarCrucero2J2(co,fi) 
    return True

def ubicarCrucero2J2(x,y):
    """Funcion que solicita la ubicacion de un crucero del jugador 2

    Args:
        x (_type_): Valores del numero de columnas
        y (_type_): Valores del numero de filas
    """
    x=int(x)
    y=int(y)
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
    orientacionDerecha.place(x=600, y=90)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=700, y=90)
    
    imprimirMatrizJ2(x,y,tablero)

def guardarCrucero2J2(x,y,orientacion,co,fi):
    """Funcion que guarda en el diccionario la ubicacion del crucero del jugador 2

    Args:
        x (_type_): ubicacion del elemento dentro de las columnas
        y (_type_): _description_ ubicacion del elemento de las filas
        orientacion (_type_): orientacion del barco
        co (_type_): Valores del numero de columnas
        fi (_type_): Valores del numero de filas

    Returns:
        bool:Retorna un valor booleano para dirigir el avance del proceso de juego
    """
    global nuevoJuego
    nuevoJuego["BarcosJ2"]["Crucero2J2"]["x1"]=x
    nuevoJuego["BarcosJ2"]["Crucero2J2"]["y1"]=y

    if orientacion==1:
        nuevoJuego["BarcosJ2"]["Crucero2J2"]["x2"]=x-1
        nuevoJuego["BarcosJ2"]["Crucero2J2"]["y2"]=y
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=5
        nuevoJuego["Matriz"]["matrizJ2"][y][x-1]=9

    elif orientacion==2:
        nuevoJuego["BarcosJ2"]["Crucero2J2"]["x2"]=x
        nuevoJuego["BarcosJ2"]["Crucero2J2"]["y2"]=y+1
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=6
        nuevoJuego["Matriz"]["matrizJ2"][y+1][x]=10

    elif orientacion==3:
        nuevoJuego["BarcosJ2"]["Crucero2J2"]["y2"]=y
        nuevoJuego["BarcosJ2"]["Crucero2J2"]["x2"]=x+1
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=7
        nuevoJuego["Matriz"]["matrizJ2"][y][x+1]=11

    elif orientacion==4:
        nuevoJuego["BarcosJ2"]["Crucero2J2"]["y2"]=y-1
        nuevoJuego["BarcosJ2"]["Crucero2J2"]["x2"]=x
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=8
        nuevoJuego["Matriz"]["matrizJ2"][y-1][x]=12

    nuevoJuego["BarcosJ2"]["Crucero2J2"]["orientacion"]=orientacion
    ubicarCrucero3J2(co,fi) 
    return True

def ubicarCrucero3J2(x,y):
    """Funcion que solicita la ubicacion de un crucero del jugador 2

    Args:
        x (_type_): Valores del numero de columnas
        y (_type_): Valores del numero de filas
    """
    x=int(x)
    y=int(y)
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
    orientacionDerecha.place(x=600, y=90)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=700, y=90)
    
    imprimirMatrizJ2(x,y,tablero)

def guardarCrucero3J2(x,y,orientacion,co,fi):
    """Funcion que guarda en el diccionario la ubicacion del crucero del jugador 2

    Args:
        x (_type_): ubicacion del elemento dentro de las columnas
        y (_type_): _description_ ubicacion del elemento de las filas
        orientacion (_type_): orientacion del barco
        co (_type_): Valores del numero de columnas
        fi (_type_): Valores del numero de filas

    Returns:
        bool:Retorna un valor booleano para dirigir el avance del proceso de juego
    """
    global nuevoJuego
    nuevoJuego["BarcosJ2"]["Crucero3J2"]["x1"]=x
    nuevoJuego["BarcosJ2"]["Crucero3J2"]["y1"]=y

    if orientacion==1:
        nuevoJuego["BarcosJ2"]["Crucero3J2"]["x2"]=x-1
        nuevoJuego["BarcosJ2"]["Crucero3J2"]["y2"]=y
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=5
        nuevoJuego["Matriz"]["matrizJ2"][y][x-1]=9

    elif orientacion==2:
        nuevoJuego["BarcosJ2"]["Crucero3J2"]["x2"]=x
        nuevoJuego["BarcosJ2"]["Crucero3J2"]["y2"]=y+1
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=6
        nuevoJuego["Matriz"]["matrizJ2"][y+1][x]=10

    elif orientacion==3:
        nuevoJuego["BarcosJ2"]["Crucero3J2"]["y2"]=y
        nuevoJuego["BarcosJ2"]["Crucero3J2"]["x2"]=x+1
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=7
        nuevoJuego["Matriz"]["matrizJ2"][y][x+1]=11

    elif orientacion==4:
        nuevoJuego["BarcosJ2"]["Crucero3J2"]["y2"]=y-1
        nuevoJuego["BarcosJ2"]["Crucero3J2"]["x2"]=x
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=8
        nuevoJuego["Matriz"]["matrizJ2"][y-1][x]=12

    nuevoJuego["BarcosJ2"]["Crucero3J2"]["orientacion"]=orientacion
    ubicarCrucero4J2(co,fi)
    return True

def ubicarCrucero4J2(x,y):
    """Funcion que solicita la ubicacion de un crucero del jugador 2

    Args:
        x (_type_): Valores del numero de columnas
        y (_type_): Valores del numero de filas
    """
    x=int(x)
    y=int(y)
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
    orientacionDerecha.place(x=600, y=90)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=700, y=90)
    
    imprimirMatrizJ2(x,y,tablero)

def guardarCrucero4J2(x,y,orientacion,co,fi):
    """Funcion que guarda en el diccionario la ubicacion del crucero del jugador 2

    Args:
        x (_type_): ubicacion del elemento dentro de las columnas
        y (_type_): _description_ ubicacion del elemento de las filas
        orientacion (_type_): orientacion del barco
        co (_type_): Valores del numero de columnas
        fi (_type_): Valores del numero de filas

    Returns:
        bool:Retorna un valor booleano para dirigir el avance del proceso de juego
    """
    global nuevoJuego
    nuevoJuego["BarcosJ2"]["Crucero4J2"]["x1"]=x
    nuevoJuego["BarcosJ2"]["Crucero4J2"]["y1"]=y

    if orientacion==1:
        nuevoJuego["BarcosJ2"]["Crucero4J2"]["x2"]=x-1
        nuevoJuego["BarcosJ2"]["Crucero4J2"]["y2"]=y
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=5
        nuevoJuego["Matriz"]["matrizJ2"][y][x-1]=9

    elif orientacion==2:
        nuevoJuego["BarcosJ2"]["Crucero4J2"]["x2"]=x
        nuevoJuego["BarcosJ2"]["Crucero4J2"]["y2"]=y+1
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=6
        nuevoJuego["Matriz"]["matrizJ2"][y+1][x]=10

    elif orientacion==3:
        nuevoJuego["BarcosJ2"]["Crucero4J2"]["y2"]=y
        nuevoJuego["BarcosJ2"]["Crucero4J2"]["x2"]=x+1
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=7
        nuevoJuego["Matriz"]["matrizJ2"][y][x+1]=11

    elif orientacion==4:
        nuevoJuego["BarcosJ2"]["Crucero4J2"]["y2"]=y-1
        nuevoJuego["BarcosJ2"]["Crucero4J2"]["x2"]=x
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=8
        nuevoJuego["Matriz"]["matrizJ2"][y-1][x]=12

    nuevoJuego["BarcosJ2"]["Crucero4J2"]["orientacion"]=orientacion
   
    ubicarAcorazado1J2(co,fi)
    return True

def ubicarAcorazado1J2(x,y):
    """Funcion que solicita la ubicacion de un acorazado del jugador 2

    Args:
        x (_type_): Valores del numero de columnas
        y (_type_): Valores del numero de filas
    """
    x=int(x)
    y=int(y)
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
    orientacionDerecha.place(x=600, y=90)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=700, y=90)
    
    imprimirMatrizJ2(x,y,tablero)

def guardarAcorazado1J2(x,y,orientacion,co,fi):
    """Funcion que guarda en el diccionario la ubicacion del acorazado del jugador 2

    Args:
        x (_type_): ubicacion del elemento dentro de las columnas
        y (_type_): _description_ ubicacion del elemento de las filas
        orientacion (_type_): orientacion del barco
        co (_type_): Valores del numero de columnas
        fi (_type_): Valores del numero de filas

    Returns:
        bool:Retorna un valor booleano para dirigir el avance del proceso de juego
    """
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
        nuevoJuego["BarcosJ2"]["Acorazado1J2"]["x2"]=x
        nuevoJuego["BarcosJ2"]["Acorazado1J2"]["y2"]=y+1
        nuevoJuego["BarcosJ2"]["Acorazado1J2"]["x3"]=x
        nuevoJuego["BarcosJ2"]["Acorazado1J2"]["y3"]=y+2
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=14
        nuevoJuego["Matriz"]["matrizJ2"][y+1][x]=18
        nuevoJuego["Matriz"]["matrizJ2"][y+2][x]=22

    elif orientacion==3:
        nuevoJuego["BarcosJ2"]["Acorazado1J2"]["y2"]=y
        nuevoJuego["BarcosJ2"]["Acorazado1J2"]["x2"]=x+1
        nuevoJuego["BarcosJ2"]["Acorazado1J2"]["y3"]=y
        nuevoJuego["BarcosJ2"]["Acorazado1J2"]["x3"]=x+2
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

    nuevoJuego["BarcosJ2"]["Acorazado1J2"]["orientacion"]=orientacion
    ubicarAcorazado2J2(co,fi)   
    return True

def ubicarAcorazado2J2(x,y):
    """Funcion que solicita la ubicacion de un acorazado del jugador 2

    Args:
        x (_type_): Valores del numero de columnas
        y (_type_): Valores del numero de filas
    """
    x=int(x)
    y=int(y)
    tablero=tk.Toplevel()
    tablero.title("Tablero")
    tablero.attributes("-fullscreen", True)

    tableroLabel= Label(tablero, text="Inserte la ubicacion del barco:")
    tableroLabel.place(x=1,y=10)

    orientacion= tk.IntVar()

    botonGuardarPosicion=Button(tablero, text="Guardar",command= lambda:validarUbicacionAcorazadoJ2(resultadoX,resultadoY,orientacion.get(),x,y) and guardarAcorazado2J2(resultadoX,resultadoY,orientacion.get (),x,y) and tablero.destroy())
    botonGuardarPosicion.place(x=400, y=40)

    orientacionLabel= Label(tablero, text="Orientacion del barco:")
    orientacionLabel.place(x=500,y=40)

    orientacionIzquierda=ttk.Radiobutton(tablero, text="Derecha", value= 1, variable=orientacion)
    orientacionIzquierda.place(x=600, y=60)
    orientacionDerecha=ttk.Radiobutton(tablero, text="Arriba", value=2, variable=orientacion)
    orientacionDerecha.place(x=600, y=90)
    orientacioAbajo=ttk.Radiobutton(tablero, text="Izquierda", value=3, variable=orientacion)
    orientacioAbajo.place(x=700, y=60)
    orientacionArriba=ttk.Radiobutton(tablero, text="Abajo", value=4, variable=orientacion)
    orientacionArriba.place(x=700, y=90)
    
    imprimirMatrizJ2(x,y,tablero)

def guardarAcorazado2J2(x,y,orientacion,co,fi):
    """Funcion que guarda en el diccionario la ubicacion del acorazado del jugador 2

    Args:
        x (_type_): ubicacion del elemento dentro de las columnas
        y (_type_): _description_ ubicacion del elemento de las filas
        orientacion (_type_): orientacion del barco
        co (_type_): Valores del numero de columnas
        fi (_type_): Valores del numero de filas

    Returns:
        bool:Retorna un valor booleano para dirigir el avance del proceso de juego
    """
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
        nuevoJuego["BarcosJ2"]["Acorazado2J2"]["x2"]=x
        nuevoJuego["BarcosJ2"]["Acorazado2J2"]["y2"]=y+1
        nuevoJuego["BarcosJ2"]["Acorazado2J2"]["x3"]=x
        nuevoJuego["BarcosJ2"]["Acorazado2J2"]["y3"]=y+2
        nuevoJuego["Matriz"]["matrizJ2"][y][x]=14
        nuevoJuego["Matriz"]["matrizJ2"][y+1][x]=18
        nuevoJuego["Matriz"]["matrizJ2"][y+2][x]=22

    elif orientacion==3:
        nuevoJuego["BarcosJ2"]["Acorazado2J2"]["y2"]=y
        nuevoJuego["BarcosJ2"]["Acorazado2J2"]["x2"]=x+1
        nuevoJuego["BarcosJ2"]["Acorazado2J2"]["y3"]=y
        nuevoJuego["BarcosJ2"]["Acorazado2J2"]["x3"]=x+2
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

    nuevoJuego["BarcosJ2"]["Acorazado2J2"]["orientacion"]=orientacion 
    pantallaBarcosJ2(co,fi)  
    return True

def pantallaBarcosJ2(x,y):
    """Funcion que muestra la ubicacion de los barcos del jugador 2

    Args:
        x (_type_): Valores del numero de columnas
        y (_type_): Valores del numero de filas
    """
    x=int(x)
    y=int(y)
    tablero=tk.Toplevel()
    tablero.title("Tablero")
    tablero.attributes("-fullscreen", True)

    tableroLabel= Label(tablero, text="Barcos del jugador 2")
    tableroLabel.place(x=1,y=10)

    botonGuardarPosicion=Button(tablero, text="Continuar",command= lambda: pantallaDoble() and tablero.destroy())
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
    """Funcion que valida sin un barco se puede guardar o no es una ubicacion del jugador

    Args:
        x (_type_): posicion en columnas del barco
        y (_type_): posicion en filas del barco
        orientacion (_type_): orientacion del barco

    Returns:
        bool: Retorna True para poder continuar el proceso de operaciones
    """
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
    """Funcion que valida sin un barco se puede guardar o no es una ubicacion del jugador

    Args:
        x (_type_): posicion en columnas del barco
        y (_type_): posicion en filas del barco
        orientacion (_type_): orientacion del barco

    Returns:
        bool: Retorna True para poder continuar el proceso de operaciones
    """
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
    """Funcion que valida sin un barco se puede guardar o no es una ubicacion del jugador

    Args:
        x (_type_): posicion en columnas del barco
        y (_type_): posicion en filas del barco
        orientacion (_type_): orientacion del barco

    Returns:
        bool: Retorna True para poder continuar el proceso de operaciones
    """
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
    """Funcion que valida sin un barco se puede guardar o no es una ubicacion del jugador

    Args:
        x (_type_): posicion en columnas del barco
        y (_type_): posicion en filas del barco
        orientacion (_type_): orientacion del barco

    Returns:
        bool: Retorna True para poder continuar el proceso de operaciones
    """
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
    """Funcion que valida sin un barco se puede guardar o no es una ubicacion del jugador

    Args:
        x (_type_): posicion en columnas del barco
        y (_type_): posicion en filas del barco
        orientacion (_type_): orientacion del barco

    Returns:
        bool: Retorna True para poder continuar el proceso de operaciones
    """
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
    """Funcion que valida sin un barco se puede guardar o no es una ubicacion del jugador

    Args:
        x (_type_): posicion en columnas del barco
        y (_type_): posicion en filas del barco
        orientacion (_type_): orientacion del barco

    Returns:
        bool: Retorna True para poder continuar el proceso de operaciones
    """
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

disparoXJ1=0
disparoYJ1=0
disparoXJ2=0
disparoYJ2=0

def accionDisparoJ1(x:int,y:int):
    """Funcion que modifica variables globales

    Args:
        x (int): variable que se utilizara para disparar a una columna de un tablero
        y (int): variable que se utilizara para disparar a una fila de un tablero
    """
    global disparoXJ1
    global disparoYJ1
    disparoXJ1=x
    disparoYJ1=y 
    

def accionDisparoJ2(x:int,y:int):
    """Funcion que modifica variables globales

    Args:
        x (int): variable que se utilizara para disparar a una columna de un tablero
        y (int): variable que se utilizara para disparar a una fila de un tablero
    """
    global disparoXJ2
    global disparoYJ2
    disparoXJ2=x
    disparoYJ2=y

def pantallaGanador(opciones:str):
    """Pantalla que muestra el final del juego

    Args:
        opciones (str): Diferentes desenlaces del juego
    """
    ventanaGanador=tk.Toplevel()
    ventanaGanador.title("Battleship")
    ventanaGanador.attributes("-fullscreen", True)

    nombreJ1=nuevoJuego["Jugador 1"]["Nickname"]
    nombreJ2=nuevoJuego["Jugador 2"]["Nickname"]
    cantidadBarcosJ1=nuevoJuego["Jugador 1"]["Cantidad Barcos"] 
    cantidadBarcosJ2=nuevoJuego["Jugador 2"]["Cantidad Barcos"]

    if opciones=="empate":
        tituloVentana= tk.Label(ventanaGanador, text="Empate", font=("Courier New", 60, "bold"))
        subtituloVentana= tk.Label(ventanaGanador, text="¡Felicidades!", font=("Courier New", 40, "bold"))
        contenidoVentana= tk.Label(ventanaGanador, text="Ambos jugadores han destruido los barcos del otro", font=("Courier New", 20, "bold"))
        labelVacio1= tk.Label(ventanaGanador, text="", font=("Courier New", 20, "bold"))
        donaciones= tk.Label(ventanaGanador, text="Si deseas hacer una donación, contacta a los desarrolladores", font=("Courier New", 18, "bold"))
        desarrolladores= tk.Label(ventanaGanador, text="Desarrolladores: ", font=("Courier New", 20, "bold"))
        desarrollador1= tk.Label(ventanaGanador, text="Ignacio Alpízar V.", font=("Courier New", 15, "bold"))
        desarrollador2= tk.Label(ventanaGanador, text="Wilmer Azofeifa V.", font=("Courier New", 15, "bold"))
        labelVacio2= tk.Label(ventanaGanador, text="", font=("Courier New", 20, "bold"))
        gracias= tk.Label(ventanaGanador, text="Gracias por jugar", font=("Courier New", 25, "bold"))
        labelVacio3= tk.Label(ventanaGanador, text="", font=("Courier New", 20, "bold"))

        botonDonar= tk.Button(ventanaGanador, text="Donar", font=("Courier New", 20, "bold"), command=lambda: messagebox.showinfo("Donar", "Gracias por su donación"), bg="blue", fg="white")
        botoSalir= tk.Button(ventanaGanador, text="Salir", font=("Courier New", 18), command=ventanaGanador.destroy, bg="red", fg="white")

        tituloVentana.pack()
        subtituloVentana.pack()
        contenidoVentana.pack()
        labelVacio1.pack()
        donaciones.pack()
        desarrolladores.pack()
        desarrollador1.pack()
        desarrollador2.pack()
        labelVacio2.pack()
        gracias.pack()
        labelVacio3.pack()

        botonDonar.pack()
        botoSalir.place(x=0, y=0)

    elif opciones=="Jugador 1":
        tituloVentana= tk.Label(ventanaGanador, text="Ganador", font=("Courier New", 60, "bold"))
        subtituloVentana= tk.Label(ventanaGanador, text=f"{nombreJ1}", font=("Courier New", 40, "bold"))
        contenidoVentana1= tk.Label(ventanaGanador, text=f"¡Felicidades!, {nombreJ1} has ganado la partida", font=("Courier New", 20, "bold"))
        contenidoVentana2= tk.Label(ventanaGanador, text=f"Barcos restantes: {cantidadBarcosJ1}", font=("Courier New", 20, "bold"))
        labelVacio1= tk.Label(ventanaGanador, text="", font=("Courier New", 20, "bold"))
        donaciones= tk.Label(ventanaGanador, text="Si deseas hacer una donación, contacta a los desarrolladores", font=("Courier New", 18, "bold"))
        desarrolladores= tk.Label(ventanaGanador, text="Desarrolladores: ", font=("Courier New", 20, "bold"))
        desarrollador1= tk.Label(ventanaGanador, text="Ignacio Alpízar V.", font=("Courier New", 15, "bold"))
        desarrollador2= tk.Label(ventanaGanador, text="Wilmer Azofeifa V.", font=("Courier New", 15, "bold"))
        labelVacio2= tk.Label(ventanaGanador, text="", font=("Courier New", 20, "bold"))
        gracias= tk.Label(ventanaGanador, text="Gracias por jugar", font=("Courier New", 25, "bold"))
        labelVacio3= tk.Label(ventanaGanador, text="", font=("Courier New", 20, "bold"))

        botonDonar= tk.Button(ventanaGanador, text="Donar", font=("Courier New", 20, "bold"), command=lambda: messagebox.showinfo("Donar", "Gracias por su donación"), bg="blue", fg="white")
        botoSalir= tk.Button(ventanaGanador, text="Salir", font=("Courier New", 18), command=ventanaGanador.destroy, bg="red", fg="white")

        tituloVentana.pack()
        subtituloVentana.pack()
        contenidoVentana1.pack()
        contenidoVentana2.pack()
        labelVacio1.pack()
        donaciones.pack()
        desarrolladores.pack()
        desarrollador1.pack()
        desarrollador2.pack()
        labelVacio2.pack()
        gracias.pack()
        labelVacio3.pack()

        botonDonar.pack()
        botoSalir.place(x=0, y=0)

    elif opciones=="Jugador 2":
        tituloVentana= tk.Label(ventanaGanador, text="Ganador", font=("Courier New", 60, "bold"))
        subtituloVentana= tk.Label(ventanaGanador, text=f"{nombreJ2}", font=("Courier New", 40, "bold"))
        contenidoVentana1= tk.Label(ventanaGanador, text=f"¡Felicidades!, {nombreJ2} has ganado la partida", font=("Courier New", 20, "bold"))
        contenidoVentana2= tk.Label(ventanaGanador, text=f"Barcos restantes: {cantidadBarcosJ2}", font=("Courier New", 20, "bold"))
        labelVacio1= tk.Label(ventanaGanador, text="", font=("Courier New", 20, "bold"))
        donaciones= tk.Label(ventanaGanador, text="Si deseas hacer una donación, contacta a los desarrolladores", font=("Courier New", 18, "bold"))
        desarrolladores= tk.Label(ventanaGanador, text="Desarrolladores: ", font=("Courier New", 20, "bold"))
        desarrollador1= tk.Label(ventanaGanador, text="Ignacio Alpízar V.", font=("Courier New", 15, "bold"))
        desarrollador2= tk.Label(ventanaGanador, text="Wilmer Azofeifa V.", font=("Courier New", 15, "bold"))
        labelVacio2= tk.Label(ventanaGanador, text="", font=("Courier New", 20, "bold"))
        gracias= tk.Label(ventanaGanador, text="Gracias por jugar", font=("Courier New", 25, "bold"))
        labelVacio3= tk.Label(ventanaGanador, text="", font=("Courier New", 20, "bold"))

        botonDonar= tk.Button(ventanaGanador, text="Donar", font=("Courier New", 20, "bold"), command=lambda: messagebox.showinfo("Donar", "Gracias por su donación"), bg="blue", fg="white")
        botoSalir= tk.Button(ventanaGanador, text="Salir", font=("Courier New", 18), command= lambda: borrarClave(nuevoJuego["NombrePartida"]) and ventanaGanador.destroy, bg="red", fg="white")

        tituloVentana.pack()
        subtituloVentana.pack()
        contenidoVentana1.pack()
        contenidoVentana2.pack()
        labelVacio1.pack()
        donaciones.pack()
        desarrolladores.pack()
        desarrollador1.pack()
        desarrollador2.pack()
        labelVacio2.pack()
        gracias.pack()
        labelVacio3.pack()

        botonDonar.pack()
        botoSalir.place(x=0, y=0)



def pantallaDoble():
    """Pantalla donde se realiza la mecanica de disparos del juego

    Returns:
       bool: Retorna Trues para poder continuar el proceso del juego
    """
    global nuevoJuego
    global matrizJ1
    global matrizJ2
    global matrizDisparosJ1
    global matrizDisparosJ2
    global limitesTablero

    x=int(nuevoJuego["Matriz"]["Columnas"])
    y=int(nuevoJuego["Matriz"]["Filas"])

    limitesTablero=[x//2,y]

    juego = Toplevel()
    juego.title("Battleship")
    juego.attributes("-fullscreen", True)

    puntajeJugador1=nuevoJuego["Jugador 1"]["Puntaje"]
    nicknameJ1=nuevoJuego["Jugador 1"]["Nickname"]
    cantidadBarcosJ1=nuevoJuego["Jugador 1"]["Cantidad Barcos"]

    puntajeJugador2=nuevoJuego["Jugador 2"]["Puntaje"]
    nicknameJ2=nuevoJuego["Jugador 2"]["Nickname"]
    cantidadBarcosJ2=nuevoJuego["Jugador 2"]["Cantidad Barcos"]
    

    

    labelPuntajeJ1=Label(juego, text=f"Puntaje de {nicknameJ1}: {puntajeJugador1}")
    labelPuntajeJ1.place(x=200, y=10) 
    labelCantidadBarcosJ1=Label(juego, text=f"Barcos restantes: {cantidadBarcosJ1}")
    labelCantidadBarcosJ1.place(x=200, y=40)

    labelPuntajeJ2=Label(juego, text=f"Puntaje de {nicknameJ2}: {puntajeJugador2}")
    labelPuntajeJ2.place(x=400, y=10)
    labelCantidadBarcosJ2=Label(juego, text=f"Barcos restantes: {cantidadBarcosJ2}")    
    labelCantidadBarcosJ2.place(x=400, y=40)

    botonSalir=Button(juego, text="Salir",command=lambda: juego.destroy())
    botonSalir.place(x=1331, y=10)

    botonGuardarSalir=Button(juego, text="Guardar y salir",command=lambda: guardarDatos(nuevoJuego["NombrePartida"]) and juego.destroy())
    botonGuardarSalir.place(x=1200, y=10)
    
    #global celdasRojasJ1
    #global celdasRojasJ2

    matrizJ1= [[tk.Button(juego,bg="#00FFFF",command= None)
                for c in range(x//2)]for f in range(y)]
    """if celdasRojasJ2!=[]:
        for tupla in celdasRojasJ2:
            x=tupla[1]
            y=tupla[0]
            matrizJ1[y][x].config(bg="red")"""
    matrizJ2= [[tk.Button(juego,bg="#00FFFF",command= None)
                for c in range(x//2)]for f in range(y)]
    """if celdasRojasJ1!=[]:
        for tupla in celdasRojasJ1:
            x=tupla[1]
            y=tupla[0]
            matrizJ2[y][x].config(bg="red")"""
    colocarBarcos()
    print("\033[94m")
    print("\n")
    print(f"{nuevoJuego["BarcosJ1"]}")
    print("\033[96m")
    print(nuevoJuego["BarcosJ2"])

    def cambiarPantalla1(juego):
        global nuevoJuego

        nuevoJuego["Pantalla"]=1
        juego.after(250,pantallaDoble())
        cerrarVentana(juego)
    
    def finalJuego(juego):
        """Esta funcion se encarga de analizar si alguno de los dos jugadores se ha quedado sin barcos

        Returns:
            bool: Retorna True para poder continuar el proceso del juego
        """
        if nuevoJuego["Jugador 1"]["Cantidad Barcos"]==0 and nuevoJuego["Jugador 2"]["Cantidad Barcos"]==0:
            pantallaGanador("empate")
            juego.destroy()

        elif nuevoJuego["Jugador 1"]["Cantidad Barcos"]==0:
            pantallaGanador("Jugador 2")
            juego.destroy()
        
        elif nuevoJuego["Jugador 2"]["Cantidad Barcos"]==0:
            pantallaGanador("Jugador 1")
            juego.destroy()
        
        else:
            return True
            
    def cambiarPantalla2(juego):
        """Funcion que cambia la variable funciona como separador entre la ventana de disparos del jugador 1 y jugador 2"""
        global nuevoJuego
        nuevoJuego["Pantalla"]=2
        juego.after(250,pantallaDoble())
        cerrarVentana(juego)

    def cerrarVentana(juego):
        """Funcion que cierra la ventana

        Args:
            juego (_type_): Ventana que se encuentra activa
        """
        juego.destroy()
        
    if nuevoJuego["Pantalla"] ==1:                                          #Segun esta condicion se muestra los barcos del jugador 1 y su tablero de disparo
        
        global celdasRojasJ1
        posX= 10
        posY= 200

        for filaBotones in matrizJ1:
            posX=10
            for btn in filaBotones:
                btn.place(x=posX, y=posY, height=30, width=30)
                posX+=32
            posY+=36

        matrizDisparosJ1= [[tk.Button(juego,bg="blue",command= lambda x=c,y=f: accionDisparoJ1(x,y))  
                            for c in range(x//2)]for f in range(y)]
        posXcopia=posX+10
        posYcopia=200
        for filaBotones in matrizDisparosJ1:
            posXcopia=posX+10
            for btn in filaBotones:
                btn.place(x=posXcopia, y=posYcopia, height=30, width=30)
                posXcopia+=32
            posYcopia+=36

        if celdasRojasJ1!=[]:
            for tupla in celdasRojasJ1:
                x=tupla[1]
                y=tupla[0]
                matrizDisparosJ1[y][x].config(bg="red")
                
        botonDisparar=Button(juego, text="Disparar",command=lambda:validarDisparoJ1(disparoXJ1, disparoYJ1) and colocarBarcos() and cambiarPantalla2(juego))
        botonDisparar.place(x=10,y=10)

    elif nuevoJuego["Pantalla"]==2:                                        #O se muestra los barcos del jugador 1 y su tablero de disparo
        global celdasRojasJ2
        puntajeJugador2=nuevoJuego["Jugador 2"]["Puntaje"]

        matrizDisparosJ2= [[tk.Button(juego,bg="blue",command= lambda x=c,y=f : accionDisparoJ2(x,y))
                            for c in range(x//2)] for f in range(y)]
        posXcopia=10
        posYcopia=200
        for filaBotones in matrizDisparosJ2:
            posXcopia=10
            for btn in filaBotones:
                btn.place(x=posXcopia, y=posYcopia, height=30, width=30)
                posXcopia+=32
            posYcopia+=36
        for tupla in celdasRojasJ2:
            x=tupla[1]
            y=tupla[0]
            matrizDisparosJ2[y][x].config(bg="red")
            
        posX= posXcopia+10
        posY= 200
        for filaBotones in matrizJ2:
            posX=posXcopia+10
            for btn in filaBotones:
                btn.place(x=posX, y=posY, height=30, width=30)
                posX+=32
            posY+=36

        botonDisparar=Button(juego, text="Disparar",command=lambda:validarDisparoJ2(disparoXJ2, disparoYJ2) and accionesMovimiento() and colocarBarcos() and finalJuego(juego) and cambiarPantalla1(juego))
        botonDisparar.place(x=10,y=10)  
    
    return True

     
def agregarCeldasRojas1(x,y):
    """Esta funcion se encarga de asignar los botones que iran de color rojo en el tablero de disparo de jugador 1

    Args:
        x (_type_): Numero que representa la columna en donde esta ubicado el boton
        y (_type_): Numero que representa la fila en donde esta ubicado el boton
    """
    global celdasRojasJ1
    roja=(y,x)
    celdasRojasJ1.append(roja)

def agregarCeldasRojas2(x,y):
    """Esta funcion se encarga de asignar los botones que iran de color rojo en el tablero de disparo de jugador 2

    Args:
        x (_type_): Numero que representa la columna en donde esta ubicado el boton
        y (_type_): Numero que representa la fila en donde esta ubicado el boton
    """
    global celdasRojasJ2
    roja=(y,x)
    celdasRojasJ2.append(roja)


def mensajeConfirmacion1(nombreBarco:str,x,y):
    """Funcion que muestra mensajes al jugador 1 uno si ha impactado, derribado no barcos del oponente
    """
    
    global nuevoJuego
    global matrizDisparosJ1
    global celdasRojasJ1

    nuevoJuego["BarcosJ2"][nombreBarco]["disparos"]=1
    if nuevoJuego["BarcosJ2"][nombreBarco]["vida"]==0:
        messagebox.showerror("Mensaje", "No le has dado a ningun barco")

    elif nombreBarco in ["Destructor1J2","Destructor2J2","Destructor3J2","Destructor4J2","Destructor5J2","Destructor6J2"] and nuevoJuego["BarcosJ2"][nombreBarco]["vida"]==1:
        messagebox.showinfo("Mensaje", "Has dado con un barco")
        if nuevoJuego["BarcosJ2"][nombreBarco]["x1"]==x and nuevoJuego["BarcosJ2"][nombreBarco]["y1"]==y:
            messagebox.showinfo("Mensaje", "Has hundido un barco")
            nuevoJuego["BarcosJ2"][nombreBarco]["vida"]=0
            nuevoJuego["Jugador 1"]["Puntaje"]+=1
            nuevoJuego["Jugador 2"]["Cantidad Barcos"]-=1

    elif nombreBarco in ["Crucero1J2","Crucero2J2","Crucero3J2","Crucero4J2"] and nuevoJuego["BarcosJ2"][nombreBarco]["vida"]==1:
        messagebox.showinfo("Mensaje", "Has dado con un barco")
        if nuevoJuego["BarcosJ2"][nombreBarco]["x1"]==x and nuevoJuego["BarcosJ2"][nombreBarco]["y1"]==y:
            nuevoJuego["BarcosJ2"][nombreBarco]["xy1"]=1
            agregarCeldasRojas1(x,y)
            
        elif nuevoJuego["BarcosJ2"][nombreBarco]["x2"]==x and nuevoJuego["BarcosJ2"][nombreBarco]["y2"]==y:
            nuevoJuego["BarcosJ2"][nombreBarco]["xy2"]=1
            agregarCeldasRojas1(x,y)
           
        if nuevoJuego["BarcosJ2"][nombreBarco]["xy1"]==1 and nuevoJuego["BarcosJ2"][nombreBarco]["xy2"]==1:
            nuevoJuego["BarcosJ2"][nombreBarco]["vida"]=0
            messagebox.showinfo("Mensaje", "Has hundido un barco")
            x1=nuevoJuego["BarcosJ2"][nombreBarco]["x1"]
            y1=nuevoJuego["BarcosJ2"][nombreBarco]["y1"]
            x2=nuevoJuego["BarcosJ2"][nombreBarco]["x2"]
            y2=nuevoJuego["BarcosJ2"][nombreBarco]["y2"]
            celdasRojasJ1.remove((y1,x1))
            celdasRojasJ1.remove((y2,x2))
            nuevoJuego["Jugador 1"]["Puntaje"]+=2
            nuevoJuego["Jugador 2"]["Cantidad Barcos"]-=1
        
            
    if nombreBarco in ["Acorazado1J2","Acorazado2J2"] and nuevoJuego["BarcosJ2"][nombreBarco]["vida"]==1:
        messagebox.showinfo("Mensaje", "Has dado con un barco")
        if nuevoJuego["BarcosJ2"][nombreBarco]["x1"]==x and nuevoJuego["BarcosJ2"][nombreBarco]["y1"]==y:
            nuevoJuego["BarcosJ2"][nombreBarco]["xy1"]=1
            agregarCeldasRojas1(x,y)
           
        elif nuevoJuego["BarcosJ2"][nombreBarco]["x2"]==x and nuevoJuego["BarcosJ2"][nombreBarco]["y2"]==y:
            nuevoJuego["BarcosJ2"][nombreBarco]["xy2"]=1
            agregarCeldasRojas1(x,y)
            
        elif nuevoJuego["BarcosJ2"][nombreBarco]["x3"]==x and nuevoJuego["BarcosJ2"][nombreBarco]["y3"]==y:
            nuevoJuego["BarcosJ2"][nombreBarco]["xy3"]=1
            agregarCeldasRojas1(x,y)
         
        if nuevoJuego["BarcosJ2"][nombreBarco]["xy1"]==1 and nuevoJuego["BarcosJ2"][nombreBarco]["xy2"]==1 and nuevoJuego["BarcosJ2"][nombreBarco]["xy3"]==1:
            nuevoJuego["BarcosJ2"][nombreBarco]["vida"]=0
            messagebox.showinfo("Mensaje", "Has hundido un barco") 
            x1=nuevoJuego["BarcosJ2"][nombreBarco]["x1"]
            y1=nuevoJuego["BarcosJ2"][nombreBarco]["y1"]
            x2=nuevoJuego["BarcosJ2"][nombreBarco]["x2"]
            y2=nuevoJuego["BarcosJ2"][nombreBarco]["y2"]
            x3=nuevoJuego["BarcosJ2"][nombreBarco]["x3"]
            y3=nuevoJuego["BarcosJ2"][nombreBarco]["y3"]
            celdasRojasJ1.remove((y1,x1))
            celdasRojasJ1.remove((y2,x2))
            celdasRojasJ1.remove((y3,x3))
            nuevoJuego["Jugador 1"]["Puntaje"]+=3
            nuevoJuego["Jugador 2"]["Cantidad Barcos"]-=1
                  

def mensajeConfirmacion2(nombreBarco:str,x,y):
    """Funcion que muestra mensajes al jugador 2 uno si ha impactado, derribado no barcos del oponente
    """
    global nuevoJuego
    global matrizDisparosJ2
    global celdasRojasJ2
    nuevoJuego["BarcosJ1"][nombreBarco]["disparos"]=1

    if nuevoJuego["BarcosJ1"][nombreBarco]["vida"]==0:
        messagebox.showerror("Mensaje", "No le has dado a ningun barco")
    
    
    elif nombreBarco in ["Destructor1J1","Destructor2J1","Destructor3J1","Destructor4J1","Destructor5J1","Destructor6J1"] and nuevoJuego["BarcosJ1"][nombreBarco]["vida"]==1:
        messagebox.showinfo("Mensaje", "Has dado con un barco")
        if nuevoJuego["BarcosJ1"][nombreBarco]["x1"]==x and nuevoJuego["BarcosJ1"][nombreBarco]["y1"]==y:
            messagebox.showinfo("Mensaje", "Has hundido un barco")
            nuevoJuego["BarcosJ1"][nombreBarco]["vida"]=0
            nuevoJuego["Jugador 2"]["Puntaje"]+=1
            nuevoJuego["Jugador 1"]["Cantidad Barcos"]-=1
        

    elif nombreBarco in ["Crucero1J1","Crucero2J1","Crucero3J1","Crucero4J1"] and nuevoJuego["BarcosJ1"][nombreBarco]["vida"]==1:
        messagebox.showinfo("Mensaje", "Has dado con un barco")
        if nuevoJuego["BarcosJ1"][nombreBarco]["x1"]==x and nuevoJuego["BarcosJ1"][nombreBarco]["y1"]==y:
            nuevoJuego["BarcosJ1"][nombreBarco]["xy1"]=1
            agregarCeldasRojas2(x,y)

        elif nuevoJuego["BarcosJ1"][nombreBarco]["x2"]==x and nuevoJuego["BarcosJ1"][nombreBarco]["y2"]==y:
            nuevoJuego["BarcosJ1"][nombreBarco]["xy2"]=1
            agregarCeldasRojas2(x,y)
            
        if nuevoJuego["BarcosJ1"][nombreBarco]["xy1"]==1 and nuevoJuego["BarcosJ1"][nombreBarco]["xy2"]==1:
            nuevoJuego["BarcosJ1"][nombreBarco]["vida"]=0
            messagebox.showinfo("Mensaje", "Has hundido un barco")
            x1=nuevoJuego["BarcosJ1"][nombreBarco]["x1"]
            y1=nuevoJuego["BarcosJ1"][nombreBarco]["y1"]
            x2=nuevoJuego["BarcosJ1"][nombreBarco]["x2"]
            y2=nuevoJuego["BarcosJ1"][nombreBarco]["y2"]
            celdasRojasJ2.remove((y1,x1))
            celdasRojasJ2.remove((y2,x2))
            nuevoJuego["Jugador 2"]["Puntaje"]+=2
            nuevoJuego["Jugador 1"]["Cantidad Barcos"]-=1

    
    if nombreBarco in ["Acorazado1J1","Acorazado2J1"] and nuevoJuego["BarcosJ1"][nombreBarco]["vida"]==1:
        messagebox.showinfo("Mensaje", "Has dado con un barco")
        if nuevoJuego["BarcosJ1"][nombreBarco]["x1"]==x and nuevoJuego["BarcosJ1"][nombreBarco]["y1"]==y:
            nuevoJuego["BarcosJ1"][nombreBarco]["xy1"]=1
            agregarCeldasRojas2(x,y)

        elif nuevoJuego["BarcosJ1"][nombreBarco]["x2"]==x and nuevoJuego["BarcosJ1"][nombreBarco]["y2"]==y:
            nuevoJuego["BarcosJ1"][nombreBarco]["xy2"]=1
            agregarCeldasRojas2(x,y)

        elif nuevoJuego["BarcosJ1"][nombreBarco]["x3"]==x and nuevoJuego["BarcosJ1"][nombreBarco]["y3"]==y:
            nuevoJuego["BarcosJ1"][nombreBarco]["xy3"]=1
            agregarCeldasRojas2(x,y)

        if nuevoJuego["BarcosJ1"][nombreBarco]["xy1"]==1 and nuevoJuego["BarcosJ1"][nombreBarco]["xy2"]==1 and nuevoJuego["BarcosJ1"][nombreBarco]["xy3"]==1:
            nuevoJuego["BarcosJ1"][nombreBarco]["vida"]=0
            messagebox.showinfo("Mensaje", "Has hundido un barco")
            x1=nuevoJuego["BarcosJ1"][nombreBarco]["x1"]
            y1=nuevoJuego["BarcosJ1"][nombreBarco]["y1"]
            x2=nuevoJuego["BarcosJ1"][nombreBarco]["x2"]
            y2=nuevoJuego["BarcosJ1"][nombreBarco]["y2"]
            x3=nuevoJuego["BarcosJ1"][nombreBarco]["x3"]
            y3=nuevoJuego["BarcosJ1"][nombreBarco]["y3"]
            celdasRojasJ2.remove((y1,x1))
            celdasRojasJ2.remove((y2,x2))
            celdasRojasJ2.remove((y3,x3))
            nuevoJuego["Jugador 2"]["Puntaje"]+=3
            nuevoJuego["Jugador 1"]["Cantidad Barcos"]-=1


def mensajeDisparoFallido():
    """Funcion que informa al jugador si su disparo no ha acertado contra ningun barco del oponente

    Returns:
        bool: Retorna True para continuar el proceso de juego
    """
    messagebox.showerror("Mensaje", "No le has dado a ningun barco")
    return True

def validarDisparoJ1(x,y):
    """Funcion que analiza si el disparo realizado por el jugador 1 ha impactado la flota del jugador 2

    Returns:
        bool: Retorna True para continuar con el juego
    """

    global nuevoJuego

    x=int(x)
    y=int(y)

    if nuevoJuego["BarcosJ2"]["Destructor1J2"]["x1"]==x and nuevoJuego["BarcosJ2"]["Destructor1J2"]["y1"]==y:
        mensajeConfirmacion1("Destructor1J2",x,y)
    elif nuevoJuego["BarcosJ2"]["Destructor2J2"]["x1"]==x and nuevoJuego["BarcosJ2"]["Destructor2J2"]["y1"]==y:
        mensajeConfirmacion1("Destructor2J2",x,y)
    elif nuevoJuego["BarcosJ2"]["Destructor3J2"]["x1"]==x and nuevoJuego["BarcosJ2"]["Destructor3J2"]["y1"]==y:
        mensajeConfirmacion1("Destructor3J2",x,y)
    elif nuevoJuego["BarcosJ2"]["Destructor4J2"]["x1"]==x and nuevoJuego["BarcosJ2"]["Destructor4J2"]["y1"]==y:
        mensajeConfirmacion1("Destructor4J2",x,y)
    elif nuevoJuego["BarcosJ2"]["Destructor5J2"]["x1"]==x and nuevoJuego["BarcosJ2"]["Destructor5J2"]["y1"]==y:
        mensajeConfirmacion1("Destructor5J2",x,y)
    elif nuevoJuego["BarcosJ2"]["Destructor6J2"]["x1"]==x and nuevoJuego["BarcosJ2"]["Destructor6J2"]["y1"]==y:
        mensajeConfirmacion1("Destructor6J2",x,y)

    elif nuevoJuego["BarcosJ2"]["Crucero1J2"]["x1"]==x and nuevoJuego["BarcosJ2"]["Crucero1J2"]["y1"]==y or nuevoJuego["BarcosJ2"]["Crucero1J2"]["x2"]==x and nuevoJuego["BarcosJ2"]["Crucero1J2"]["y2"]==y:
        mensajeConfirmacion1("Crucero1J2",x,y)
    elif nuevoJuego["BarcosJ2"]["Crucero2J2"]["x1"]==x and nuevoJuego["BarcosJ2"]["Crucero2J2"]["y1"]==y or nuevoJuego["BarcosJ2"]["Crucero2J2"]["x2"]==x and nuevoJuego["BarcosJ2"]["Crucero2J2"]["y2"]==y:
        mensajeConfirmacion1("Crucero2J2",x,y)
    elif nuevoJuego["BarcosJ2"]["Crucero3J2"]["x1"]==x and nuevoJuego["BarcosJ2"]["Crucero3J2"]["y1"]==y or nuevoJuego["BarcosJ2"]["Crucero3J2"]["x2"]==x and nuevoJuego["BarcosJ2"]["Crucero3J2"]["y2"]==y:
        mensajeConfirmacion1("Crucero3J2",x,y)
    elif nuevoJuego["BarcosJ2"]["Crucero4J2"]["x1"]==x and nuevoJuego["BarcosJ2"]["Crucero4J2"]["y1"]==y or nuevoJuego["BarcosJ2"]["Crucero4J2"]["x2"]==x and nuevoJuego["BarcosJ2"]["Crucero4J2"]["y2"]==y:
        mensajeConfirmacion1("Crucero4J2",x,y)  

    elif nuevoJuego["BarcosJ2"]["Acorazado1J2"]["x1"]==x and nuevoJuego["BarcosJ2"]["Acorazado1J2"]["y1"]==y or nuevoJuego["BarcosJ2"]["Acorazado1J2"]["x2"]==x and nuevoJuego["BarcosJ2"]["Acorazado1J2"]["y2"]==y or nuevoJuego["BarcosJ2"]["Acorazado1J2"]["x3"]==x and nuevoJuego["BarcosJ2"]["Acorazado1J2"]["y3"]==y:
        mensajeConfirmacion1("Acorazado1J2",x,y)
    elif nuevoJuego["BarcosJ2"]["Acorazado2J2"]["x1"]==x and nuevoJuego["BarcosJ2"]["Acorazado2J2"]["y1"]==y or nuevoJuego["BarcosJ2"]["Acorazado2J2"]["x2"]==x and nuevoJuego["BarcosJ2"]["Acorazado2J2"]["y2"]==y or nuevoJuego["BarcosJ2"]["Acorazado2J2"]["x3"]==x and nuevoJuego["BarcosJ2"]["Acorazado2J2"]["y3"]==y:
        mensajeConfirmacion1("Acorazado2J2",x,y)
    else:
        mensajeDisparoFallido()
    
    return True

def validarDisparoJ2(x,y):
    """Funcion que analiza si el disparo realizado por el jugador 2 ha impactado la flota del jugador 2

    Returns:
        bool: Retorna True para continuar con el juego
    """
    global nuevoJuego
  
    x=int(x)
    y=int(y)
  

    if nuevoJuego["BarcosJ1"]["Destructor1J1"]["x1"]==x and nuevoJuego["BarcosJ1"]["Destructor1J1"]["y1"]==y:
        mensajeConfirmacion2("Destructor1J1",x,y)
    elif nuevoJuego["BarcosJ1"]["Destructor2J1"]["x1"]==x and nuevoJuego["BarcosJ1"]["Destructor2J1"]["y1"]==y:
        mensajeConfirmacion2("Destructor2J1",x,y)
    elif nuevoJuego["BarcosJ1"]["Destructor3J1"]["x1"]==x and nuevoJuego["BarcosJ1"]["Destructor3J1"]["y1"]==y:
        mensajeConfirmacion2("Destructor3J1",x,y)
    elif nuevoJuego["BarcosJ1"]["Destructor4J1"]["x1"]==x and nuevoJuego["BarcosJ1"]["Destructor4J1"]["y1"]==y:
        mensajeConfirmacion2("Destructor4J1",x,y)
    elif nuevoJuego["BarcosJ1"]["Destructor5J1"]["x1"]==x and nuevoJuego["BarcosJ1"]["Destructor5J1"]["y1"]==y:
        mensajeConfirmacion2("Destructor5J1",x,y)
    elif nuevoJuego["BarcosJ1"]["Destructor6J1"]["x1"]==x and nuevoJuego["BarcosJ1"]["Destructor6J1"]["y1"]==y:
        mensajeConfirmacion2("Destructor6J1",x,y)

    elif nuevoJuego["BarcosJ1"]["Crucero1J1"]["x1"]==x and nuevoJuego["BarcosJ1"]["Crucero1J1"]["y1"]==y or nuevoJuego["BarcosJ1"]["Crucero1J1"]["x2"]==x and nuevoJuego["BarcosJ1"]["Crucero1J1"]["y2"]==y:
        mensajeConfirmacion2("Crucero1J1",x,y)
    elif nuevoJuego["BarcosJ1"]["Crucero2J1"]["x1"]==x and nuevoJuego["BarcosJ1"]["Crucero2J1"]["y1"]==y or nuevoJuego["BarcosJ1"]["Crucero2J1"]["x2"]==x and nuevoJuego["BarcosJ1"]["Crucero2J1"]["y2"]==y:
        mensajeConfirmacion2("Crucero2J1",x,y)
    elif nuevoJuego["BarcosJ1"]["Crucero3J1"]["x1"]==x and nuevoJuego["BarcosJ1"]["Crucero3J1"]["y1"]==y or nuevoJuego["BarcosJ1"]["Crucero3J1"]["x2"]==x and nuevoJuego["BarcosJ1"]["Crucero3J1"]["y2"]==y:
        mensajeConfirmacion2("Crucero3J1",x,y)
    elif nuevoJuego["BarcosJ1"]["Crucero4J1"]["x1"]==x and nuevoJuego["BarcosJ1"]["Crucero4J1"]["y1"]==y or nuevoJuego["BarcosJ1"]["Crucero4J1"]["x2"]==x and nuevoJuego["BarcosJ1"]["Crucero4J1"]["y2"]==y:
        mensajeConfirmacion2("Crucero4J1",x,y)
    
    elif nuevoJuego["BarcosJ1"]["Acorazado1J1"]["x1"]==x and nuevoJuego["BarcosJ1"]["Acorazado1J1"]["y1"]==y or nuevoJuego["BarcosJ1"]["Acorazado1J1"]["x2"]==x and nuevoJuego["BarcosJ1"]["Acorazado1J1"]["y2"]==y or nuevoJuego["BarcosJ1"]["Acorazado1J1"]["x3"]==x and nuevoJuego["BarcosJ1"]["Acorazado1J1"]["y3"]==y:
        mensajeConfirmacion2("Acorazado1J1",x,y)
    elif nuevoJuego["BarcosJ1"]["Acorazado2J1"]["x1"]==x and nuevoJuego["BarcosJ1"]["Acorazado2J1"]["y1"]==y or nuevoJuego["BarcosJ1"]["Acorazado2J1"]["x2"]==x and nuevoJuego["BarcosJ1"]["Acorazado2J1"]["y2"]==y or nuevoJuego["BarcosJ1"]["Acorazado2J1"]["x3"]==x and nuevoJuego["BarcosJ1"]["Acorazado2J1"]["y3"]==y:
        mensajeConfirmacion2("Acorazado2J1",x,y)
    else:
        mensajeDisparoFallido()
    
    return True 

matrizJ1 = []
matrizJ2 = []

izquierda= 3
derecha= 1
arriba= 2
abajo= 4

x = nuevoJuego["Matriz"]["Columnas"]
y = nuevoJuego["Matriz"]["Filas"]
limitesTablero= []

def colocarDestructores():
    """Función que coloca los destructores en la matriz de juego, segun la posicion en la que se guardaron
    """
    global nuevoJuego
    global matrizJ1
    global matrizJ2
    
    global izquierda
    global derecha
    global arriba
    global abajo

    global destructorHaciaArriba
    global destructorHaciaAbajo
    global destructorHaciaDerecha
    global destructorHaciaIzquierda

    for barco in nuevoJuego["BarcosJ1"].keys():       # Se ejecuta la funcion colocarDestructores para jugador 1
        if (barco in ["Destructor1J1", "Destructor2J1", "Destructor3J1", "Destructor4J1", "Destructor5J1", "Destructor6J1"]):
            x = nuevoJuego["BarcosJ1"][barco]["x1"]
            y = nuevoJuego["BarcosJ1"][barco]["y1"]
            orientacion = nuevoJuego["BarcosJ1"][barco]["orientacion"]

            if (nuevoJuego["BarcosJ1"][barco]["vida"]==0):        # Se valida si el barco aun sigue a flote o ya fue hundido
                "matrizJ1[y][x].configure(image = vacio)"
              
                pass

            elif (orientacion==izquierda):          # Se valida la orientacion del barco para colocarlo
                orientacionBarco= destructorHaciaIzquierda
                matrizJ1[y][x].configure(image= orientacionBarco)

            elif (orientacion==derecha):            # Se valida la orientacion del barco para colocarlo
                orientacionBarco= destructorHaciaDerecha
                matrizJ1[y][x].configure(image= orientacionBarco)

            elif (orientacion==abajo):              # Se valida la orientacion del barco para colocarlo
                orientacionBarco= destructorHaciaAbajo
                matrizJ1[y][x].configure(image= orientacionBarco)

            elif (orientacion==arriba):             # Se valida la orientacion del barco para colocarlo
                orientacionBarco= destructorHaciaArriba
                matrizJ1[y][x].configure(image= orientacionBarco)

    for barco in nuevoJuego["BarcosJ2"].keys():       # Se ejecuta la funcion colocarDestructores para jugador 2
        if (barco in ["Destructor1J2", "Destructor2J2", "Destructor3J2", "Destructor4J2", "Destructor5J2", "Destructor6J2"]):
                x= nuevoJuego["BarcosJ2"][barco]["x1"]
                y= nuevoJuego["BarcosJ2"][barco]["y1"]
                orientacion= nuevoJuego["BarcosJ2"][barco]["orientacion"]

                if (nuevoJuego["BarcosJ2"][barco]["vida"]==0):        # Se valida si el barco aun sigue a flote o ya fue hundido
                    "matrizJ2[y][x].configure(image = vacio)"
                 
                    pass

                elif (orientacion==izquierda):          # Se valida la orientacion del barco para colocarlo
                    orientacionBarco= destructorHaciaIzquierda
                    matrizJ2[y][x].configure(image= orientacionBarco)

                elif (orientacion==derecha):            # Se valida la orientacion del barco para colocarlo
                    orientacionBarco= destructorHaciaDerecha
                    matrizJ2[y][x].configure(image= orientacionBarco)

                elif (orientacion==abajo):              # Se valida la orientacion del barco para colocarlo
                    orientacionBarco= destructorHaciaAbajo
                    matrizJ2[y][x].configure(image= orientacionBarco)

                elif (orientacion==arriba):             # Se valida la orientacion del barco para colocarlo
                    orientacionBarco= destructorHaciaArriba
                    matrizJ2[y][x].configure(image= orientacionBarco)

def colocarCruceros():
    """Función que coloca los cruceros en la matriz de juego, segun la posicion en la que se guardaron
    """
    global nuevoJuego
    global matrizJ1
    global matrizJ2

    global cruceroHaciaDerecha1
    global cruceroHaciaIzquierda1
    global cruceroHaciaAbajo1
    global cruceroHaciaArriba1

    global cruceroHaciaDerecha2
    global cruceroHaciaIzquierda2
    global cruceroHaciaAbajo2
    global cruceroHaciaArriba2

    for barco in nuevoJuego["BarcosJ1"].keys():       # Se ejecuta la funcion colocarCruceros para jugador 1
        if (barco in ["Crucero1J1", "Crucero2J1", "Crucero3J1", "Crucero4J1"]):
            x1 = nuevoJuego["BarcosJ1"][barco]["x1"]
            y1 = nuevoJuego["BarcosJ1"][barco]["y1"]
            x2 = nuevoJuego["BarcosJ1"][barco]["x2"]
            y2 = nuevoJuego["BarcosJ1"][barco]["y2"]
            orientacion = nuevoJuego["BarcosJ1"][barco]["orientacion"]

            if (nuevoJuego["BarcosJ1"][barco]["vida"]==0):        # Se valida si el barco aun sigue a flote o ya fue hundido
                #matrizJ1[y1][x1].configure(image = vacio)
                #matrizJ1[y2][x2].configure(image = vacio)
                pass
            elif (orientacion==izquierda):          # Se valida la orientacion del barco para colocarlo
                orientacionbarco1 = cruceroHaciaIzquierda1
                orientacionbarco2 = cruceroHaciaIzquierda2
                matrizJ1[y1][x1].configure(image = orientacionbarco1)
                matrizJ1[y2][x2].configure(image = orientacionbarco2)

            elif (orientacion==derecha):            # Se valida la orientacion del barco para colocarlo
                orientacionbarco1 = cruceroHaciaDerecha1
                orientacionbarco2 = cruceroHaciaDerecha2
                matrizJ1[y1][x1].configure(image = orientacionbarco1)
                matrizJ1[y2][x2].configure(image = orientacionbarco2)

            elif (orientacion==abajo):          # Se valida la orientacion del barco para colocarlo
                orientacionbarco1 = cruceroHaciaAbajo1
                orientacionbarco2 = cruceroHaciaAbajo2
                matrizJ1[y1][x1].configure(image = orientacionbarco1)
                matrizJ1[y2][x2].configure(image = orientacionbarco2)

            elif (orientacion==arriba):         # Se valida la orientacion del barco para colocarlo
                orientacionbarco1 = cruceroHaciaArriba1
                orientacionbarco2 = cruceroHaciaArriba2
                matrizJ1[y1][x1].configure(image = orientacionbarco1)
                matrizJ1[y2][x2].configure(image = orientacionbarco2)

    for barco in nuevoJuego["BarcosJ2"].keys():       # Se ejecuta la funcion colocarCruceros para jugador 2
        if (barco in ["Crucero1J2", "Crucero2J2", "Crucero3J2", "Crucero4J2"]):
            x1 = nuevoJuego["BarcosJ2"][barco]["x1"]
            y1 = nuevoJuego["BarcosJ2"][barco]["y1"]
            x2 = nuevoJuego["BarcosJ2"][barco]["x2"]
            y2 = nuevoJuego["BarcosJ2"][barco]["y2"]
            orientacion = nuevoJuego["BarcosJ2"][barco]["orientacion"]

            if (nuevoJuego["BarcosJ2"][barco]["vida"]==0):        # Se valida si el barco aun sigue a flote o ya fue hundido
                #matrizJ2[y1][x1].configure(image = vacio)
               # matrizJ2[y2][x2].configure(image = vacio)
                pass
            elif (orientacion==izquierda):          # Se valida la orientacion del barco para colocarlo
                orientacionbarco1 = cruceroHaciaIzquierda1
                orientacionbarco2 = cruceroHaciaIzquierda2
                matrizJ2[y1][x1].configure(image = orientacionbarco1)
                matrizJ2[y2][x2].configure(image = orientacionbarco2)

            elif (orientacion==derecha):            # Se valida la orientacion del barco para colocarlo
                orientacionbarco1 = cruceroHaciaDerecha1
                orientacionbarco2 = cruceroHaciaDerecha2
                matrizJ2[y1][x1].configure(image = orientacionbarco1)
                matrizJ2[y2][x2].configure(image = orientacionbarco2)

            elif (orientacion==abajo):              # Se valida la orientacion del barco para colocarlo
                orientacionbarco1 = cruceroHaciaAbajo1
                orientacionbarco2 = cruceroHaciaAbajo2
                matrizJ2[y1][x1].configure(image = orientacionbarco1)
                matrizJ2[y2][x2].configure(image = orientacionbarco2)

            elif (orientacion==arriba):             # Se valida la orientacion del barco para colocarlo
                orientacionbarco1 = cruceroHaciaArriba1
                orientacionbarco2 = cruceroHaciaArriba2
                matrizJ2[y1][x1].configure(image = orientacionbarco1)
                matrizJ2[y2][x2].configure(image = orientacionbarco2)

def colocarAcorazados():
    """Función que coloca los acorazados en la matriz de juego, segun la posicion en la que se guardaron
    """
    global nuevoJuego
    global matrizJ1
    global matrizJ2
    #Acorazado 1
    global acorazadoHaciaDerecha1
    global acorazadoHaciaIzquierda1
    global acorazadoHaciaArriba1
    global acorazadoHaciaAbajo1
    #Acorazado 2
    global acorazadoHaciaDerecha2
    global acorazadoHaciaIzquierda2
    global acorazadoHaciaArriba2
    global acorazadoHaciaAbajo2
    #Acorazado 3
    global acorazadoHaciaDerecha3
    global acorazadoHaciaIzquierda3
    global acorazadoHaciaArriba3
    global acorazadoHaciaAbajo3
    
    for barco in nuevoJuego["BarcosJ1"].keys():       # Se ejecuta la funcion colocarAcorazados para jugador 1
        if (barco in ["Acorazado1J1", "Acorazado2J1"]):
            x1 = nuevoJuego["BarcosJ1"][barco]["x1"]
            y1 = nuevoJuego["BarcosJ1"][barco]["y1"]
            x2 = nuevoJuego["BarcosJ1"][barco]["x2"]
            y2 = nuevoJuego["BarcosJ1"][barco]["y2"]
            x3 = nuevoJuego["BarcosJ1"][barco]["x3"]
            y3 = nuevoJuego["BarcosJ1"][barco]["y3"]
            orientacion = nuevoJuego["BarcosJ1"][barco]["orientacion"]

            if (nuevoJuego["BarcosJ1"][barco]["vida"]==0):        # Se valida si el barco aun sigue a flote o ya fue hundido
                #matrizJ1[y1][x1].configure(image = vacio)
                #matrizJ1[y2][x2].configure(image = vacio)
                #matrizJ1[y3][x3].configure(image = vacio)   
                pass
            elif (orientacion==izquierda):          # Se valida la orientacion del barco para colocarlo
                orientacionbarco1 = acorazadoHaciaIzquierda1
                orientacionbarco2 = acorazadoHaciaIzquierda2
                orientacionbarco3 = acorazadoHaciaIzquierda3
                matrizJ1[y1][x1].configure(image = orientacionbarco1)
                matrizJ1[y2][x2].configure(image = orientacionbarco2)
                matrizJ1[y3][x3].configure(image = orientacionbarco3)

            elif (orientacion==derecha):          # Se valida la orientacion del barco para colocarlo
                orientacionbarco1 = acorazadoHaciaDerecha1
                orientacionbarco2 = acorazadoHaciaDerecha2
                orientacionbarco3 = acorazadoHaciaDerecha3
                matrizJ1[y1][x1].configure(image = orientacionbarco1)
                matrizJ1[y2][x2].configure(image = orientacionbarco2)
                matrizJ1[y3][x3].configure(image = orientacionbarco3)

            elif (orientacion==abajo):            # Se valida la orientacion del barco para colocarlo
                orientacionbarco1 = acorazadoHaciaAbajo1
                orientacionbarco2 = acorazadoHaciaAbajo2
                orientacionbarco3 = acorazadoHaciaAbajo3
                matrizJ1[y1][x1].configure(image = orientacionbarco1)
                matrizJ1[y2][x2].configure(image = orientacionbarco2)
                matrizJ1[y3][x3].configure(image = orientacionbarco3)

            elif (orientacion==arriba):          # Se valida la orientacion del barco para colocarlo
                orientacionbarco1 = acorazadoHaciaArriba1
                orientacionbarco2 = acorazadoHaciaArriba2
                orientacionbarco3 = acorazadoHaciaArriba3
                matrizJ1[y1][x1].configure(image = orientacionbarco1)
                matrizJ1[y2][x2].configure(image = orientacionbarco2)
                matrizJ1[y3][x3].configure(image = orientacionbarco3)

    for barco in nuevoJuego["BarcosJ2"].keys():       # Se ejecuta la funcion colocarAcorazados para jugador 2
        if (barco in ["Acorazado1J2", "Acorazado2J2"]):
                x1 = nuevoJuego["BarcosJ2"][barco]["x1"]
                y1 = nuevoJuego["BarcosJ2"][barco]["y1"]
                x2 = nuevoJuego["BarcosJ2"][barco]["x2"]
                y2 = nuevoJuego["BarcosJ2"][barco]["y2"]
                x3 = nuevoJuego["BarcosJ2"][barco]["x3"]
                y3 = nuevoJuego["BarcosJ2"][barco]["y3"]
                orientacion = nuevoJuego["BarcosJ2"][barco]["orientacion"]

                if (nuevoJuego["BarcosJ2"][barco]["vida"]==0):        # Se valida si el barco aun sigue a flote o ya fue hundido
                    #matrizJ2[y1][x1].configure(image = vacio)
                    #matrizJ2[y2][x2].configure(image = vacio)
                    #matrizJ2[y3][x3].configure(image = vacio)
                    pass
                elif (orientacion==izquierda):          # Se valida la orientacion del barco para colocarlo
                    orientacionbarco1 = acorazadoHaciaIzquierda1
                    orientacionbarco2 = acorazadoHaciaIzquierda2
                    orientacionbarco3 = acorazadoHaciaIzquierda3
                    matrizJ2[y1][x1].configure(image = orientacionbarco1)
                    matrizJ2[y2][x2].configure(image = orientacionbarco2)
                    matrizJ2[y3][x3].configure(image = orientacionbarco3)

                elif (orientacion==derecha):            # Se valida la orientacion del barco para colocarlo
                    orientacionbarco1 = acorazadoHaciaDerecha1
                    orientacionbarco2 = acorazadoHaciaDerecha2
                    orientacionbarco3 = acorazadoHaciaDerecha3
                    matrizJ2[y1][x1].configure(image = orientacionbarco1)
                    matrizJ2[y2][x2].configure(image = orientacionbarco2)
                    matrizJ2[y3][x3].configure(image = orientacionbarco3)

                elif (orientacion==abajo):          # Se valida la orientacion del barco para colocarlo
                    orientacionbarco1 = acorazadoHaciaAbajo1
                    orientacionbarco2 = acorazadoHaciaAbajo2
                    orientacionbarco3 = acorazadoHaciaAbajo3
                    matrizJ2[y1][x1].configure(image = orientacionbarco1)
                    matrizJ2[y2][x2].configure(image = orientacionbarco2)
                    matrizJ2[y3][x3].configure(image = orientacionbarco3)

                elif (orientacion==arriba):         # Se valida la orientacion del barco para colocarlo
                    orientacionbarco1 = acorazadoHaciaArriba1
                    orientacionbarco2 = acorazadoHaciaArriba2
                    orientacionbarco3 = acorazadoHaciaArriba3
                    matrizJ2[y1][x1].configure(image = orientacionbarco1)
                    matrizJ2[y2][x2].configure(image = orientacionbarco2)
                    matrizJ2[y3][x3].configure(image = orientacionbarco3)
    
                

def colocarBarcos():
    """Funcion que itera en los jugadores para agregar los barcos a los tableros
    """
    colocarDestructores()
    colocarCruceros()
    colocarAcorazados()
    return True

def accionesMovimiento():
    """Función que itera en los barcos para que ingresen a la funcion de movimiento
    """
    movimientoDestructores()
    movimientoCruceros()
    movimientoAcorazados()
    return True

def movimientoDestructores():
    """Función encargada de validar y realizar los movimientos sobre los Destructores
    """
    global nuevoJuego
    global matrizJ1
    global matrizJ2

    for barco in nuevoJuego["BarcosJ1"].keys():       # Se ejecuta la funcion movimientoDestructores para los barcos del jugador 1
        if (barco in ["Destructor1J1", "Destructor2J1", "Destructor3J1", "Destructor4J1", "Destructor5J1", "Destructor6J1"]):
            y= nuevoJuego["BarcosJ1"][barco]["y1"]
            x= nuevoJuego["BarcosJ1"][barco]["x1"]
            listaPosicionesBarcos= listaPosicionesActualesBarcos(nuevoJuego["BarcosJ1"])
            if (nuevoJuego["BarcosJ1"][barco]["vida"]==0):        # Se valida si el barco aun sigue a flote o ya fue hundido
                matrizJ1[y][x].configure(image = vacio)
                pass 

            elif (nuevoJuego["BarcosJ1"][barco]["disparos"]!=0):      # Se valida si el barco ya recibio un disparo
                pass

            elif (nuevoJuego["BarcosJ1"][barco]["orientacion"]==arriba):      # Se valida la orientacion del barco para moverlo
                if (listaPosicionesBarcos.count((x,y-1))==0 and listaPosicionesBarcos.count((x,y-2))==0 and y-2 >=0): # Se valida si puede avanzar 2 casillas
                    matrizJ1[y][x].configure(image= vacio)
                    matrizJ1[y-2][x].configure(image= destructorHaciaArriba)
                    nuevoJuego["BarcosJ1"][barco]["y1"]= nuevoJuego["BarcosJ1"][barco]["y1"]-2
                    nuevoJuego["BarcosJ1"][barco]["movimiento"] = 1
                elif (nuevoJuego["BarcosJ1"][barco]["y1"]==0):                  # Se valida si el barco esta en un borde
                    nuevoJuego["BarcosJ1"][barco]["orientacion"]= abajo
                    matrizJ1[y][x].configure(image= destructorHaciaAbajo)
                elif(listaPosicionesBarcos.count((x,y-1))>=1):  # Se valida si la posicion donde avanzará el barco está disponible
                    if (nuevoJuego["BarcosJ1"][barco]["movimiento"]==0):
                        nuevoJuego["BarcosJ1"][barco]["orientacion"]= abajo
                        matrizJ1[y][x].configure(image= destructorHaciaAbajo)
                        nuevoJuego["BarcosJ1"][barco]["movimiento"] = 1
                    else:
                        nuevoJuego["BarcosJ1"][barco]["movimiento"] = 0
                else:
                    matrizJ1[y][x].configure(image= vacio)
                    matrizJ1[y-1][x].configure(image= destructorHaciaArriba)
                    nuevoJuego["BarcosJ1"][barco]["y1"]= nuevoJuego["BarcosJ1"][barco]["y1"]-1
                    nuevoJuego["BarcosJ1"][barco]["movimiento"] = 1

            elif (nuevoJuego["BarcosJ1"][barco]["orientacion"]==abajo):       # Se valida la orientacion del barco para moverlo
                if (listaPosicionesBarcos.count((x,y+1))==0 and listaPosicionesBarcos.count((x,y+2))==0 and y+2 <= limitesTablero[1]-1): # Se valida si puede avanzar 2 casillas
                    matrizJ1[y][x].configure(image= vacio)
                    matrizJ1[y+2][x].configure(image= destructorHaciaAbajo)
                    nuevoJuego["BarcosJ1"][barco]["y1"]= nuevoJuego["BarcosJ1"][barco]["y1"]+2
                    nuevoJuego["BarcosJ1"][barco]["movimiento"] = 1
                elif (nuevoJuego["BarcosJ1"][barco]["y1"]==limitesTablero[1]-1):# Se valida si el barco esta en un borde
                    nuevoJuego["BarcosJ1"][barco]["orientacion"]= arriba
                    matrizJ1[y][x].configure(image= destructorHaciaArriba)
                elif(listaPosicionesBarcos.count((x,y+1))>=1):  # Se valida si la posicion donde avanzará el barco está disponible
                    if (nuevoJuego["BarcosJ1"][barco]["movimiento"]==0):
                        nuevoJuego["BarcosJ1"][barco]["orientacion"]= arriba
                        matrizJ1[y][x].configure(image= destructorHaciaArriba)
                        nuevoJuego["BarcosJ1"][barco]["movimiento"] = 1
                    else:
                        nuevoJuego["BarcosJ1"][barco]["movimiento"] = 0
                else:
                    matrizJ1[y][x].configure(image= vacio)
                    matrizJ1[y+1][x].configure(image= destructorHaciaAbajo)
                    nuevoJuego["BarcosJ1"][barco]["y1"]= nuevoJuego["BarcosJ1"][barco]["y1"]+1
                    nuevoJuego["BarcosJ1"][barco]["movimiento"] = 1

            elif (nuevoJuego["BarcosJ1"][barco]["orientacion"]==izquierda):       # Se valida la orientacion del barco para moverlo
                if (listaPosicionesBarcos.count((x-1,y))==0 and listaPosicionesBarcos.count((x-2,y))==0 and x-2 >=0): # Se valida si puede avanzar 2 casillas
                    matrizJ1[y][x].configure(image= vacio)
                    matrizJ1[y][x-2].configure(image= destructorHaciaIzquierda)
                    nuevoJuego["BarcosJ1"][barco]["x1"]= nuevoJuego["BarcosJ1"][barco]["x1"]-2
                    nuevoJuego["BarcosJ1"][barco]["movimiento"] = 1
                elif (nuevoJuego["BarcosJ1"][barco]["x1"]==0):                      # Se valida si el barco esta en un borde
                    nuevoJuego["BarcosJ1"][barco]["orientacion"]= derecha
                    matrizJ1[y][x].configure(image= destructorHaciaDerecha)
                elif(listaPosicionesBarcos.count((x-1,y))>=1):      # Se valida si la posicion donde avanzará el barco está disponible
                    if (nuevoJuego["BarcosJ1"][barco]["movimiento"]==0):
                        nuevoJuego["BarcosJ1"][barco]["orientacion"]= derecha
                        matrizJ1[y][x].configure(image= destructorHaciaDerecha)
                        nuevoJuego["BarcosJ1"][barco]["movimiento"] = 1
                    else:
                        nuevoJuego["BarcosJ1"][barco]["movimiento"] = 0
                else:
                    matrizJ1[y][x].configure(image= vacio)
                    matrizJ1[y][x-1].configure(image= destructorHaciaIzquierda)
                    nuevoJuego["BarcosJ1"][barco]["x1"]= nuevoJuego["BarcosJ1"][barco]["x1"]-1
                    nuevoJuego["BarcosJ1"][barco]["movimiento"] = 1

            elif (nuevoJuego["BarcosJ1"][barco]["orientacion"]==derecha):     # Se valida la orientacion del barco para moverlo
                if (listaPosicionesBarcos.count((x+1,y))==0 and listaPosicionesBarcos.count((x+2,y))==0 and x+2 <= limitesTablero[0]-1): # Se valida si puede avanzar 2 casillas
                    matrizJ1[y][x].configure(image= vacio)
                    matrizJ1[y][x+2].configure(image= destructorHaciaDerecha)
                    nuevoJuego["BarcosJ1"][barco]["x1"]= nuevoJuego["BarcosJ1"][barco]["x1"]+2
                    nuevoJuego["BarcosJ1"][barco]["movimiento"] = 1
                elif (nuevoJuego["BarcosJ1"][barco]["x1"]==limitesTablero[0]-1):# Se valida si el barco esta en un borde
                    nuevoJuego["BarcosJ1"][barco]["orientacion"]= izquierda
                    matrizJ1[y][x].configure(image= destructorHaciaIzquierda)
                elif(listaPosicionesBarcos.count((x+1,y))>=1):  # Se valida si la posicion donde avanzará el barco está disponible
                    if (nuevoJuego["BarcosJ1"][barco]["movimiento"]==0):
                        nuevoJuego["BarcosJ1"][barco]["orientacion"]= izquierda
                        matrizJ1[y][x].configure(image= destructorHaciaIzquierda)
                        nuevoJuego["BarcosJ1"][barco]["movimiento"] = 1
                    else:
                        nuevoJuego["BarcosJ1"][barco]["movimiento"] = 0
                else:
                    matrizJ1[y][x].configure(image= vacio)
                    matrizJ1[y][x+1].configure(image= destructorHaciaDerecha)
                    nuevoJuego["BarcosJ1"][barco]["x1"]= nuevoJuego["BarcosJ1"][barco]["x1"]+1
                    nuevoJuego["BarcosJ1"][barco]["movimiento"] = 1

    for barco in nuevoJuego["BarcosJ2"].keys():       # Se ejecuta la funcion movimientoDestructores para los barcos del jugador 2
        if (barco in ["Destructor1J2", "Destructor2J2", "Destructor3J2", "Destructor4J2", "Destructor5J2", "Destructor6J2"]):
            y= nuevoJuego["BarcosJ2"][barco]["y1"]
            x= nuevoJuego["BarcosJ2"][barco]["x1"]
            listaPosicionesBarcos= listaPosicionesActualesBarcos(nuevoJuego["BarcosJ2"])
            if (nuevoJuego["BarcosJ2"][barco]["vida"]==0):        # Se valida si el barco aun sigue a flote o ya fue hundido
                matrizJ2[y][x].configure(image = vacio)
                pass 

            elif (nuevoJuego["BarcosJ2"][barco]["disparos"]!=0):      # Se valida si el barco ya recibio un disparo
                pass

            elif (nuevoJuego["BarcosJ2"][barco]["orientacion"]==arriba):      # Se valida la orientacion del barco para moverlo
                if (listaPosicionesBarcos.count((x,y-1))==0 and listaPosicionesBarcos.count((x,y-2))==0 and y-2 >=0): # Se valida si puede avanzar 2 casillas
                    matrizJ2[y][x].configure(image= vacio)
                    matrizJ2[y-2][x].configure(image= destructorHaciaArriba)
                    nuevoJuego["BarcosJ2"][barco]["y1"]= nuevoJuego["BarcosJ2"][barco]["y1"]-2
                    nuevoJuego["BarcosJ2"][barco]["movimiento"] = 1
                elif (nuevoJuego["BarcosJ2"][barco]["y1"]==0):                  # Se valida si el barco esta en un borde
                    nuevoJuego["BarcosJ2"][barco]["orientacion"]= abajo
                    matrizJ2[y][x].configure(image= destructorHaciaAbajo)
                elif(listaPosicionesBarcos.count((x,y-1))>=1):  # Se valida si la posicion donde avanzará el barco está disponible
                    if (nuevoJuego["BarcosJ2"][barco]["movimiento"]==0):
                        nuevoJuego["BarcosJ2"][barco]["orientacion"]= abajo
                        matrizJ2[y][x].configure(image= destructorHaciaAbajo)
                        nuevoJuego["BarcosJ2"][barco]["movimiento"] = 1
                    else:
                        nuevoJuego["BarcosJ2"][barco]["movimiento"] = 0
                else:
                    matrizJ2[y][x].configure(image= vacio)
                    matrizJ2[y-1][x].configure(image= destructorHaciaArriba)
                    nuevoJuego["BarcosJ2"][barco]["y1"]= nuevoJuego["BarcosJ2"][barco]["y1"]-1
                    nuevoJuego["BarcosJ2"][barco]["movimiento"] = 1

            elif (nuevoJuego["BarcosJ2"][barco]["orientacion"]==abajo):       # Se valida la orientacion del barco para moverlo
                if (listaPosicionesBarcos.count((x,y+1))==0 and listaPosicionesBarcos.count((x,y+2))==0 and y+2 <= limitesTablero[1]-1): # Se valida si puede avanzar 2 casillas
                    matrizJ2[y][x].configure(image= vacio)
                    matrizJ2[y+2][x].configure(image= destructorHaciaAbajo)
                    nuevoJuego["BarcosJ2"][barco]["y1"]= nuevoJuego["BarcosJ2"][barco]["y1"]+2
                    nuevoJuego["BarcosJ2"][barco]["movimiento"] = 1
                elif (nuevoJuego["BarcosJ2"][barco]["y1"]==limitesTablero[1]-1):# Se valida si el barco esta en un borde
                    nuevoJuego["BarcosJ2"][barco]["orientacion"]= arriba
                    matrizJ2[y][x].configure(image= destructorHaciaArriba)
                elif(listaPosicionesBarcos.count((x,y+1))>=1):  # Se valida si la posicion donde avanzará el barco está disponible
                    if (nuevoJuego["BarcosJ2"][barco]["movimiento"]==0):
                        nuevoJuego["BarcosJ2"][barco]["orientacion"]= arriba
                        matrizJ2[y][x].configure(image= destructorHaciaArriba)
                        nuevoJuego["BarcosJ2"][barco]["movimiento"] = 1
                    else:
                        nuevoJuego["BarcosJ2"][barco]["movimiento"] = 0
                else:
                    matrizJ2[y][x].configure(image= vacio)
                    matrizJ2[y+1][x].configure(image= destructorHaciaAbajo)
                    nuevoJuego["BarcosJ2"][barco]["y1"]= nuevoJuego["BarcosJ2"][barco]["y1"]+1
                    nuevoJuego["BarcosJ2"][barco]["movimiento"] = 1

            elif (nuevoJuego["BarcosJ2"][barco]["orientacion"]==izquierda):       # Se valida la orientacion del barco para moverlo
                if (listaPosicionesBarcos.count((x-1,y))==0 and listaPosicionesBarcos.count((x-2,y))==0 and x-2 >=0): # Se valida si puede avanzar 2 casillas
                    matrizJ2[y][x].configure(image= vacio)
                    matrizJ2[y][x-2].configure(image= destructorHaciaIzquierda)
                    nuevoJuego["BarcosJ2"][barco]["x1"]= nuevoJuego["BarcosJ2"][barco]["x1"]-2
                    nuevoJuego["BarcosJ2"][barco]["movimiento"] = 1
                elif (nuevoJuego["BarcosJ2"][barco]["x1"]==0):                      # Se valida si el barco esta en un borde
                    nuevoJuego["BarcosJ2"][barco]["orientacion"]= derecha
                    matrizJ2[y][x].configure(image= destructorHaciaDerecha)
                elif(listaPosicionesBarcos.count((x-1,y))>=1):      # Se valida si la posicion donde avanzará el barco está disponible
                    if (nuevoJuego["BarcosJ2"][barco]["movimiento"]==0):
                        nuevoJuego["BarcosJ2"][barco]["orientacion"]= derecha
                        matrizJ2[y][x].configure(image= destructorHaciaDerecha)
                        nuevoJuego["BarcosJ2"][barco]["movimiento"] = 1
                    else:
                        nuevoJuego["BarcosJ2"][barco]["movimiento"] = 0
                else:
                    matrizJ2[y][x].configure(image= vacio)
                    matrizJ2[y][x-1].configure(image= destructorHaciaIzquierda)
                    nuevoJuego["BarcosJ2"][barco]["x1"]= nuevoJuego["BarcosJ2"][barco]["x1"]-1
                    nuevoJuego["BarcosJ2"][barco]["movimiento"] = 1

            elif (nuevoJuego["BarcosJ2"][barco]["orientacion"]==derecha):     # Se valida la orientacion del barco para moverlo
                if (listaPosicionesBarcos.count((x+1,y))==0 and listaPosicionesBarcos.count((x+2,y))==0 and x+2 <= limitesTablero[0]-1): # Se valida si puede avanzar 2 casillas
                    matrizJ2[y][x].configure(image= vacio)
                    matrizJ2[y][x+2].configure(image= destructorHaciaDerecha)
                    nuevoJuego["BarcosJ2"][barco]["x1"]= nuevoJuego["BarcosJ2"][barco]["x1"]+2
                    nuevoJuego["BarcosJ2"][barco]["movimiento"] = 1
                elif (nuevoJuego["BarcosJ2"][barco]["x1"]==limitesTablero[0]-1):# Se valida si el barco esta en un borde
                    nuevoJuego["BarcosJ2"][barco]["orientacion"]= izquierda
                    matrizJ2[y][x].configure(image= destructorHaciaIzquierda)
                elif(listaPosicionesBarcos.count((x+1,y))>=1):  # Se valida si la posicion donde avanzará el barco está disponible
                    if (nuevoJuego["BarcosJ2"][barco]["movimiento"]==0):
                        nuevoJuego["BarcosJ2"][barco]["orientacion"]= izquierda
                        matrizJ2[y][x].configure(image= destructorHaciaIzquierda)
                        nuevoJuego["BarcosJ2"][barco]["movimiento"] = 1
                    else:
                        nuevoJuego["BarcosJ2"][barco]["movimiento"] = 0
                else:
                    matrizJ2[y][x].configure(image= vacio)
                    matrizJ2[y][x+1].configure(image= destructorHaciaDerecha)
                    nuevoJuego["BarcosJ2"][barco]["x1"]= nuevoJuego["BarcosJ2"][barco]["x1"]+1
                    nuevoJuego["BarcosJ2"][barco]["movimiento"] = 1

def movimientoCruceros():
    """Función encargada de validar y realizar los movimientos sobre los cruceros
    """
    global nuevoJuego
    global matrizJ1
    global matrizJ2
    for barco in nuevoJuego["BarcosJ1"].keys():       # Se ejecuta la funcion movimientoCruceros para los barcos del jugador 1
        if (barco in ["Crucero1J1", "Crucero2J1", "Crucero3J1", "Crucero4J1"]):
            x1 = nuevoJuego["BarcosJ1"][barco]["x1"]
            y1 = nuevoJuego["BarcosJ1"][barco]["y1"]
            x2 = nuevoJuego["BarcosJ1"][barco]["x2"]
            y2 = nuevoJuego["BarcosJ1"][barco]["y2"]
            listaPosicionesBarcos = listaPosicionesActualesBarcos(nuevoJuego["BarcosJ1"])
            if (nuevoJuego["BarcosJ1"][barco]["vida"]==0):        # Se valida si el barco aun sigue a flote o ya fue hundido
                matrizJ1[y1][x1].configure(image = vacio)
                matrizJ1[y2][x2].configure(image = vacio)
                pass

            elif (nuevoJuego["BarcosJ1"][barco]["disparos"]!=0):      # Se valida si el barco ya recibio un disparo
                    pass

            elif (nuevoJuego["BarcosJ1"][barco]["orientacion"]==arriba):      # Se valida la orientacion del barco para moverlo
                if (nuevoJuego["BarcosJ1"][barco]["y1"]==0):                  # Se valida si el barco esta en un borde
                    nuevoJuego["BarcosJ1"][barco]["orientacion"] = abajo
                    matrizJ1[y1][x1].configure(image= cruceroHaciaAbajo2)
                    matrizJ1[y2][x2].configure(image= cruceroHaciaAbajo1)
                    nuevoJuego["BarcosJ1"][barco]["y1"] = nuevoJuego["BarcosJ1"][barco]["y1"]+1
                    nuevoJuego["BarcosJ1"][barco]["y2"] = nuevoJuego["BarcosJ1"][barco]["y2"]-1
                elif (listaPosicionesBarcos.count((x1,y1-1))>=1):   # Se valida si la posicion donde avanzará el barco está disponible
                    if (nuevoJuego["BarcosJ1"][barco]["movimiento"]==0):
                        nuevoJuego["BarcosJ1"][barco]["orientacion"]= abajo
                        matrizJ1[y1][x1].configure(image= cruceroHaciaAbajo2)
                        matrizJ1[y2][x2].configure(image= cruceroHaciaAbajo1)
                        nuevoJuego["BarcosJ1"][barco]["y1"] = nuevoJuego["BarcosJ1"][barco]["y1"]+1
                        nuevoJuego["BarcosJ1"][barco]["y2"] = nuevoJuego["BarcosJ1"][barco]["y2"]-1
                        nuevoJuego["BarcosJ1"][barco]["movimiento"] = 1
                    else:
                        nuevoJuego["BarcosJ1"][barco]["movimiento"] = 0
                else:
                    matrizJ1[y2][x2].configure(image= vacio)
                    matrizJ1[y1-1][x1].configure(image= cruceroHaciaArriba1)
                    matrizJ1[y2-1][x2].configure(image= cruceroHaciaArriba2)
                    nuevoJuego["BarcosJ1"][barco]["y1"]= nuevoJuego["BarcosJ1"][barco]["y1"]-1
                    nuevoJuego["BarcosJ1"][barco]["y2"]= nuevoJuego["BarcosJ1"][barco]["y2"]-1
                    nuevoJuego["BarcosJ1"][barco]["movimiento"] = 1

            elif (nuevoJuego["BarcosJ1"][barco]["orientacion"]==abajo):       # Se valida la orientacion del barco para moverlo
                if (nuevoJuego["BarcosJ1"][barco]["y1"]==limitesTablero[1]-1):# Se valida si el barco esta en un borde
                    nuevoJuego["BarcosJ1"][barco]["orientacion"] = arriba
                    nuevoJuego["BarcosJ1"][barco]["y1"] = nuevoJuego["BarcosJ1"][barco]["y1"]-1
                    nuevoJuego["BarcosJ1"][barco]["y2"] = nuevoJuego["BarcosJ1"][barco]["y2"]+1
                    matrizJ1[y1][x1].configure(image= cruceroHaciaArriba2)
                    matrizJ1[y2][x2].configure(image= cruceroHaciaArriba1)
                elif (listaPosicionesBarcos.count((x1,y1+1))>=1):   # Se valida si la posicion donde avanzará el barco está disponible
                    if (nuevoJuego["BarcosJ1"][barco]["movimiento"]==0):
                        nuevoJuego["BarcosJ1"][barco]["orientacion"]= arriba
                        matrizJ1[y1][x1].configure(image= cruceroHaciaArriba2)
                        matrizJ1[y2][x2].configure(image= cruceroHaciaArriba1)
                        nuevoJuego["BarcosJ1"][barco]["y1"] = nuevoJuego["BarcosJ1"][barco]["y1"]-1
                        nuevoJuego["BarcosJ1"][barco]["y2"] = nuevoJuego["BarcosJ1"][barco]["y2"]+1
                        nuevoJuego["BarcosJ1"][barco]["movimiento"] = 1
                    else:
                        nuevoJuego["BarcosJ1"][barco]["movimiento"] = 0
                else:
                    matrizJ1[y2][x2].configure(image = vacio)
                    matrizJ1[y1+1][x1].configure(image= cruceroHaciaAbajo1)
                    matrizJ1[y2+1][x2].configure(image= cruceroHaciaAbajo2)
                    nuevoJuego["BarcosJ1"][barco]["y1"]= nuevoJuego["BarcosJ1"][barco]["y1"]+1
                    nuevoJuego["BarcosJ1"][barco]["y2"]= nuevoJuego["BarcosJ1"][barco]["y2"]+1
                    nuevoJuego["BarcosJ1"][barco]["movimiento"] = 1
                
            elif (nuevoJuego["BarcosJ1"][barco]["orientacion"]==izquierda):       # Se valida la orientacion del barco para moverlo
                if (nuevoJuego["BarcosJ1"][barco]["x1"]==0):                      # Se valida si el barco esta en un borde
                    nuevoJuego["BarcosJ1"][barco]["orientacion"] = derecha
                    nuevoJuego["BarcosJ1"][barco]["x1"] = nuevoJuego["BarcosJ1"][barco]["x1"]+1
                    nuevoJuego["BarcosJ1"][barco]["x2"] = nuevoJuego["BarcosJ1"][barco]["x2"]-1
                    matrizJ1[y1][x1].configure(image= cruceroHaciaDerecha2)
                    matrizJ1[y2][x2].configure(image= cruceroHaciaDerecha1)
                elif (listaPosicionesBarcos.count((x1-1,y1))>=1):   # Se valida si la posicion donde avanzará el barco está disponible
                    if (nuevoJuego["BarcosJ1"][barco]["movimiento"]==0):
                        nuevoJuego["BarcosJ1"][barco]["orientacion"] = derecha
                        nuevoJuego["BarcosJ1"][barco]["x1"] = nuevoJuego["BarcosJ1"][barco]["x1"]+1
                        nuevoJuego["BarcosJ1"][barco]["x2"] = nuevoJuego["BarcosJ1"][barco]["x2"]-1
                        matrizJ1[y1][x1].configure(image= cruceroHaciaDerecha2)
                        matrizJ1[y2][x2].configure(image= cruceroHaciaDerecha1)
                        nuevoJuego["BarcosJ1"][barco]["movimiento"] = 1
                    else:
                        nuevoJuego["BarcosJ1"][barco]["movimiento"] = 0
                else:
                    matrizJ1[y2][x2].configure(image = vacio)
                    matrizJ1[y1][x1-1].configure(image= cruceroHaciaIzquierda1)
                    matrizJ1[y2][x2-1].configure(image= cruceroHaciaIzquierda2)
                    nuevoJuego["BarcosJ1"][barco]["x1"]= nuevoJuego["BarcosJ1"][barco]["x1"]-1
                    nuevoJuego["BarcosJ1"][barco]["x2"]= nuevoJuego["BarcosJ1"][barco]["x2"]-1
                    nuevoJuego["BarcosJ1"][barco]["movimiento"] = 1

            elif (nuevoJuego["BarcosJ1"][barco]["orientacion"]==derecha):     # Se valida la orientacion del barco para moverlo
                if (nuevoJuego["BarcosJ1"][barco]["x1"]==limitesTablero[0]-1):# Se valida si el barco esta en un borde
                    nuevoJuego["BarcosJ1"][barco]["orientacion"] = izquierda
                    nuevoJuego["BarcosJ1"][barco]["x1"] = nuevoJuego["BarcosJ1"][barco]["x1"]-1
                    nuevoJuego["BarcosJ1"][barco]["x2"] = nuevoJuego["BarcosJ1"][barco]["x2"]+1
                    matrizJ1[y1][x1].configure(image= cruceroHaciaIzquierda2)
                    matrizJ1[y2][x2].configure(image= cruceroHaciaIzquierda1)
                elif (listaPosicionesBarcos.count((x1+1,y1))>=1):   # Se valida si la posicion donde avanzará el barco está disponible
                    if (nuevoJuego["BarcosJ1"][barco]["movimiento"]==0):
                        nuevoJuego["BarcosJ1"][barco]["orientacion"] = izquierda
                        nuevoJuego["BarcosJ1"][barco]["x1"] = nuevoJuego["BarcosJ1"][barco]["x1"]-1
                        nuevoJuego["BarcosJ1"][barco]["x2"] = nuevoJuego["BarcosJ1"][barco]["x2"]+1
                        matrizJ1[y1][x1].configure(image= cruceroHaciaIzquierda2)
                        matrizJ1[y2][x2].configure(image= cruceroHaciaIzquierda1)
                        nuevoJuego["BarcosJ1"][barco]["movimiento"] = 1
                    else:
                        nuevoJuego["BarcosJ1"][barco]["movimiento"] = 0
                else:
                    matrizJ1[y2][x2].configure(image = vacio)
                    matrizJ1[y1][x1+1].configure(image= cruceroHaciaDerecha1)
                    matrizJ1[y2][x2+1].configure(image= cruceroHaciaDerecha2)
                    nuevoJuego["BarcosJ1"][barco]["x1"]= nuevoJuego["BarcosJ1"][barco]["x1"]+1
                    nuevoJuego["BarcosJ1"][barco]["x2"]= nuevoJuego["BarcosJ1"][barco]["x2"]+1
                    nuevoJuego["BarcosJ1"][barco]["movimiento"] = 1

    for barco in nuevoJuego["BarcosJ2"].keys():       # Se ejecuta la funcion movimientoCruceros para los barcos del jugador 2
        if (barco in ["Crucero1J2", "Crucero2J2", "Crucero3J2", "Crucero4J2"]):
            x1 = nuevoJuego["BarcosJ2"][barco]["x1"]
            y1 = nuevoJuego["BarcosJ2"][barco]["y1"]
            x2 = nuevoJuego["BarcosJ2"][barco]["x2"]
            y2 = nuevoJuego["BarcosJ2"][barco]["y2"]
            listaPosicionesBarcos = listaPosicionesActualesBarcos(nuevoJuego["BarcosJ2"])
            if (nuevoJuego["BarcosJ2"][barco]["vida"]==0):        # Se valida si el barco aun sigue a flote o ya fue hundido
                matrizJ2[y1][x1].configure(image = vacio)
                matrizJ2[y2][x2].configure(image = vacio)
                pass

            elif (nuevoJuego["BarcosJ2"][barco]["disparos"]!=0):      # Se valida si el barco ya recibio un disparo
                    pass

            elif (nuevoJuego["BarcosJ2"][barco]["orientacion"]==arriba):      # Se valida la orientacion del barco para moverlo
                if (nuevoJuego["BarcosJ2"][barco]["y1"]==0):                  # Se valida si el barco esta en un borde
                    nuevoJuego["BarcosJ2"][barco]["orientacion"] = abajo
                    matrizJ2[y1][x1].configure(image= cruceroHaciaAbajo2)
                    matrizJ2[y2][x2].configure(image= cruceroHaciaAbajo1)
                    nuevoJuego["BarcosJ2"][barco]["y1"] = nuevoJuego["BarcosJ2"][barco]["y1"]+1
                    nuevoJuego["BarcosJ2"][barco]["y2"] = nuevoJuego["BarcosJ2"][barco]["y2"]-1
                elif (listaPosicionesBarcos.count((x1,y1-1))>=1):   # Se valida si la posicion donde avanzará el barco está disponible
                    if (nuevoJuego["BarcosJ2"][barco]["movimiento"]==0):
                        nuevoJuego["BarcosJ2"][barco]["orientacion"]= abajo
                        matrizJ2[y1][x1].configure(image= cruceroHaciaAbajo2)
                        matrizJ2[y2][x2].configure(image= cruceroHaciaAbajo1)
                        nuevoJuego["BarcosJ2"][barco]["y1"] = nuevoJuego["BarcosJ2"][barco]["y1"]+1
                        nuevoJuego["BarcosJ2"][barco]["y2"] = nuevoJuego["BarcosJ2"][barco]["y2"]-1
                        nuevoJuego["BarcosJ2"][barco]["movimiento"] = 1
                    else:
                        nuevoJuego["BarcosJ2"][barco]["movimiento"] = 0
                else:
                    matrizJ2[y2][x2].configure(image= vacio)
                    matrizJ2[y1-1][x1].configure(image= cruceroHaciaArriba1)
                    matrizJ2[y2-1][x2].configure(image= cruceroHaciaArriba2)
                    nuevoJuego["BarcosJ2"][barco]["y1"]= nuevoJuego["BarcosJ2"][barco]["y1"]-1
                    nuevoJuego["BarcosJ2"][barco]["y2"]= nuevoJuego["BarcosJ2"][barco]["y2"]-1
                    nuevoJuego["BarcosJ2"][barco]["movimiento"] = 1

            elif (nuevoJuego["BarcosJ2"][barco]["orientacion"]==abajo):       # Se valida la orientacion del barco para moverlo
                if (nuevoJuego["BarcosJ2"][barco]["y1"]==limitesTablero[1]-1):# Se valida si el barco esta en un borde
                    nuevoJuego["BarcosJ2"][barco]["orientacion"] = arriba
                    nuevoJuego["BarcosJ2"][barco]["y1"] = nuevoJuego["BarcosJ2"][barco]["y1"]-1
                    nuevoJuego["BarcosJ2"][barco]["y2"] = nuevoJuego["BarcosJ2"][barco]["y2"]+1
                    matrizJ2[y1][x1].configure(image= cruceroHaciaArriba2)
                    matrizJ2[y2][x2].configure(image= cruceroHaciaArriba1)
                elif (listaPosicionesBarcos.count((x1,y1+1))>=1):   # Se valida si la posicion donde avanzará el barco está disponible
                    if (nuevoJuego["BarcosJ2"][barco]["movimiento"]==0):
                        nuevoJuego["BarcosJ2"][barco]["orientacion"]= arriba
                        matrizJ2[y1][x1].configure(image= cruceroHaciaArriba2)
                        matrizJ2[y2][x2].configure(image= cruceroHaciaArriba1)
                        nuevoJuego["BarcosJ2"][barco]["y1"] = nuevoJuego["BarcosJ2"][barco]["y1"]-1
                        nuevoJuego["BarcosJ2"][barco]["y2"] = nuevoJuego["BarcosJ2"][barco]["y2"]+1
                        nuevoJuego["BarcosJ2"][barco]["movimiento"] = 1
                    else:
                        nuevoJuego["BarcosJ2"][barco]["movimiento"] = 0
                else:
                    matrizJ2[y2][x2].configure(image = vacio)
                    matrizJ2[y1+1][x1].configure(image= cruceroHaciaAbajo1)
                    matrizJ2[y2+1][x2].configure(image= cruceroHaciaAbajo2)
                    nuevoJuego["BarcosJ2"][barco]["y1"]= nuevoJuego["BarcosJ2"][barco]["y1"]+1
                    nuevoJuego["BarcosJ2"][barco]["y2"]= nuevoJuego["BarcosJ2"][barco]["y2"]+1
                    nuevoJuego["BarcosJ2"][barco]["movimiento"] = 1
                
            elif (nuevoJuego["BarcosJ2"][barco]["orientacion"]==izquierda):       # Se valida la orientacion del barco para moverlo
                if (nuevoJuego["BarcosJ2"][barco]["x1"]==0):                      # Se valida si el barco esta en un borde
                    nuevoJuego["BarcosJ2"][barco]["orientacion"] = derecha
                    nuevoJuego["BarcosJ2"][barco]["x1"] = nuevoJuego["BarcosJ2"][barco]["x1"]+1
                    nuevoJuego["BarcosJ2"][barco]["x2"] = nuevoJuego["BarcosJ2"][barco]["x2"]-1
                    matrizJ2[y1][x1].configure(image= cruceroHaciaDerecha2)
                    matrizJ2[y2][x2].configure(image= cruceroHaciaDerecha1)
                elif (listaPosicionesBarcos.count((x1-1,y1))>=1):   # Se valida si la posicion donde avanzará el barco está disponible
                    if (nuevoJuego["BarcosJ2"][barco]["movimiento"]==0):
                        nuevoJuego["BarcosJ2"][barco]["orientacion"] = derecha
                        nuevoJuego["BarcosJ2"][barco]["x1"] = nuevoJuego["BarcosJ2"][barco]["x1"]+1
                        nuevoJuego["BarcosJ2"][barco]["x2"] = nuevoJuego["BarcosJ2"][barco]["x2"]-1
                        matrizJ2[y1][x1].configure(image= cruceroHaciaDerecha2)
                        matrizJ2[y2][x2].configure(image= cruceroHaciaDerecha1)
                        nuevoJuego["BarcosJ2"][barco]["movimiento"] = 1
                    else:
                        nuevoJuego["BarcosJ2"][barco]["movimiento"] = 0
                else:
                    matrizJ2[y2][x2].configure(image = vacio)
                    matrizJ2[y1][x1-1].configure(image= cruceroHaciaIzquierda1)
                    matrizJ2[y2][x2-1].configure(image= cruceroHaciaIzquierda2)
                    nuevoJuego["BarcosJ2"][barco]["x1"]= nuevoJuego["BarcosJ2"][barco]["x1"]-1
                    nuevoJuego["BarcosJ2"][barco]["x2"]= nuevoJuego["BarcosJ2"][barco]["x2"]-1
                    nuevoJuego["BarcosJ2"][barco]["movimiento"] = 1

            elif (nuevoJuego["BarcosJ2"][barco]["orientacion"]==derecha):     # Se valida la orientacion del barco para moverlo
                if (nuevoJuego["BarcosJ2"][barco]["x1"]==limitesTablero[0]-1):# Se valida si el barco esta en un borde
                    nuevoJuego["BarcosJ2"][barco]["orientacion"] = izquierda
                    nuevoJuego["BarcosJ2"][barco]["x1"] = nuevoJuego["BarcosJ2"][barco]["x1"]-1
                    nuevoJuego["BarcosJ2"][barco]["x2"] = nuevoJuego["BarcosJ2"][barco]["x2"]+1
                    matrizJ2[y1][x1].configure(image= cruceroHaciaIzquierda2)
                    matrizJ2[y2][x2].configure(image= cruceroHaciaIzquierda1)
                elif (listaPosicionesBarcos.count((x1+1,y1))>=1):   # Se valida si la posicion donde avanzará el barco está disponible
                    if (nuevoJuego["BarcosJ2"][barco]["movimiento"]==0):
                        nuevoJuego["BarcosJ2"][barco]["orientacion"] = izquierda
                        nuevoJuego["BarcosJ2"][barco]["x1"] = nuevoJuego["BarcosJ2"][barco]["x1"]-1
                        nuevoJuego["BarcosJ2"][barco]["x2"] = nuevoJuego["BarcosJ2"][barco]["x2"]+1
                        matrizJ2[y1][x1].configure(image= cruceroHaciaIzquierda2)
                        matrizJ2[y2][x2].configure(image= cruceroHaciaIzquierda1)
                        nuevoJuego["BarcosJ2"][barco]["movimiento"] = 1
                    else:
                        nuevoJuego["BarcosJ2"][barco]["movimiento"] = 0
                else:
                    matrizJ2[y2][x2].configure(image = vacio)
                    matrizJ2[y1][x1+1].configure(image= cruceroHaciaDerecha1)
                    matrizJ2[y2][x2+1].configure(image= cruceroHaciaDerecha2)
                    nuevoJuego["BarcosJ2"][barco]["x1"]= nuevoJuego["BarcosJ2"][barco]["x1"]+1
                    nuevoJuego["BarcosJ2"][barco]["x2"]= nuevoJuego["BarcosJ2"][barco]["x2"]+1
                    nuevoJuego["BarcosJ2"][barco]["movimiento"] = 1

def movimientoAcorazados():
    """Función encargada de validar y realizar los movimientos sobre los Acorazados
    """
    global nuevoJuego
    global matrizJ1
    global matrizJ2
    for barco in nuevoJuego["BarcosJ1"].keys():       # Se ejecuta la funcion movimientoAcorazados para los barcos del jugador 1
        if (barco in ["Acorazado1J1", "Acorazado2J1"]):
            x1 = nuevoJuego["BarcosJ1"][barco]["x1"]
            y1 = nuevoJuego["BarcosJ1"][barco]["y1"]
            x2 = nuevoJuego["BarcosJ1"][barco]["x2"]
            y2 = nuevoJuego["BarcosJ1"][barco]["y2"]
            x3 = nuevoJuego["BarcosJ1"][barco]["x3"]
            y3 = nuevoJuego["BarcosJ1"][barco]["y3"]
            listaPosicionesBarcos = listaPosicionesActualesBarcos(nuevoJuego["BarcosJ1"])
            if (nuevoJuego["BarcosJ1"][barco]["vida"]==0):        # Se valida si el barco aun sigue a flote o ya fue hundido
                matrizJ1[y1][x1].configure(image = vacio)
                matrizJ1[y2][x2].configure(image = vacio)
                matrizJ1[y3][x3].configure(image = vacio)
                pass 

            elif (nuevoJuego["BarcosJ1"][barco]["disparos"]!=0):  # Se valida si el barco ya recibio un disparo
                    pass

            elif (nuevoJuego["BarcosJ1"][barco]["orientacion"]==arriba):    # Se valida la orientacion del barco para moverlo
                if (nuevoJuego["BarcosJ1"][barco]["y1"]==0):                # Se valida si el barco esta en un borde
                    nuevoJuego["BarcosJ1"][barco]["orientacion"] = abajo
                    matrizJ1[y1][x1].configure(image= acorazadoHaciaAbajo3)
                    matrizJ1[y2][x2].configure(image= acorazadoHaciaAbajo2)
                    matrizJ1[y3][x3].configure(image= acorazadoHaciaAbajo1)
                    nuevoJuego["BarcosJ1"][barco]["y1"] = nuevoJuego["BarcosJ1"][barco]["y1"]+2
                    nuevoJuego["BarcosJ1"][barco]["y2"] = nuevoJuego["BarcosJ1"][barco]["y2"]
                    nuevoJuego["BarcosJ1"][barco]["y3"] = nuevoJuego["BarcosJ1"][barco]["y3"]-2
                elif (listaPosicionesBarcos.count((x1,y1-1))>=1):   # Se valida si la posicion donde avanzará el barco está disponible
                    if (nuevoJuego["BarcosJ1"][barco]["movimiento"]==0):
                        nuevoJuego["BarcosJ1"][barco]["orientacion"]= abajo
                        matrizJ1[y1][x1].configure(image= acorazadoHaciaAbajo3)
                        matrizJ1[y2][x2].configure(image= acorazadoHaciaAbajo2)
                        matrizJ1[y3][x3].configure(image= acorazadoHaciaAbajo1)
                        nuevoJuego["BarcosJ1"][barco]["y1"] = nuevoJuego["BarcosJ1"][barco]["y1"]+2
                        nuevoJuego["BarcosJ1"][barco]["y2"] = nuevoJuego["BarcosJ1"][barco]["y2"]
                        nuevoJuego["BarcosJ1"][barco]["y3"] = nuevoJuego["BarcosJ1"][barco]["y3"]-2
                        nuevoJuego["BarcosJ1"][barco]["movimiento"] = 1
                    else:
                        nuevoJuego["BarcosJ1"][barco]["movimiento"] = 0
                else:
                    matrizJ1[y3][x3].configure(image= vacio)
                    matrizJ1[y1-1][x1].configure(image= acorazadoHaciaArriba1)
                    matrizJ1[y2-1][x2].configure(image= acorazadoHaciaArriba2)
                    matrizJ1[y3-1][x3].configure(image= acorazadoHaciaArriba3)
                    nuevoJuego["BarcosJ1"][barco]["y1"] = nuevoJuego["BarcosJ1"][barco]["y1"]-1
                    nuevoJuego["BarcosJ1"][barco]["y2"] = nuevoJuego["BarcosJ1"][barco]["y2"]-1
                    nuevoJuego["BarcosJ1"][barco]["y3"] = nuevoJuego["BarcosJ1"][barco]["y3"]-1
                    nuevoJuego["BarcosJ1"][barco]["movimiento"] = 1
            
            elif (nuevoJuego["BarcosJ1"][barco]["orientacion"]==abajo):       # Se valida la orientacion del barco para moverlo
                if (nuevoJuego["BarcosJ1"][barco]["y1"]==limitesTablero[1]-1):# Se valida si el barco esta en un borde
                    nuevoJuego["BarcosJ1"][barco]["orientacion"] = arriba
                    matrizJ1[y1][x1].configure(image= acorazadoHaciaArriba3)
                    matrizJ1[y2][x2].configure(image= acorazadoHaciaArriba2)
                    matrizJ1[y3][x3].configure(image= acorazadoHaciaArriba1)
                    nuevoJuego["BarcosJ1"][barco]["y1"] = nuevoJuego["BarcosJ1"][barco]["y1"]-2
                    nuevoJuego["BarcosJ1"][barco]["y2"] = nuevoJuego["BarcosJ1"][barco]["y2"]
                    nuevoJuego["BarcosJ1"][barco]["y3"] = nuevoJuego["BarcosJ1"][barco]["y3"]+2
                elif (listaPosicionesBarcos.count((x1,y1+1))>=1):   # Se valida si la posicion donde avanzará el barco está disponible
                    if (nuevoJuego["BarcosJ1"][barco]["movimiento"]==0):
                        nuevoJuego["BarcosJ1"][barco]["orientacion"]= arriba
                        matrizJ1[y1][x1].configure(image= acorazadoHaciaArriba3)
                        matrizJ1[y2][x2].configure(image= acorazadoHaciaArriba2)
                        matrizJ1[y3][x3].configure(image= acorazadoHaciaArriba1)
                        nuevoJuego["BarcosJ1"][barco]["y1"] = nuevoJuego["BarcosJ1"][barco]["y1"]-2
                        nuevoJuego["BarcosJ1"][barco]["y2"] = nuevoJuego["BarcosJ1"][barco]["y2"]
                        nuevoJuego["BarcosJ1"][barco]["y3"] = nuevoJuego["BarcosJ1"][barco]["y3"]+2
                        nuevoJuego["BarcosJ1"][barco]["movimiento"] = 1
                    else:
                        nuevoJuego["BarcosJ1"][barco]["movimiento"] = 0
                else:
                    matrizJ1[y3][x3].configure(image= vacio)
                    matrizJ1[y1+1][x1].configure(image= acorazadoHaciaAbajo1)
                    matrizJ1[y2+1][x2].configure(image= acorazadoHaciaAbajo2)
                    matrizJ1[y3+1][x3].configure(image= acorazadoHaciaAbajo3)
                    nuevoJuego["BarcosJ1"][barco]["y1"] = nuevoJuego["BarcosJ1"][barco]["y1"]+1
                    nuevoJuego["BarcosJ1"][barco]["y2"] = nuevoJuego["BarcosJ1"][barco]["y2"]+1
                    nuevoJuego["BarcosJ1"][barco]["y3"] = nuevoJuego["BarcosJ1"][barco]["y3"]+1
                    nuevoJuego["BarcosJ1"][barco]["movimiento"] = 1

            elif (nuevoJuego["BarcosJ1"][barco]["orientacion"]==izquierda):       # Se valida la orientacion del barco para moverlo
                if (nuevoJuego["BarcosJ1"][barco]["x1"]==0):                      # Se valida si el barco esta en un borde
                    nuevoJuego["BarcosJ1"][barco]["orientacion"] = derecha
                    matrizJ1[y1][x1].configure(image= acorazadoHaciaDerecha3)
                    matrizJ1[y2][x2].configure(image= acorazadoHaciaDerecha2)
                    matrizJ1[y3][x3].configure(image= acorazadoHaciaDerecha1)
                    nuevoJuego["BarcosJ1"][barco]["x1"] = nuevoJuego["BarcosJ1"][barco]["x1"]+2
                    nuevoJuego["BarcosJ1"][barco]["x2"] = nuevoJuego["BarcosJ1"][barco]["x2"]
                    nuevoJuego["BarcosJ1"][barco]["x3"] = nuevoJuego["BarcosJ1"][barco]["x3"]-2
                elif (listaPosicionesBarcos.count((x1-1,y1))>=1):   # Se valida si la posicion donde avanzará el barco está disponible
                    if (nuevoJuego["BarcosJ1"][barco]["movimiento"]==0):
                        nuevoJuego["BarcosJ1"][barco]["orientacion"]= derecha
                        matrizJ1[y1][x1].configure(image= acorazadoHaciaDerecha3)
                        matrizJ1[y2][x2].configure(image= acorazadoHaciaDerecha2)
                        matrizJ1[y3][x3].configure(image= acorazadoHaciaDerecha1)
                        nuevoJuego["BarcosJ1"][barco]["x1"] = nuevoJuego["BarcosJ1"][barco]["x1"]+2
                        nuevoJuego["BarcosJ1"][barco]["x2"] = nuevoJuego["BarcosJ1"][barco]["x2"]
                        nuevoJuego["BarcosJ1"][barco]["x3"] = nuevoJuego["BarcosJ1"][barco]["x3"]-2
                        nuevoJuego["BarcosJ1"][barco]["movimiento"] = 1
                    else:
                        nuevoJuego["BarcosJ1"][barco]["movimiento"] = 0
                else:
                    matrizJ1[y3][x3].configure(image= vacio)
                    matrizJ1[y1][x1-1].configure(image= acorazadoHaciaIzquierda1)
                    matrizJ1[y2][x2-1].configure(image= acorazadoHaciaIzquierda2)
                    matrizJ1[y3][x3-1].configure(image= acorazadoHaciaIzquierda3)
                    nuevoJuego["BarcosJ1"][barco]["x1"] = nuevoJuego["BarcosJ1"][barco]["x1"]-1
                    nuevoJuego["BarcosJ1"][barco]["x2"] = nuevoJuego["BarcosJ1"][barco]["x2"]-1
                    nuevoJuego["BarcosJ1"][barco]["x3"] = nuevoJuego["BarcosJ1"][barco]["x3"]-1
                    nuevoJuego["BarcosJ1"][barco]["movimiento"] = 1
            
            elif (nuevoJuego["BarcosJ1"][barco]["orientacion"]==derecha):     # Se valida la orientacion del barco para moverlo
                if (nuevoJuego["BarcosJ1"][barco]["x1"]==limitesTablero[0]-1):# Se valida si el barco esta en un borde
                    nuevoJuego["BarcosJ1"][barco]["orientacion"] = izquierda
                    matrizJ1[y1][x1].configure(image= acorazadoHaciaIzquierda3)
                    matrizJ1[y2][x2].configure(image= acorazadoHaciaIzquierda2)
                    matrizJ1[y3][x3].configure(image= acorazadoHaciaIzquierda1)
                    nuevoJuego["BarcosJ1"][barco]["x1"] = nuevoJuego["BarcosJ1"][barco]["x1"]-2
                    nuevoJuego["BarcosJ1"][barco]["x2"] = nuevoJuego["BarcosJ1"][barco]["x2"]
                    nuevoJuego["BarcosJ1"][barco]["x3"] = nuevoJuego["BarcosJ1"][barco]["x3"]+2
                elif (listaPosicionesBarcos.count((x1+1,y1))>=1):   # Se valida si la posicion donde avanzará el barco está disponible
                    if (nuevoJuego["BarcosJ1"][barco]["movimiento"]==0):
                        nuevoJuego["BarcosJ1"][barco]["orientacion"]= izquierda
                        matrizJ1[y1][x1].configure(image= acorazadoHaciaIzquierda3)
                        matrizJ1[y2][x2].configure(image= acorazadoHaciaIzquierda2)
                        matrizJ1[y3][x3].configure(image= acorazadoHaciaIzquierda1)
                        nuevoJuego["BarcosJ1"][barco]["x1"] = nuevoJuego["BarcosJ1"][barco]["x1"]-2
                        nuevoJuego["BarcosJ1"][barco]["x2"] = nuevoJuego["BarcosJ1"][barco]["x2"]
                        nuevoJuego["BarcosJ1"][barco]["x3"] = nuevoJuego["BarcosJ1"][barco]["x3"]+2
                        nuevoJuego["BarcosJ1"][barco]["movimiento"] = 1
                    else:
                        nuevoJuego["BarcosJ1"][barco]["movimiento"] = 0
                else:
                    matrizJ1[y3][x3].configure(image= vacio)
                    matrizJ1[y1][x1+1].configure(image= acorazadoHaciaDerecha1)
                    matrizJ1[y2][x2+1].configure(image= acorazadoHaciaDerecha2)
                    matrizJ1[y3][x3+1].configure(image= acorazadoHaciaDerecha3)
                    nuevoJuego["BarcosJ1"][barco]["x1"] = nuevoJuego["BarcosJ1"][barco]["x1"]+1
                    nuevoJuego["BarcosJ1"][barco]["x2"] = nuevoJuego["BarcosJ1"][barco]["x2"]+1
                    nuevoJuego["BarcosJ1"][barco]["x3"] = nuevoJuego["BarcosJ1"][barco]["x3"]+1
                    nuevoJuego["BarcosJ1"][barco]["movimiento"] = 1
    
    for barco in nuevoJuego["BarcosJ2"].keys():       # Se ejecuta la funcion movimientoAcorazados para los barcos del jugador 2
        if (barco in ["Acorazado1J2", "Acorazado2J2"]):
            x1 = nuevoJuego["BarcosJ2"][barco]["x1"]
            y1 = nuevoJuego["BarcosJ2"][barco]["y1"]
            x2 = nuevoJuego["BarcosJ2"][barco]["x2"]
            y2 = nuevoJuego["BarcosJ2"][barco]["y2"]
            x3 = nuevoJuego["BarcosJ2"][barco]["x3"]
            y3 = nuevoJuego["BarcosJ2"][barco]["y3"]
            listaPosicionesBarcos = listaPosicionesActualesBarcos(nuevoJuego["BarcosJ2"])
            if (nuevoJuego["BarcosJ2"][barco]["vida"]==0):        # Se valida si el barco aun sigue a flote o ya fue hundido
                matrizJ2[y1][x1].configure(image = vacio)
                matrizJ2[y2][x2].configure(image = vacio)
                matrizJ2[y3][x3].configure(image = vacio)
                pass 

            elif (nuevoJuego["BarcosJ2"][barco]["disparos"]!=0):  # Se valida si el barco ya recibio un disparo
                    pass

            elif (nuevoJuego["BarcosJ2"][barco]["orientacion"]==arriba):    # Se valida la orientacion del barco para moverlo
                if (nuevoJuego["BarcosJ2"][barco]["y1"]==0):                # Se valida si el barco esta en un borde
                    nuevoJuego["BarcosJ2"][barco]["orientacion"] = abajo
                    matrizJ2[y1][x1].configure(image= acorazadoHaciaAbajo3)
                    matrizJ2[y2][x2].configure(image= acorazadoHaciaAbajo2)
                    matrizJ2[y3][x3].configure(image= acorazadoHaciaAbajo1)
                    nuevoJuego["BarcosJ2"][barco]["y1"] = nuevoJuego["BarcosJ2"][barco]["y1"]+2
                    nuevoJuego["BarcosJ2"][barco]["y2"] = nuevoJuego["BarcosJ2"][barco]["y2"]
                    nuevoJuego["BarcosJ2"][barco]["y3"] = nuevoJuego["BarcosJ2"][barco]["y3"]-2
                elif (listaPosicionesBarcos.count((x1,y1-1))>=1):   # Se valida si la posicion donde avanzará el barco está disponible
                    if (nuevoJuego["BarcosJ2"][barco]["movimiento"]==0):
                        nuevoJuego["BarcosJ2"][barco]["orientacion"]= abajo
                        matrizJ2[y1][x1].configure(image= acorazadoHaciaAbajo3)
                        matrizJ2[y2][x2].configure(image= acorazadoHaciaAbajo2)
                        matrizJ2[y3][x3].configure(image= acorazadoHaciaAbajo1)
                        nuevoJuego["BarcosJ2"][barco]["y1"] = nuevoJuego["BarcosJ2"][barco]["y1"]+2
                        nuevoJuego["BarcosJ2"][barco]["y2"] = nuevoJuego["BarcosJ2"][barco]["y2"]
                        nuevoJuego["BarcosJ2"][barco]["y3"] = nuevoJuego["BarcosJ2"][barco]["y3"]-2
                        nuevoJuego["BarcosJ2"][barco]["movimiento"] = 1
                    else:
                        nuevoJuego["BarcosJ2"][barco]["movimiento"] = 0
                else:
                    matrizJ2[y3][x3].configure(image= vacio)
                    matrizJ2[y1-1][x1].configure(image= acorazadoHaciaArriba1)
                    matrizJ2[y2-1][x2].configure(image= acorazadoHaciaArriba2)
                    matrizJ2[y3-1][x3].configure(image= acorazadoHaciaArriba3)
                    nuevoJuego["BarcosJ2"][barco]["y1"] = nuevoJuego["BarcosJ2"][barco]["y1"]-1
                    nuevoJuego["BarcosJ2"][barco]["y2"] = nuevoJuego["BarcosJ2"][barco]["y2"]-1
                    nuevoJuego["BarcosJ2"][barco]["y3"] = nuevoJuego["BarcosJ2"][barco]["y3"]-1
                    nuevoJuego["BarcosJ2"][barco]["movimiento"] = 1
            
            elif (nuevoJuego["BarcosJ2"][barco]["orientacion"]==abajo):       # Se valida la orientacion del barco para moverlo
                if (nuevoJuego["BarcosJ2"][barco]["y1"]==limitesTablero[1]-1):# Se valida si el barco esta en un borde
                    nuevoJuego["BarcosJ2"][barco]["orientacion"] = arriba
                    matrizJ2[y1][x1].configure(image= acorazadoHaciaArriba3)
                    matrizJ2[y2][x2].configure(image= acorazadoHaciaArriba2)
                    matrizJ2[y3][x3].configure(image= acorazadoHaciaArriba1)
                    nuevoJuego["BarcosJ2"][barco]["y1"] = nuevoJuego["BarcosJ2"][barco]["y1"]-2
                    nuevoJuego["BarcosJ2"][barco]["y2"] = nuevoJuego["BarcosJ2"][barco]["y2"]
                    nuevoJuego["BarcosJ2"][barco]["y3"] = nuevoJuego["BarcosJ2"][barco]["y3"]+2
                elif (listaPosicionesBarcos.count((x1,y1+1))>=1):   # Se valida si la posicion donde avanzará el barco está disponible
                    if (nuevoJuego["BarcosJ2"][barco]["movimiento"]==0):
                        nuevoJuego["BarcosJ2"][barco]["orientacion"]= arriba
                        matrizJ2[y1][x1].configure(image= acorazadoHaciaArriba3)
                        matrizJ2[y2][x2].configure(image= acorazadoHaciaArriba2)
                        matrizJ2[y3][x3].configure(image= acorazadoHaciaArriba1)
                        nuevoJuego["BarcosJ2"][barco]["y1"] = nuevoJuego["BarcosJ2"][barco]["y1"]-2
                        nuevoJuego["BarcosJ2"][barco]["y2"] = nuevoJuego["BarcosJ2"][barco]["y2"]
                        nuevoJuego["BarcosJ2"][barco]["y3"] = nuevoJuego["BarcosJ2"][barco]["y3"]+2
                        nuevoJuego["BarcosJ2"][barco]["movimiento"] = 1
                    else:
                        nuevoJuego["BarcosJ2"][barco]["movimiento"] = 0
                        #nuevoJuego["BarcosJ2"]                
                else:
                    matrizJ2[y3][x3].configure(image= vacio)
                    matrizJ2[y1+1][x1].configure(image= acorazadoHaciaAbajo1)
                    matrizJ2[y2+1][x2].configure(image= acorazadoHaciaAbajo2)
                    matrizJ2[y3+1][x3].configure(image= acorazadoHaciaAbajo3)
                    nuevoJuego["BarcosJ2"][barco]["y1"] = nuevoJuego["BarcosJ2"][barco]["y1"]+1
                    nuevoJuego["BarcosJ2"][barco]["y2"] = nuevoJuego["BarcosJ2"][barco]["y2"]+1
                    nuevoJuego["BarcosJ2"][barco]["y3"] = nuevoJuego["BarcosJ2"][barco]["y3"]+1
                    nuevoJuego["BarcosJ2"][barco]["movimiento"] = 1

            elif (nuevoJuego["BarcosJ2"][barco]["orientacion"]==izquierda):       # Se valida la orientacion del barco para moverlo
                if (nuevoJuego["BarcosJ2"][barco]["x1"]==0):                      # Se valida si el barco esta en un borde
                    nuevoJuego["BarcosJ2"][barco]["orientacion"] = derecha
                    matrizJ2[y1][x1].configure(image= acorazadoHaciaDerecha3)
                    matrizJ2[y2][x2].configure(image= acorazadoHaciaDerecha2)
                    matrizJ2[y3][x3].configure(image= acorazadoHaciaDerecha1)
                    nuevoJuego["BarcosJ2"][barco]["x1"] = nuevoJuego["BarcosJ2"][barco]["x1"]+2
                    nuevoJuego["BarcosJ2"][barco]["x2"] = nuevoJuego["BarcosJ2"][barco]["x2"]
                    nuevoJuego["BarcosJ2"][barco]["x3"] = nuevoJuego["BarcosJ2"][barco]["x3"]-2
                elif (listaPosicionesBarcos.count((x1-1,y1))>=1):   # Se valida si la posicion donde avanzará el barco está disponible
                    if (nuevoJuego["BarcosJ2"][barco]["movimiento"]==0):
                        nuevoJuego["BarcosJ2"][barco]["orientacion"]= derecha
                        matrizJ2[y1][x1].configure(image= acorazadoHaciaDerecha3)
                        matrizJ2[y2][x2].configure(image= acorazadoHaciaDerecha2)
                        matrizJ2[y3][x3].configure(image= acorazadoHaciaDerecha1)
                        nuevoJuego["BarcosJ2"][barco]["x1"] = nuevoJuego["BarcosJ2"][barco]["x1"]+2
                        nuevoJuego["BarcosJ2"][barco]["x2"] = nuevoJuego["BarcosJ2"][barco]["x2"]
                        nuevoJuego["BarcosJ2"][barco]["x3"] = nuevoJuego["BarcosJ2"][barco]["x3"]-2
                        nuevoJuego["BarcosJ2"][barco]["movimiento"] = 1
                    else:
                        nuevoJuego["BarcosJ2"][barco]["movimiento"] = 0
                else:
                    matrizJ2[y3][x3].configure(image= vacio)
                    matrizJ2[y1][x1-1].configure(image= acorazadoHaciaIzquierda1)
                    matrizJ2[y2][x2-1].configure(image= acorazadoHaciaIzquierda2)
                    matrizJ2[y3][x3-1].configure(image= acorazadoHaciaIzquierda3)
                    nuevoJuego["BarcosJ2"][barco]["x1"] = nuevoJuego["BarcosJ2"][barco]["x1"]-1
                    nuevoJuego["BarcosJ2"][barco]["x2"] = nuevoJuego["BarcosJ2"][barco]["x2"]-1
                    nuevoJuego["BarcosJ2"][barco]["x3"] = nuevoJuego["BarcosJ2"][barco]["x3"]-1
                    nuevoJuego["BarcosJ2"][barco]["movimiento"] = 1
            
            elif (nuevoJuego["BarcosJ2"][barco]["orientacion"]==derecha):     # Se valida la orientacion del barco para moverlo
                if (nuevoJuego["BarcosJ2"][barco]["x1"]==limitesTablero[0]-1):# Se valida si el barco esta en un borde
                    nuevoJuego["BarcosJ2"][barco]["orientacion"] = izquierda
                    matrizJ2[y1][x1].configure(image= acorazadoHaciaIzquierda3)
                    matrizJ2[y2][x2].configure(image= acorazadoHaciaIzquierda2)
                    matrizJ2[y3][x3].configure(image= acorazadoHaciaIzquierda1)
                    nuevoJuego["BarcosJ2"][barco]["x1"] = nuevoJuego["BarcosJ2"][barco]["x1"]-2
                    nuevoJuego["BarcosJ2"][barco]["x2"] = nuevoJuego["BarcosJ2"][barco]["x2"]
                    nuevoJuego["BarcosJ2"][barco]["x3"] = nuevoJuego["BarcosJ2"][barco]["x3"]+2
                elif (listaPosicionesBarcos.count((x1+1,y1))>=1):   # Se valida si la posicion donde avanzará el barco está disponible
                    if (nuevoJuego["BarcosJ2"][barco]["movimiento"]==0):
                        nuevoJuego["BarcosJ2"][barco]["orientacion"]= izquierda
                        matrizJ2[y1][x1].configure(image= acorazadoHaciaIzquierda3)
                        matrizJ2[y2][x2].configure(image= acorazadoHaciaIzquierda2)
                        matrizJ2[y3][x3].configure(image= acorazadoHaciaIzquierda1)
                        nuevoJuego["BarcosJ2"][barco]["x1"] = nuevoJuego["BarcosJ2"][barco]["x1"]-2
                        nuevoJuego["BarcosJ2"][barco]["x2"] = nuevoJuego["BarcosJ2"][barco]["x2"]
                        nuevoJuego["BarcosJ2"][barco]["x3"] = nuevoJuego["BarcosJ2"][barco]["x3"]+2
                        nuevoJuego["BarcosJ2"][barco]["movimiento"] = 1
                    else:
                        nuevoJuego["BarcosJ2"][barco]["movimiento"] = 0
                else:
                    matrizJ2[y3][x3].configure(image= vacio)
                    matrizJ2[y1][x1+1].configure(image= acorazadoHaciaDerecha1)
                    matrizJ2[y2][x2+1].configure(image= acorazadoHaciaDerecha2)
                    matrizJ2[y3][x3+1].configure(image= acorazadoHaciaDerecha3)
                    nuevoJuego["BarcosJ2"][barco]["x1"] = nuevoJuego["BarcosJ2"][barco]["x1"]+1
                    nuevoJuego["BarcosJ2"][barco]["x2"] = nuevoJuego["BarcosJ2"][barco]["x2"]+1
                    nuevoJuego["BarcosJ2"][barco]["x3"] = nuevoJuego["BarcosJ2"][barco]["x3"]+1
                    nuevoJuego["BarcosJ2"][barco]["movimiento"] = 1
                    
def listaPosicionesActualesBarcos(barcosDeJ:dict)->list:
    """Función que almacena en una lista tuplas con la posicion X y Y actuales de cada destructor 
    del jugador.

    Args:
        barcosDeJ (dict): Diccionario con la informacion de los barcos de un jugador N

    Returns:
        list: Lista de tuplas con la posicion X y Y de actuales de cada destructor del jugador
    """
    listaPosicionesActualesD= []
    for barco in barcosDeJ:
        if (barcosDeJ[barco]["vida"]==1):
            x = barcosDeJ[barco]["x1"]
            y = barcosDeJ[barco]["y1"]
            listaPosicionesActualesD.append((x,y))
        try:
            if (barcosDeJ[barco]["vida"]==1):
                x2 = barcosDeJ[barco]["x2"]
                y2 = barcosDeJ[barco]["y2"]
                listaPosicionesActualesD.append((x2,y2))
        except Exception as ex:
            pass
        try:
            if (barcosDeJ[barco]["vida"]==1):
                x3 = barcosDeJ[barco]["x3"]
                y3 = barcosDeJ[barco]["y3"]
                listaPosicionesActualesD.append((x3,y3))
        except Exception as ex:
            pass
    return(listaPosicionesActualesD)


#Destructores
destructorHaciaArriba = Image.open("b1.png")
destructorHaciaArriba = destructorHaciaArriba.resize((50, 50))  # Ajusta el tamaño de la imagen
imagenRotada = destructorHaciaArriba.rotate(90)                 # Rota la imagen según la dirección
destructorHaciaArriba = ImageTk.PhotoImage(imagenRotada)

destructorHaciaAbajo = Image.open("b1.png")
destructorHaciaAbajo = destructorHaciaAbajo.resize((50, 50))  # Ajusta el tamaño de la imagen
imagenRotada = destructorHaciaAbajo.rotate(180+90)            # Rota la imagen según la dirección
destructorHaciaAbajo = ImageTk.PhotoImage(imagenRotada)

destructorHaciaIzquierda = Image.open("b1.png")
destructorHaciaIzquierda = destructorHaciaIzquierda.resize((50, 50))  # Ajusta el tamaño de la imagen
imagenRotada = destructorHaciaIzquierda.rotate(180)                   # Rota la imagen según la dirección
destructorHaciaIzquierda = ImageTk.PhotoImage(imagenRotada)

destructorHaciaDerecha = Image.open("b1.png")
destructorHaciaDerecha = destructorHaciaDerecha.resize((50, 50))  # Ajusta el tamaño de la imagen
destructorHaciaDerecha = ImageTk.PhotoImage(destructorHaciaDerecha)

#Crucero 1
cruceroHaciaDerecha1 = Image.open("b21.png")
cruceroHaciaDerecha1 = cruceroHaciaDerecha1.resize((50, 50))  # Ajusta el tamaño de la imagen
cruceroHaciaDerecha1 = ImageTk.PhotoImage(cruceroHaciaDerecha1)

cruceroHaciaIzquierda1 = Image.open("b21.png")
cruceroHaciaIzquierda1 = cruceroHaciaIzquierda1.resize((50, 50))  # Ajusta el tamaño de la imagen
imagenRotada = cruceroHaciaIzquierda1.rotate(180)                 # Rota la imagen según la dirección
cruceroHaciaIzquierda1 = ImageTk.PhotoImage(imagenRotada)

cruceroHaciaArriba1 = Image.open("b21.png")
cruceroHaciaArriba1 = cruceroHaciaArriba1.resize((50, 50))  # Ajusta el tamaño de la imagen
imagenRotada = cruceroHaciaArriba1.rotate(90)               # Rota la imagen según la dirección
cruceroHaciaArriba1 = ImageTk.PhotoImage(imagenRotada)

cruceroHaciaAbajo1 = Image.open("b21.png")
cruceroHaciaAbajo1 = cruceroHaciaAbajo1.resize((50, 50))  # Ajusta el tamaño de la imagen
imagenRotada = cruceroHaciaAbajo1.rotate(180+90)          # Rota la imagen según la dirección
cruceroHaciaAbajo1 = ImageTk.PhotoImage(imagenRotada)

#Crucero 2
cruceroHaciaDerecha2 =Image.open("b22.png")
cruceroHaciaDerecha2 = cruceroHaciaDerecha2.resize((50, 50))  # Ajusta el tamaño de la imagen
cruceroHaciaDerecha2 = ImageTk.PhotoImage(cruceroHaciaDerecha2)

cruceroHaciaIzquierda2 =Image.open("b22.png")
cruceroHaciaIzquierda2 = cruceroHaciaIzquierda2.resize((50, 50))  # Ajusta el tamaño de la imagen
imagenRotada = cruceroHaciaIzquierda2.rotate(180)                 # Rota la imagen según la dirección
cruceroHaciaIzquierda2 = ImageTk.PhotoImage(imagenRotada)

cruceroHaciaArriba2 =Image.open("b22.png")
cruceroHaciaArriba2 = cruceroHaciaArriba2.resize((50, 50))  # Ajusta el tamaño de la imagen
imagenRotada = cruceroHaciaArriba2.rotate(90)               # Rota la imagen según la dirección
cruceroHaciaArriba2 = ImageTk.PhotoImage(imagenRotada)

cruceroHaciaAbajo2 =Image.open("b22.png")
cruceroHaciaAbajo2 = cruceroHaciaAbajo2.resize((50, 50))  # Ajusta el tamaño de la imagen
imagenRotada = cruceroHaciaAbajo2.rotate(180+90)          # Rota la imagen según la dirección
cruceroHaciaAbajo2 = ImageTk.PhotoImage(imagenRotada)

#Acorazado 1
acorazadoHaciaDerecha1 = Image.open("b31.png")
acorazadoHaciaDerecha1 = acorazadoHaciaDerecha1.resize((50, 50))  # Ajusta el tamaño de la imagen
acorazadoHaciaDerecha1 = ImageTk.PhotoImage(acorazadoHaciaDerecha1)

acorazadoHaciaIzquierda1 = Image.open("b31.png")
acorazadoHaciaIzquierda1 = acorazadoHaciaIzquierda1.resize((50, 50))  # Ajusta el tamaño de la imagen
imagenRotada = acorazadoHaciaIzquierda1.rotate(180)                   # Rota la imagen según la dirección
acorazadoHaciaIzquierda1 = ImageTk.PhotoImage(imagenRotada)

acorazadoHaciaArriba1 = Image.open("b31.png")
acorazadoHaciaArriba1 = acorazadoHaciaArriba1.resize((50, 50))  # Ajusta el tamaño de la imagen
imagenRotada = acorazadoHaciaArriba1.rotate(90)                 # Rota la imagen según la dirección
acorazadoHaciaArriba1 = ImageTk.PhotoImage(imagenRotada)

acorazadoHaciaAbajo1 = Image.open("b31.png")
acorazadoHaciaAbajo1 = acorazadoHaciaAbajo1.resize((50, 50))  # Ajusta el tamaño de la imagen
imagenRotada = acorazadoHaciaAbajo1.rotate(90+180)            # Rota la imagen según la dirección
acorazadoHaciaAbajo1 = ImageTk.PhotoImage(imagenRotada)

#Acorazado 2
acorazadoHaciaDerecha2 = Image.open("b32.png")
acorazadoHaciaDerecha2 = acorazadoHaciaDerecha2.resize((50, 50)) # Ajusta el tamaño de la imagen
acorazadoHaciaDerecha2 = ImageTk.PhotoImage(acorazadoHaciaDerecha2)

acorazadoHaciaIzquierda2 = Image.open("b32.png")
acorazadoHaciaIzquierda2 = acorazadoHaciaIzquierda2.resize((50, 50))  # Ajusta el tamaño de la imagen
imagenRotada = acorazadoHaciaIzquierda2.rotate(180)                   # Rota la imagen según la dirección
acorazadoHaciaIzquierda2 = ImageTk.PhotoImage(imagenRotada)

acorazadoHaciaArriba2 = Image.open("b32.png")
acorazadoHaciaArriba2 = acorazadoHaciaArriba2.resize((50, 50))  # Ajusta el tamaño de la imagen
imagenRotada = acorazadoHaciaArriba2.rotate(90)                 # Rota la imagen según la dirección
acorazadoHaciaArriba2 = ImageTk.PhotoImage(imagenRotada)

acorazadoHaciaAbajo2 = Image.open("b32.png")
acorazadoHaciaAbajo2 = acorazadoHaciaAbajo2.resize((50, 50))  # Ajusta el tamaño de la imagen
imagenRotada = acorazadoHaciaAbajo2.rotate(90+180)            # Rota la imagen según la dirección
acorazadoHaciaAbajo2 = ImageTk.PhotoImage(imagenRotada)

#Acorazado 3
acorazadoHaciaDerecha3 = Image.open("b33.png")
acorazadoHaciaDerecha3 = acorazadoHaciaDerecha3.resize((50, 50)) # Ajusta el tamaño de la imagen
acorazadoHaciaDerecha3 = ImageTk.PhotoImage(acorazadoHaciaDerecha3)

acorazadoHaciaIzquierda3 = Image.open("b33.png")
acorazadoHaciaIzquierda3 = acorazadoHaciaIzquierda3.resize((50, 50))  # Ajusta el tamaño de la imagen
imagenRotada = acorazadoHaciaIzquierda3.rotate(180)                   # Rota la imagen según la dirección
acorazadoHaciaIzquierda3 = ImageTk.PhotoImage(imagenRotada)

acorazadoHaciaArriba3 = Image.open("b33.png")
acorazadoHaciaArriba3 = acorazadoHaciaArriba3.resize((50, 50))  # Ajusta el tamaño de la imagen
imagenRotada = acorazadoHaciaArriba3.rotate(90)                 # Rota la imagen según la dirección
acorazadoHaciaArriba3 = ImageTk.PhotoImage(imagenRotada)

acorazadoHaciaAbajo3 = Image.open("b33.png")
acorazadoHaciaAbajo3 = acorazadoHaciaAbajo3.resize((50, 50))  # Ajusta el tamaño de la imagen
imagenRotada = acorazadoHaciaAbajo3.rotate(90+180)            # Rota la imagen según la dirección
acorazadoHaciaAbajo3 = ImageTk.PhotoImage(imagenRotada)

#Vacio
vacio= Image.open("vacio.png")
vacio = vacio.resize((50, 50))  # Ajusta el tamaño de la imagen
vacio = ImageTk.PhotoImage(vacio)

imagenGuia1= Image.open("Guia1.png")
imagenGuia1= imagenGuia1.resize((150, 150))  # Ajusta el tamaño de la imagen
imagenGuia1= ImageTk.PhotoImage(imagenGuia1)

imagenGuia2= Image.open("Guia2.png")
imagenGuia2= imagenGuia2.resize((150, 150))  # Ajusta el tamaño de la imagen
imagenGuia2= ImageTk.PhotoImage(imagenGuia2)

imagenGuia3= Image.open("Guia3.png")
imagenGuia3= imagenGuia3.resize((150, 150))  # Ajusta el tamaño de la imagen
imagenGuia3= ImageTk.PhotoImage(imagenGuia3)

imagenGuia4= Image.open("Guia4.png")
imagenGuia4= imagenGuia4.resize((150, 150))  # Ajusta el tamaño de la imagen
imagenGuia4= ImageTk.PhotoImage(imagenGuia4)

menu.mainloop()