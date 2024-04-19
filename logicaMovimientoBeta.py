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

nuevoJuego = {
    "Matriz": {"Columnas": 20,"Filas": 10, "matrizJ1": [], "matriJ2": []},
    "NombrePartida": "Abd",
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
        "Destructor1J1": {"vida": 1, "x1": 0, "y1": 0 ,"orientacion": 1, "movimiento":1, "disparos":0} ,
        "Destructor2J1": {"vida": 1, "x1": 1, "y1": 4 ,"orientacion": 2, "movimiento":1, "disparos":0} ,
        "Destructor3J1": {"vida": 1, "x1": 2, "y1": 9 ,"orientacion": 4, "movimiento":1, "disparos":0} ,
        "Destructor4J1": {"vida": 1, "x1": 5, "y1": 1 ,"orientacion": 3, "movimiento":1, "disparos":0} ,
        "Destructor5J1": {"vida": 1, "x1": 6, "y1": 8 ,"orientacion": 2, "movimiento":1, "disparos":0}, 
        "Destructor6J1": {"vida": 1, "x1": 3, "y1": 5 ,"orientacion": 1, "movimiento":1, "disparos":0}, 

        "Crucero1J1":  {"vida": 1, "x1": 3, "y1": 2, "x2": 4 , "y2": 2, "orientacion": 1, "movimiento":1, "disparos":0, "xy1":0, "xy2":0},
        "Crucero2J1":  {"vida": 1, "x1": 9, "y1": 4, "x2": 9 , "y2": 5, "orientacion": 4, "movimiento":1, "disparos":0, "xy1":0, "xy2":0},
        "Crucero3J1":  {"vida": 1, "x1": 4, "y1": 9, "x2": 4 , "y2": 8, "orientacion": 3, "movimiento":1, "disparos":0, "xy1":0, "xy2":0},
        "Crucero4J1":  {"vida": 1, "x1": 8, "y1": 0, "x2": 7 , "y2": 0, "orientacion": 2, "movimiento":1, "disparos":0, "xy1":0, "xy2":0},

        "Acorazado1J1": {"vida": 1, "x1": 6, "y1": 5,"x2": 6, "y2": 4,"x3": 6, "y3": 3, "orientacion": 3, "movimiento":1, "disparos":0, "xy1":0, "xy2":0, "xy3":0},
        "Acorazado2J1": {"vida": 1, "x1": 0, "y1": 6,"x2": 1, "y2": 6,"x3": 2, "y3": 6, "orientacion": 1, "movimiento":1, "disparos":0, "xy1":0, "xy2":0, "xy3":0}
        },

    "BarcosJ2": {                   
        "Destructor1J2": {"vida": 1, "x1": 9, "y1": 8 ,"orientacion": 1, "movimiento":1, "disparos":0} ,
        "Destructor2J2": {"vida": 1, "x1": 4, "y1": 6 ,"orientacion": 2, "movimiento":1, "disparos":0} ,
        "Destructor3J2": {"vida": 1, "x1": 1, "y1": 1 ,"orientacion": 3, "movimiento":1, "disparos":0} ,
        "Destructor4J2": {"vida": 1, "x1": 9, "y1": 9 ,"orientacion": 4, "movimiento":1, "disparos":0} ,
        "Destructor5J2": {"vida": 1, "x1": 5, "y1": 4 ,"orientacion": 1, "movimiento":1, "disparos":0} ,
        "Destructor6J2": {"vida": 1, "x1": 0, "y1": 7 ,"orientacion": 2, "movimiento":1, "disparos":0} ,

        "Crucero1J2": {"vida": 1, "x1": 0, "y1": 3, "x2": 0 , "y2": 2, "orientacion": 3, "movimiento":1, "disparos":0},
        "Crucero2J2": {"vida": 1, "x1": 6, "y1": 7, "x2": 7 , "y2": 7, "orientacion": 1, "movimiento":1, "disparos":0},
        "Crucero3J2": {"vida": 1, "x1": 9, "y1": 1, "x2": 2 , "y2": 4, "orientacion": 4, "movimiento":1, "disparos":0},
        "Crucero4J2": {"vida": 1, "x1": 1, "y1": 9, "x2": 0 , "y2": 9, "orientacion": 2, "movimiento":1, "disparos":0},

        "Acorazado1J2": {"vida": 1, "x1": 2, "y1": 3,"x2": 3, "y2": 3, "x3": 4, "y3": 3, "orientacion": 1, "movimiento":1, "disparos":0},
        "Acorazado2J2": {"vida": 1, "x1": 6, "y1": 0,"x2": 6, "y2": 1, "x3": 6, "y3": 2, "orientacion": 4, "movimiento":1, "disparos":0}
        }
}

