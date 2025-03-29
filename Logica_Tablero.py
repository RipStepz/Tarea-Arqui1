import random

def Obtener_Largo_Tablero(): 
    Largo_Pasillo = input("Ingresar Largo del pasillo: ")
    Flag = True

    while(Flag):
        try: 
            Largo_Pasillo = int(Largo_Pasillo)
    
        except:
            Largo_Pasillo = input("El largo del pasillo tiene que ser un numero intero, por favor reintentar: ")
            if type(Largo_Pasillo) == int:
                Largo_Pasillo = int(Largo_Pasillo)
        
        if type(Largo_Pasillo) == int:
             Flag = False

    return Largo_Pasillo

def Generar_Tablero(largo_Pasillo):
    Filas = 11
    columnas = largo_Pasillo
    tablero = [["x" for _ in range(columnas)] for _ in range(Filas)]
    return tablero

def Imprimir_Tablero(Tablero):
    for fila in Tablero:
        print(" ".join(fila))

def Generar_Snake(Tablero):
    Tablero[5][0] = "S"
    return Tablero

def Obtener_Cantidad_Guardias():
    Cantidad_Guardias = input("Ingresar Cantidad de guardias: ")
    Flag = True

    while(Flag):
        try: 
            Cantidad_Guardias = int(Cantidad_Guardias)
    
        except:
            Cantidad_Guardias = input("La cantidad de guardias tiene que ser un numero entero, por favor reintentar: ")
            if type(Cantidad_Guardias) == int:
                Cantidad_Guardias = int(Cantidad_Guardias)
        
        if type(Cantidad_Guardias) == int:
             Flag = False
    return Cantidad_Guardias

def Comprobar_Cantidad_Guardias(Largo_Pasillo, Cantidad_Guardias):
    Flag = True

    Cantidad_De_Casillas = Largo_Pasillo * 11
    Casillas_Usables = Cantidad_De_Casillas - 2
    
    while Flag:
        if Cantidad_Guardias > Casillas_Usables:
            print(f"Hay mas guardias de los posibles, cantidad maxima posible de guardias {Casillas_Usables}\n")
            Cantidad_Guardias = Obtener_Cantidad_Guardias()
        else:
            Flag = False
    return Cantidad_Guardias

def Generar_Guardias(Largo_Pasillo, Cantidad_Guardias, Tablero):
    Cantidad_Guardias = Comprobar_Cantidad_Guardias(Largo_Pasillo, Cantidad_Guardias)
    i = 0
    while i < Cantidad_Guardias:
        x = random.randint(0,Largo_Pasillo - 1)
        y = random.randint(0,10)
        while (Tablero[y][x] == "S" or Tablero[y][x] == "*" or Tablero[y][x] == "!"):
            x = random.randint(0,Largo_Pasillo - 1)
            y = random.randint(0,10)

        Tablero[y][x] = "!"
        i += 1
    
    return Tablero

def Generar_Objetivo(Largo_Pasillo,Tablero):
    Flag = True
    Objetivo = random.randint(0,10)
    while Flag:
        if Tablero[Objetivo][Largo_Pasillo - 1] == "S":
            Objetivo = random.randint(0,10)
        else:
            Tablero[Objetivo][Largo_Pasillo - 1] = "*"
            Flag = False
    
    
    return Tablero
