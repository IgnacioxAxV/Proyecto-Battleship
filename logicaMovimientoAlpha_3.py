import tkinter as tk
from PIL import ImageTk, Image
import json 

matrizJ1 = []
matrizJ2 = []
cantidadDestructores = 0
limitesTablero= []

izquierda= 1
derecha= 2
arriba= 4
abajo= 3
with open(r"C:\Users\Administrator\partidas.json", "r") as file:
    partidas = json.load(file)

barcosJ1:dict = partidas["BarcosJ1"]
barcosJ2:dict = partidas["BarcosJ2"]

def colocarDestructores():
    """Función que coloca los destructores en la matriz de juego, segun la posicion en la que se guardaron
    """
    global matrizJ1
    #global matrizJ2
    global barcosJ1
    #global barcosJ2
    global destructorHaciaArriba
    global destructorHaciaAbajo
    global destructorHaciaDerecha
    global destructorHaciaIzquierda

    for barco in barcosJ1.keys():
        cont=1
        while (cont<7):
            if (barco == f"Destructor{cont}J1"):
                x = barcosJ1[barco]["x1"]
                y = barcosJ1[barco]["y1"]
                orientacion = barcosJ1[barco]["orientacion"]
                if (orientacion==izquierda):
                    orientacionBarco= destructorHaciaIzquierda
                elif (orientacion==derecha):
                    orientacionBarco= destructorHaciaDerecha
                elif (orientacion==abajo):
                    orientacionBarco= destructorHaciaAbajo
                elif (orientacion==arriba):
                    orientacionBarco= destructorHaciaArriba
                matrizJ1[y][x].configure(image= orientacionBarco)
            cont+=1
    #for barco in barcosJ2.keys():
    #    cont=1
    #    while (cont<7):
    #        if (barco== f"Destructor{cont}J2"):
    #            x= barcosJ2[barco]["x1"]
    #            y= barcosJ2[barco]["y1"]
    #            orientacion= barcosJ2[barco]["orientacion"]
    #            if (orientacion==izquierda):
    #                orientacionBarco= destructorHaciaIzquierda
    #            elif (orientacion==derecha):
    #                orientacionBarco= destructorHaciaDerecha
    #            elif (orientacion==abajo):
    #                orientacionBarco= destructorHaciaAbajo
    #            elif (orientacion==arriba):
    #                orientacionBarco= destructorHaciaArriba
    #            matrizJ2[y][x].configure(image= orientacionBarco)
    #        cont+=1
    colocarCruceros()
    colocarAcorazados()
    accionesMovimiento()


def colocarCruceros():
    """Función que coloca los cruceros en la matriz de juego, segun la posicion en la que se guardaron
    """
    global matrizJ1
    #global matrizJ2
    global barcosJ1
    #global barcosJ2
    global cruceroHaciaDerecha1
    global cruceroHaciaIzquierda1
    global cruceroHaciaAbajo1
    global cruceroHaciaArriba1
    global cruceroHaciaDerecha2
    global cruceroHaciaIzquierda2
    global cruceroHaciaAbajo2
    global cruceroHaciaArriba2

    for barco in barcosJ1.keys():
        if (barco in ["Crucero1J1", "Crucero2J1", "Crucero3J1", "Crucero4J1"]):
            x1 = barcosJ1[barco]["x1"]
            y1 = barcosJ1[barco]["y1"]
            x2 = barcosJ1[barco]["x2"]
            y2 = barcosJ1[barco]["y2"]
            orientacion = barcosJ1[barco]["orientacion"]
            if (orientacion==izquierda):
                orientacionbarco1 = cruceroHaciaIzquierda1
                orientacionbarco2 = cruceroHaciaIzquierda2
                matrizJ1[y1][x1].configure(image = orientacionbarco1)
                matrizJ1[y2][x2].configure(image = orientacionbarco2)
            elif (orientacion==derecha):
                orientacionbarco1 = cruceroHaciaDerecha1
                orientacionbarco2 = cruceroHaciaDerecha2
                matrizJ1[y1][x1].configure(image = orientacionbarco1)
                matrizJ1[y2][x2].configure(image = orientacionbarco2)
            elif (orientacion==abajo):
                orientacionbarco1 = cruceroHaciaAbajo1
                orientacionbarco2 = cruceroHaciaAbajo2
                matrizJ1[y1][x1].configure(image = orientacionbarco1)
                matrizJ1[y2][x2].configure(image = orientacionbarco2)
            elif (orientacion==arriba):
                orientacionbarco1 = cruceroHaciaArriba1
                orientacionbarco2 = cruceroHaciaArriba2
                matrizJ1[y1][x1].configure(image = orientacionbarco1)
                matrizJ1[y2][x2].configure(image = orientacionbarco2)