def colocarDestructores():
    """Función que coloca los destructores en la matriz de juego, segun la posicion en la que se guardaron
    """
    global matrizJ1
    global matrizJ2

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
                pass

            elif (orientacion==izquierda):          # Se valida la orientacion del barco para colocarlo
                orientacionBarco= destructorHaciaIzquierda
            elif (orientacion==derecha):            # Se valida la orientacion del barco para colocarlo
                orientacionBarco= destructorHaciaDerecha
            elif (orientacion==abajo):              # Se valida la orientacion del barco para colocarlo
                orientacionBarco= destructorHaciaAbajo
            elif (orientacion==arriba):             # Se valida la orientacion del barco para colocarlo
                orientacionBarco= destructorHaciaArriba

            matrizJ1[y][x].configure(image= orientacionBarco)

    for barco in nuevoJuego["BarcosJ2"].keys():       # Se ejecuta la funcion colocarDestructores para jugador 2
        if (barco in ["Destructor1J2", "Destructor2J2", "Destructor3J2", "Destructor4J2", "Destructor5J2", "Destructor6J2"]):
                x= nuevoJuego["BarcosJ2"][barco]["x1"]
                y= nuevoJuego["BarcosJ2"][barco]["y1"]
                orientacion= nuevoJuego["BarcosJ2"][barco]["orientacion"]

                if (nuevoJuego["BarcosJ2"][barco]["vida"]==0):        # Se valida si el barco aun sigue a flote o ya fue hundido
                    pass

                elif (orientacion==izquierda):          # Se valida la orientacion del barco para colocarlo
                    orientacionBarco= destructorHaciaIzquierda
                elif (orientacion==derecha):            # Se valida la orientacion del barco para colocarlo
                    orientacionBarco= destructorHaciaDerecha
                elif (orientacion==abajo):              # Se valida la orientacion del barco para colocarlo
                    orientacionBarco= destructorHaciaAbajo
                elif (orientacion==arriba):             # Se valida la orientacion del barco para colocarlo
                    orientacionBarco= destructorHaciaArriba

                matrizJ2[y][x].configure(image= orientacionBarco)

def colocarCruceros():
    """Función que coloca los cruceros en la matriz de juego, segun la posicion en la que se guardaron
    """
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
    
                matrizJ1[y][x].configure(image=vacio)

def colocarBarcos():
    """Funcion que itera en los jugadores para agregar los barcos a los tableros
    """
    colocarDestructores()
    colocarCruceros()
    colocarAcorazados()

    accionesMovimiento()

def accionesMovimiento():
    """Función que itera en los barcos para que ingresen a la funcion de movimiento
    """
    movimientoDestructores()
    movimientoCruceros()
    movimientoAcorazados()

def movimientoDestructores():
    """Función encargada de validar y realizar los movimientos sobre los Destructores
    """
    global matrizJ1
    global matrizJ2

    for barco in nuevoJuego["BarcosJ1"].keys():       # Se ejecuta la funcion movimientoDestructores para los barcos del jugador 1
        if (barco in ["Destructor1J1", "Destructor2J1", "Destructor3J1", "Destructor4J1", "Destructor5J1", "Destructor6J1"]):
            y= nuevoJuego["BarcosJ1"][barco]["y1"]
            x= nuevoJuego["BarcosJ1"][barco]["x1"]
            listaPosicionesBarcos= listaPosicionesActualesBarcos(nuevoJuego["BarcosJ1"])
            if (nuevoJuego["BarcosJ1"][barco]["vida"]==0):        # Se valida si el barco aun sigue a flote o ya fue hundido
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
                pass 

            elif (nuevoJuego["BarcosJ2"][barco]["disparos"]!=0):      # Se valida si el barco ya recibio un disparo
                pass

            elif (nuevoJuego["BarcosJ2"][barco]["orientacion"]==arriba):      # Se valida la orientacion del barco para moverlo
                if (listaPosicionesBarcos.count((x,y-1))==0 and listaPosicionesBarcos.count((x,y-2))==0 and y-2 >=0): # Se valida si puede avanzar 2 casillas
                    matrizJ2[y][x].configure(image= vacio)
                    matrizJ2[y-2][x].configure(image= destructorHaciaArriba)
                    nuevoJuego["BarcosJ2"][barco]["x1"]= nuevoJuego["BarcosJ2"][barco]["x1"]-2
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
                    nuevoJuego["BarcosJ2"][barco]["x1"]= nuevoJuego["BarcosJ2"][barco]["x1"]+2
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
                    nuevoJuego["BarcosJ1"][barco]["y1"] = nuevoJuego["rcosJ1"][barco]["y1"]+1
                    nuevoJuego["BarcosJ1"][barco]["y2"] = nuevoJuego["rcosJ1"][barco]["y2"]+1
                    nuevoJuego["BarcosJ1"][barco]["y3"] = nuevoJuego["rcosJ1"][barco]["y3"]+1
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
                    nuevoJuego["barcosJ2"][barco]["y3"] = nuevoJuego["BarcosJ2"][barco]["y3"]-2
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
                        nuevoJuego["barcosJ2"][barco]["movimiento"] = 0
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
                        nuevoJuego["BarcosJ2"]                
                else:
                    matrizJ2[y3][x3].configure(image= vacio)
                    matrizJ2[y1+1][x1].configure(image= acorazadoHaciaAbajo1)
                    matrizJ2[y2+1][x2].configure(image= acorazadoHaciaAbajo2)
                    matrizJ2[y3+1][x3].configure(image= acorazadoHaciaAbajo3)
                    nuevoJuego["barcosJ2"][barco]["y1"] = nuevoJuego["BarcosJ2"][barco]["y1"]+1
                    nuevoJuego["barcosJ2"][barco]["y2"] = nuevoJuego["BarcosJ2"][barco]["y2"]+1
                    nuevoJuego["barcosJ2"][barco]["y3"] = nuevoJuego["BarcosJ2"][barco]["y3"]+1
                    nuevoJuego["barcosJ2"][barco]["movimiento"] = 1

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

#juego= tablero(10,10)        
y = nuevoJuego["Matriz"]["Filas"]
x = nuevoJuego["Matriz"]["Columnas"]//2
juego= tablero(x=x,y=y)

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