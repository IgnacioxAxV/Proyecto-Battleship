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
with open(r"C:\Users\Wilmer\OneDrive - Estudiantes ITCR\Desktop\Proyecto\partidas.json", "r") as file:
    partidas = json.load(file)

barcosJ1:dict = partidas["BarcosJ1"]
barcosJ2:dict = partidas["BarcosJ2"]

#for i in barcosJ1.keys():
#    print(i)
#    print(barcosJ1[i])

def colocarDestructores():
    global matrizJ1
    global barcosJ1
    global destructorHaciaArriba
    global destructorHaciaAbajo
    global destructorHaciaDerecha
    global destructorHaciaIzquierda

    for barco in barcosJ1.keys():
        cont=1
        while (cont<7):
            if (barco== f"Destructor{cont}J1"):
                x= barcosJ1[barco]["x1"]
                y= barcosJ1[barco]["y1"]
                orientacion= barcosJ1[barco]["orientacion"]
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
    for barco in barcosJ2.keys():
        cont=1
        while (cont<7):
            if (barco== f"Destructor{cont}J1"):
                x= barcosJ1[barco]["x1"]
                y= barcosJ1[barco]["y1"]
                orientacion= barco["orientacion"]
                if (orientacion==izquierda):
                    orientacionBarco= destructorHaciaIzquierda
                elif (orientacion==derecha):
                    orientacionBarco= destructorHaciaDerecha
                elif (orientacion==abajo):
                    orientacionBarco= destructorHaciaAbajo
                elif (orientacion==arriba):
                    orientacionBarco= destructorHaciaArriba
                matrizJ2[y][x].configure(image= orientacionBarco)
            cont+=1
    accionesMovimiento()


"""def accion (x,y):
    global matrizJ1
    global imagen
    matrizJ1[y][x].configure(image=imagen)"""

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

def movimientoDestructores():
    """Función encargada de validar y realizar los movimientos sobre los barcos
        
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

                if (barcosJ1[barco]["orientacion"]==arriba):
                    if (barcosJ1[barco]["y1"]==0):
                        barcosJ1[barco]["orientacion"]= abajo
                        y= barcosJ1[barco]["y1"]
                        x= barcosJ1[barco]["x1"]
                        matrizJ1[y][x].configure(image= destructorHaciaAbajo)
                    else:
                        y= barcosJ1[barco]["y1"]
                        x= barcosJ1[barco]["x1"]
                        matrizJ1[y][x].configure(image= vacio)
                        matrizJ1[y-1][x].configure(image= destructorHaciaArriba)
                        barcosJ1[barco]["y1"]= barcosJ1[barco]["y1"]-1

                elif (barcosJ1[barco]["orientacion"]==abajo):
                    if (barcosJ1[barco]["y1"]==limitesTablero[1]-1):
                        barcosJ1[barco]["orientacion"]= arriba
                        y= barcosJ1[barco]["y1"]
                        x= barcosJ1[barco]["x1"]
                        matrizJ1[y][x].configure(image= destructorHaciaArriba)
                    else:
                        y= barcosJ1[barco]["y1"]
                        x= barcosJ1[barco]["x1"]
                        matrizJ1[y][x].configure(image= vacio)
                        matrizJ1[y+1][x].configure(image= destructorHaciaAbajo)
                        barcosJ1[barco]["y1"]= barcosJ1[barco]["y1"]+1

                elif (barcosJ1[barco]["orientacion"]==izquierda):
                    if (barcosJ1[barco]["x1"]==0):
                        barcosJ1[barco]["orientacion"]= derecha
                        y= barcosJ1[barco]["y1"]
                        x= barcosJ1[barco]["x1"]
                        matrizJ1[y][x].configure(image= destructorHaciaDerecha)
                    else:
                        y= barcosJ1[barco]["y1"]
                        x= barcosJ1[barco]["x1"]
                        matrizJ1[y][x].configure(image= vacio)
                        matrizJ1[y][x-1].configure(image= destructorHaciaIzquierda)
                        barcosJ1[barco]["x1"]= barcosJ1[barco]["x1"]-1

                elif (barcosJ1[barco]["orientacion"]==derecha):
                    if (barcosJ1[barco]["x1"]==limitesTablero[0]-1):
                        barcosJ1[barco]["orientacion"]= izquierda
                        y= barcosJ1[barco]["y1"]
                        x= barcosJ1[barco]["x1"]
                        matrizJ1[y][x].configure(image= destructorHaciaIzquierda)
                    else:
                        y= barcosJ1[barco]["y1"]
                        x= barcosJ1[barco]["x1"]
                        matrizJ1[y][x].configure(image= vacio)
                        matrizJ1[y][x+1].configure(image= destructorHaciaDerecha)
                        barcosJ1[barco]["x1"]= barcosJ1[barco]["x1"]+1
            cont+=1

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

destructorHaciaArriba = Image.open("b1.png")
destructorHaciaArriba = destructorHaciaArriba.resize((50, 50))  # Ajusta el tamaño de la imagen
imagenRotada = destructorHaciaArriba.rotate(90)
destructorHaciaArriba = ImageTk.PhotoImage(imagenRotada)

destructorHaciaAbajo = Image.open("b1.png")
destructorHaciaAbajo = destructorHaciaAbajo.resize((50, 50))  # Ajusta el tamaño de la imagen
rotar = destructorHaciaAbajo.rotate(180+90)
destructorHaciaAbajo= ImageTk.PhotoImage(rotar)

destructorHaciaIzquierda = Image.open("b1.png")
destructorHaciaIzquierda = destructorHaciaIzquierda.resize((50, 50))  # Ajusta el tamaño de la imagen
rotar = destructorHaciaIzquierda.rotate(180)
destructorHaciaIzquierda= ImageTk.PhotoImage(rotar)

destructorHaciaDerecha = Image.open("b1.png")
destructorHaciaDerecha = destructorHaciaDerecha.resize((50, 50))  # Ajusta el tamaño de la imagen
destructorHaciaDerecha= ImageTk.PhotoImage(destructorHaciaDerecha)

vacio= Image.open("vacio.png")
vacio = vacio.resize((50, 50))  # Ajusta el tamaño de la imagen
vacio = ImageTk.PhotoImage(vacio)

juego.mainloop()