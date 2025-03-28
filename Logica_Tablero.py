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
    ##print(f"El largo del tablero seleccionado es: {Largo_Pasillo}")

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

    print(f"La cantidad de guardias seleccionados son: {Cantidad_Guardias}")