import Logica_Tablero, Logica_movimiento, Logica_convercion_base

Posicion_S = [5,0]
Largo_Pasillo = Logica_Tablero.Obtener_Largo_Tablero()
Cantidad_Guardias = Logica_Tablero.Obtener_Cantidad_Guardias()
Caso_de_movimiento = 0

Tablero = Logica_Tablero.Generar_Tablero(Largo_Pasillo)
Tablero = Logica_Tablero.Generar_Snake(Tablero)
Tablero = Logica_Tablero.Generar_Objetivo(Largo_Pasillo,Tablero)
Tablero = Logica_Tablero.Generar_Guardias(Largo_Pasillo, Cantidad_Guardias, Tablero)

Logica_Tablero.Imprimir_Tablero(Tablero)

Flag = True

while Flag:
    
    Direccion = Logica_movimiento.Pedir_Accion_Direccion()
    if Direccion == "-1":
        print("Juego terminado por decision del jugador")
        break
    Binario = Logica_movimiento.Pedir_Accion_Base(Largo_Pasillo)
    Lista_Tablero_S_C = Logica_movimiento.Mover_En_binario(Binario, Tablero, Posicion_S, Direccion, Largo_Pasillo)

    Tablero = Lista_Tablero_S_C[0]
    Posicion_S = Lista_Tablero_S_C[1]
    Caso_de_movimiento = Lista_Tablero_S_C[2]
    
    if Caso_de_movimiento == 1: ## !
        print("Has sido atrapado por los guardias")
        Flag = False

    elif Caso_de_movimiento == 2: ## *
        print("\nLograste llegar a tu objetivo, se iniciara la etapa final")
        Numero_Secreto = Logica_movimiento.hackeo_Numero_en_base_X(Largo_Pasillo)

        if 0 < Largo_Pasillo and Largo_Pasillo <= 20 :
            Respuesta = input(f"El numero binario que tienes que transformar a decimal es {Numero_Secreto[1]} :")

        elif 20 < Largo_Pasillo and Largo_Pasillo <= 100:
            Respuesta = input(f"El numero octal que tienes que transformar a decimal es {Numero_Secreto[1]}: ")

        elif Largo_Pasillo > 100:
            Respuesta = input(f"El numero de hexadecimal que tienes que transformar a decimal es {Numero_Secreto[1]} :")

        if Numero_Secreto[0] == int(Respuesta):
            print("felicidades ganaste el juego")
            
        else:
            print("Perdiste")
        
        Flag = False 
    else: ## X el juego continua
        Logica_Tablero.Imprimir_Tablero(Tablero)