def colocarAcorazados():
    """Función que coloca los acorazados en la matriz de juego, segun la posicion en la que se guardaron
    """
    global matrizJ1
    #global matrizJ2
    global barcosJ1
    #global barcosJ2
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
    
    for barco in barcosJ1.keys():
        if (barco in ["Acorazado1J1", "Acorazado2J1"]):
            x1 = barcosJ1[barco]["x1"]
            y1 = barcosJ1[barco]["y1"]
            x2 = barcosJ1[barco]["x2"]
            y2 = barcosJ1[barco]["y2"]
            x3 = barcosJ1[barco]["x3"]
            y3 = barcosJ1[barco]["y3"]
            orientacion = barcosJ1[barco]["orientacion"]

            if (orientacion==izquierda):
                orientacionbarco1 = acorazadoHaciaIzquierda1
                orientacionbarco2 = acorazadoHaciaIzquierda2
                orientacionbarco3 = acorazadoHaciaIzquierda3
                matrizJ1[y1][x1].configure(image = orientacionbarco1)
                matrizJ1[y2][x2].configure(image = orientacionbarco2)
                matrizJ1[y3][x3].configure(image = orientacionbarco3)

            elif (orientacion==derecha):
                orientacionbarco1 = acorazadoHaciaDerecha1
                orientacionbarco2 = acorazadoHaciaDerecha2
                orientacionbarco3 = acorazadoHaciaDerecha3
                matrizJ1[y1][x1].configure(image = orientacionbarco1)
                matrizJ1[y2][x2].configure(image = orientacionbarco2)
                matrizJ1[y3][x3].configure(image = orientacionbarco3)

            elif (orientacion==abajo):
                orientacionbarco1 = acorazadoHaciaAbajo1
                orientacionbarco2 = acorazadoHaciaAbajo2
                orientacionbarco3 = acorazadoHaciaAbajo3
                matrizJ1[y1][x1].configure(image = orientacionbarco1)
                matrizJ1[y2][x2].configure(image = orientacionbarco2)
                matrizJ1[y3][x3].configure(image = orientacionbarco3)

            elif (orientacion==arriba):
                orientacionbarco1 = acorazadoHaciaArriba1
                orientacionbarco2 = acorazadoHaciaArriba2
                orientacionbarco3 = acorazadoHaciaArriba3
                matrizJ1[y1][x1].configure(image = orientacionbarco1)
                matrizJ1[y2][x2].configure(image = orientacionbarco2)
                matrizJ1[y3][x3].configure(image = orientacionbarco3)
    
def eliminarImagen (x,y):
    """Función que elimina una imagen en una posicion deseada

    Args:
        x (int): Posicion x
        y (int): Posicion y
    """
    global matrizJ1
    matrizJ1[y][x].configure(image=vacio)

def accionesMovimiento():
    """Función que itera en los barcos para que ingresen a la funcion de movimiento
    """
    global barcosJ1
    global barcosJ2
    movimientoDestructores()
    movimientoCruceros()

