import tkinter as tk
from PIL import ImageTk, Image

matrizBotones = []
cantidadDestructores = 0
limitesTablero= []

destructores = {"destructor0":["vertical",0,0,"arriba"],
                "destructor1":["vertical",0,0,"arriba"],
                "destructor2":["vertical",0,0,"arriba"],
                "destructor3":["vertical",0,0,"arriba"],
                "destructor4":["vertical",0,0,"arriba"],
                "destructor5":["vertical",0,0,"arriba"],}



def accion (x,y):
    """Función que coloca un barco en el boton seleccionado

    Args:
        x (int): Posicion x
        y (int): Posicion y
    """
    #print (f"x={x},y={y}")

    global matrizBotones
    global imagen
    matrizBotones[y][x].configure(image=imagen)

def eliminarImagen (x,y):
    """Función que elimina una imagen en una posicion deseada

    Args:
        x (int): Posicion x
        y (int): Posicion y
    """
    global matrizBotones
    matrizBotones[y][x].configure(image=vacio)

def limiteDestructores(x,y):
    """Funcion que delimita la cantidad de destructores a colocar

    Args:
        x (int): Posicion x
        y (int): Posicion y
    """
    global cantidadDestructores
    if (cantidadDestructores==6):
        accionesMovimiento()
    else:
        destructores[f"destructor{cantidadDestructores}"][1]= x
        destructores[f"destructor{cantidadDestructores}"][2]= y
        #destructores[f"destructor{cantidadDestructores}"].append(y)
        #print(destructores)
        accion(x,y)
        cantidadDestructores+=1
        

def accionesMovimiento():
    """Función que itera en los barcos para que ingresen a la funcion de movimiento
    """
    global destructores
    for barcos in destructores.keys():
        infbarco = destructores[barcos]
        movimiento(infbarco)
        

def movimiento(infBarco:list):
    """Función encargada de validar y realizar los movimientos sobre los barcos

    Args:
        infBarco (list): Lista con la del barco que entra a la función
    """
    global matrizBotones
    global destructores
    if (infBarco[0]== "vertical"):          #Pregunta orientacion del barco
        if (infBarco[3]== "arriba"):        #Pregunta si el barco va hacia arriba
            if (infBarco[2]==0):            #Pregunta si el barco esta en el borde superior 
                matrizBotones[infBarco[2]][infBarco[1]].configure(image= destructorHaciaAbajo)  #Cambia la direccion del barco
                cont= 0
                for values in destructores.values():
                    if (values==infBarco):
                        destructores[f"destructor{cont}"]= ["vertical",infBarco[1],infBarco[2],"abajo"] #Cambia la direccion del barco en el diccionario
                    cont+= 1
            else:
                eliminarImagen(x=infBarco[1], y=infBarco[2])
                matrizBotones[infBarco[2]-1][infBarco[1]].configure(image= imagen)
                cont= 0
                for values in destructores.values():
                    if (values==infBarco):
                        destructores[f"destructor{cont}"]= ["vertical",infBarco[1],infBarco[2]-1,"arriba"]
                    cont+= 1
        elif (infBarco[3]== "abajo"):       #Pregunta si el barco va hacia abajo
            if (infBarco[2]==9):            #Pregunta si el barco esta en el borde inferior
                matrizBotones[infBarco[2]][infBarco[1]].configure(image= imagen)    #Cambia la direccion del barco
                cont= 0
                for values in destructores.values():
                    if (values==infBarco):
                        destructores[f"destructor{cont}"]= ["vertical",infBarco[1],infBarco[2],"arriba"] #Cambia la direccion del barco en el diccionario
                    cont+= 1
            else:
                eliminarImagen(x=infBarco[1], y=infBarco[2])
                matrizBotones[infBarco[2]+1][infBarco[1]].configure(image= destructorHaciaAbajo)
                cont= 0
                for values in destructores.values():
                    if (values==infBarco):
                        destructores[f"destructor{cont}"]= ["vertical",infBarco[1],infBarco[2]+1,"abajo"]
                    cont+= 1
    if (infBarco[0]== "horizontal"):            #Pregunta orientacion del barco
        print ("UBBBKBKSUIAJLBO")

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
    print(limitesTablero)
    global matrizBotones
    juego = tk.Tk()
    juego.title("Battleship")
    resolucion=f"{x*50}x{y*50}+0+0"
    juego.geometry(resolucion)

    matrizBotones= [[tk.Button(juego,bg="#00FFFF",command= lambda x=c, y=f:limiteDestructores(x,y))
                     for c in range(x)]for f in range(y)]
    posX= 0
    posY= 0
    for filaBotones in matrizBotones:
        posX=0
        for btn in filaBotones:
            btn.place(x=posX, y=posY)
            btn.configure(height=50, width=50)
            posX+=50
        posY+=50
    return juego

juego= tablero(20,10)        

imagen = Image.open("b1.png")
imagen = imagen.resize((50, 50))  # Ajusta el tamaño de la imagen
imagenRotada = imagen.rotate(90)
imagen = ImageTk.PhotoImage(imagenRotada)

destructorHaciaAbajo = Image.open("b1.png")
destructorHaciaAbajo = destructorHaciaAbajo.resize((50, 50))  # Ajusta el tamaño de la imagen
rotar = destructorHaciaAbajo.rotate(180+90)
destructorHaciaAbajo= ImageTk.PhotoImage(rotar)

vacio= Image.open("vacio.png")
vacio = vacio.resize((50, 50))  # Ajusta el tamaño de la imagen
vacio = ImageTk.PhotoImage(vacio)

juego.mainloop()