def movimientoDestructores():
    """Función encargada de validar y realizar los movimientos sobre los Destructores
        
    Args:
        infBarco (list): Lista con la información del barco que entra a la función
    """
    global matrizJ1
    global matrizJ2
    global barcosJ1
    global barcosJ2
    for barco in barcosJ1:
        cont=1
        while (cont<7):
            if (barco== f"Destructor{cont}J1"):
                y= barcosJ1[barco]["y1"]
                x= barcosJ1[barco]["x1"]
                listaPosicionesBarcos= listaPosicionesActualesBarcos(barcosJ1)
                if (barcosJ1[barco]["vida"]==0):
                    y= barcosJ1[barco]["y1"]
                    x= barcosJ1[barco]["x1"]
                    matrizJ1[y][x].configure(image = vacio)
                    #del barcosJ1[barco]

                elif (barcosJ1[barco]["orientacion"]==arriba):
                    if (barcosJ1[barco]["y1"]==0):
                        barcosJ1[barco]["orientacion"]= abajo
                        matrizJ1[y][x].configure(image= destructorHaciaAbajo)
                    elif(listaPosicionesBarcos.count((x,y-1))>=1):
                        if (barcosJ1[barco]["movimiento"]==0):
                            barcosJ1[barco]["orientacion"]= abajo
                            matrizJ1[y][x].configure(image= destructorHaciaAbajo)
                            barcosJ1[barco]["movimiento"] = 1
                        else:
                            barcosJ1[barco]["movimiento"] = 0
                    else:
                        matrizJ1[y][x].configure(image= vacio)
                        matrizJ1[y-1][x].configure(image= destructorHaciaArriba)
                        barcosJ1[barco]["y1"]= barcosJ1[barco]["y1"]-1

                elif (barcosJ1[barco]["orientacion"]==abajo):
                    if (barcosJ1[barco]["y1"]==limitesTablero[1]-1):
                        barcosJ1[barco]["orientacion"]= arriba
                        matrizJ1[y][x].configure(image= destructorHaciaArriba)
                    elif(listaPosicionesBarcos.count((x,y+1))>=1):
                        if (barcosJ1[barco]["movimiento"]==0):
                            barcosJ1[barco]["orientacion"]= arriba
                            matrizJ1[y][x].configure(image= destructorHaciaArriba)
                            barcosJ1[barco]["movimiento"] = 1
                        else:
                            barcosJ1[barco]["movimiento"] = 0
                    else:
                        matrizJ1[y][x].configure(image= vacio)
                        matrizJ1[y+1][x].configure(image= destructorHaciaAbajo)
                        barcosJ1[barco]["y1"]= barcosJ1[barco]["y1"]+1

                elif (barcosJ1[barco]["orientacion"]==izquierda):
                    if (barcosJ1[barco]["x1"]==0):
                        barcosJ1[barco]["orientacion"]= derecha
                        matrizJ1[y][x].configure(image= destructorHaciaDerecha)
                    elif(listaPosicionesBarcos.count((x-1,y))>=1):
                        if (barcosJ1[barco]["movimiento"]==0):
                            barcosJ1[barco]["orientacion"]= derecha
                            matrizJ1[y][x].configure(image= destructorHaciaDerecha)
                            barcosJ1[barco]["movimiento"] = 1
                        else:
                            barcosJ1[barco]["movimiento"] = 0
                    else:
                        matrizJ1[y][x].configure(image= vacio)
                        matrizJ1[y][x-1].configure(image= destructorHaciaIzquierda)
                        barcosJ1[barco]["x1"]= barcosJ1[barco]["x1"]-1

                elif (barcosJ1[barco]["orientacion"]==derecha):
                    if (barcosJ1[barco]["x1"]==limitesTablero[0]-1):
                        barcosJ1[barco]["orientacion"]= izquierda
                        matrizJ1[y][x].configure(image= destructorHaciaIzquierda)
                    elif(listaPosicionesBarcos.count((x+1,y))>=1):
                        if (barcosJ1[barco]["movimiento"]==0):
                            barcosJ1[barco]["orientacion"]= izquierda
                            matrizJ1[y][x].configure(image= destructorHaciaIzquierda)
                            barcosJ1[barco]["movimiento"] = 1
                        else:
                            barcosJ1[barco]["movimiento"] = 0
                    else:
                        matrizJ1[y][x].configure(image= vacio)
                        matrizJ1[y][x+1].configure(image= destructorHaciaDerecha)
                        barcosJ1[barco]["x1"]= barcosJ1[barco]["x1"]+1
            cont+=1

def movimientoCruceros():
    """Función encargada de validar y realizar los movimientos sobre los barcos
    """
    global matrizJ1
    global matrizJ2
    global barcosJ1
    global barcosJ2
    for barco in barcosJ1.keys():
        if (barco in ["Crucero1J1", "Crucero2J1", "Crucero3J1", "Crucero4J1"]):
            x1 = barcosJ1[barco]["x1"]
            y1 = barcosJ1[barco]["y1"]
            x2 = barcosJ1[barco]["x2"]
            y2 = barcosJ1[barco]["y2"]
            #orientacion = barcosJ1[barco]["orientacion"]
            listaPosicionesBarcos = listaPosicionesActualesBarcos(barcosJ1)
            if (barcosJ1[barco]["vida"]==0):
                pass # Validacion pendiente

            elif (barcosJ1[barco]["orientacion"]==arriba):
                if (barcosJ1[barco]["y1"]==0):
                    barcosJ1[barco]["orientacion"] = abajo
                    matrizJ1[y1][x1].configure(image= cruceroHaciaAbajo2)
                    matrizJ1[y2][x2].configure(image= cruceroHaciaAbajo1)
                    barcosJ1[barco]["y1"] = barcosJ1[barco]["y1"]+1
                    barcosJ1[barco]["y2"] = barcosJ1[barco]["y2"]-1
                elif (listaPosicionesBarcos.count((x1,y1-1))>=1):
                    if (barcosJ1[barco]["movimiento"]==0):
                        barcosJ1[barco]["orientacion"]= abajo
                        matrizJ1[y1][x1].configure(image= cruceroHaciaAbajo2)
                        matrizJ1[y2][x2].configure(image= cruceroHaciaAbajo1)
                        barcosJ1[barco]["y1"] = barcosJ1[barco]["y1"]+1
                        barcosJ1[barco]["y2"] = barcosJ1[barco]["y2"]-1
                        barcosJ1[barco]["movimiento"] = 1
                    else:
                        barcosJ1[barco]["movimiento"] = 0
                else:
                    matrizJ1[y2][x2].configure(image= vacio)
                    matrizJ1[y1-1][x1].configure(image= cruceroHaciaArriba1)
                    matrizJ1[y2-1][x2].configure(image= cruceroHaciaArriba2)
                    barcosJ1[barco]["y1"]= barcosJ1[barco]["y1"]-1
                    barcosJ1[barco]["y2"]= barcosJ1[barco]["y2"]-1

            elif (barcosJ1[barco]["orientacion"]==abajo):
                if (barcosJ1[barco]["y1"]==limitesTablero[1]-1):
                    barcosJ1[barco]["orientacion"] = arriba
                    barcosJ1[barco]["y1"] = barcosJ1[barco]["y1"]-1
                    barcosJ1[barco]["y2"] = barcosJ1[barco]["y2"]+1
                    matrizJ1[y1][x1].configure(image= cruceroHaciaArriba2)
                    matrizJ1[y2][x2].configure(image= cruceroHaciaArriba1)
                elif (listaPosicionesBarcos.count((x1,y1+1))>=1):
                    if (barcosJ1[barco]["movimiento"]==0):
                        barcosJ1[barco]["orientacion"]= arriba
                        matrizJ1[y1][x1].configure(image= cruceroHaciaArriba2)
                        matrizJ1[y2][x2].configure(image= cruceroHaciaArriba1)
                        barcosJ1[barco]["y1"] = barcosJ1[barco]["y1"]-1
                        barcosJ1[barco]["y2"] = barcosJ1[barco]["y2"]+1
                        barcosJ1[barco]["movimiento"] = 1
                    else:
                        barcosJ1[barco]["movimiento"] = 0
                else:
                    matrizJ1[y2][x2].configure(image = vacio)
                    matrizJ1[y1+1][x1].configure(image= cruceroHaciaAbajo1)
                    matrizJ1[y2+1][x2].configure(image= cruceroHaciaAbajo2)
                    barcosJ1[barco]["y1"]= barcosJ1[barco]["y1"]+1
                    barcosJ1[barco]["y2"]= barcosJ1[barco]["y2"]+1
                
            elif (barcosJ1[barco]["orientacion"]==izquierda):
                if (barcosJ1[barco]["x1"]==0):
                    barcosJ1[barco]["orientacion"] = derecha
                    barcosJ1[barco]["x1"] = barcosJ1[barco]["x1"]+1
                    barcosJ1[barco]["x2"] = barcosJ1[barco]["x2"]-1
                    matrizJ1[y1][x1].configure(image= cruceroHaciaDerecha2)
                    matrizJ1[y2][x2].configure(image= cruceroHaciaDerecha1)
                elif (listaPosicionesBarcos.count((x1-1,y1))>=1):
                    if (barcosJ1[barco]["movimiento"]==0):
                        barcosJ1[barco]["orientacion"] = derecha
                        barcosJ1[barco]["x1"] = barcosJ1[barco]["x1"]+1
                        barcosJ1[barco]["x2"] = barcosJ1[barco]["x2"]-1
                        matrizJ1[y1][x1].configure(image= cruceroHaciaDerecha2)
                        matrizJ1[y2][x2].configure(image= cruceroHaciaDerecha1)
                        barcosJ1[barco]["movimiento"] = 1
                    else:
                        barcosJ1[barco]["movimiento"] = 0
                else:
                    matrizJ1[y2][x2].configure(image = vacio)
                    matrizJ1[y1][x1-1].configure(image= cruceroHaciaIzquierda1)
                    matrizJ1[y2][x2-1].configure(image= cruceroHaciaIzquierda2)
                    barcosJ1[barco]["x1"]= barcosJ1[barco]["x1"]-1
                    barcosJ1[barco]["x2"]= barcosJ1[barco]["x2"]-1

            elif (barcosJ1[barco]["orientacion"]==derecha):
                if (barcosJ1[barco]["x1"]==limitesTablero[0]-1):
                    barcosJ1[barco]["orientacion"] = izquierda
                    barcosJ1[barco]["x1"] = barcosJ1[barco]["x1"]-1
                    barcosJ1[barco]["x2"] = barcosJ1[barco]["x2"]+1
                    matrizJ1[y1][x1].configure(image= cruceroHaciaIzquierda2)
                    matrizJ1[y2][x2].configure(image= cruceroHaciaIzquierda1)
                elif (listaPosicionesBarcos.count((x1+1,y1))>=1):
                    if (barcosJ1[barco]["movimiento"]==0):
                        barcosJ1[barco]["orientacion"] = izquierda
                        barcosJ1[barco]["x1"] = barcosJ1[barco]["x1"]-1
                        barcosJ1[barco]["x2"] = barcosJ1[barco]["x2"]+1
                        matrizJ1[y1][x1].configure(image= cruceroHaciaIzquierda2)
                        matrizJ1[y2][x2].configure(image= cruceroHaciaIzquierda1)
                        barcosJ1[barco]["movimiento"] = 1
                    else:
                        barcosJ1[barco]["movimiento"] = 0
                else:
                    matrizJ1[y2][x2].configure(image = vacio)
                    matrizJ1[y1][x1+1].configure(image= cruceroHaciaDerecha1)
                    matrizJ1[y2][x2+1].configure(image= cruceroHaciaDerecha2)
                    barcosJ1[barco]["x1"]= barcosJ1[barco]["x1"]+1
                    barcosJ1[barco]["x2"]= barcosJ1[barco]["x2"]+1

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
        x = barcosDeJ[barco]["x1"]
        y = barcosDeJ[barco]["y1"]
        try:
            x2 = barcosDeJ[barco]["x2"]
            y2 = barcosDeJ[barco]["y2"]
            listaPosicionesActualesD.append((x2,y2))
        except Exception as ex:
            pass
        try:
            x3 = barcosDeJ[barco]["x3"]
            y3 = barcosDeJ[barco]["y3"]
            listaPosicionesActualesD.append((x3,y3))
        except Exception as ex:
            pass
        listaPosicionesActualesD.append((x,y))
    return(listaPosicionesActualesD)

def tablero (x:int,y:int)->tk.Tk:
    """Función que crea un tablero el cual es una matriz de botones 

    Args:
        x (int): Posicion x
        y (int): Posicion y

    Returns:
        tk.Tk: Ventana del tablero
    """
    global limitesTablero
    limitesTablero.append(x)
    limitesTablero.append(y)
    global matrizJ1
    juego = tk.Tk()
    juego.title("Battleship")
    resolucion=f"{x*50}x{y*50}+0+0"
    juego.geometry(resolucion)

    matrizJ1= [[tk.Button(juego,bg="#00FFFF",command= colocarDestructores)
                     for c in range(x)]for f in range(y)]
    posX= 0
    posY= 0
    for filaBotones in matrizJ1:
        posX=0
        for btn in filaBotones:
            btn.place(x=posX, y=posY)
            btn.configure(height=50, width=50)
            posX+=50
        posY+=50
    return juego

juego= tablero(10,10)        

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

juego.mainloop()