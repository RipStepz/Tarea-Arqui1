import Logica_Tablero, Logica_movimiento

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
    Binario = Logica_movimiento.Pedir_Accion_Base(Largo_Pasillo)
    Lista_Tablero_S_C = Logica_movimiento.Mover_En_binario(Binario, Tablero, Posicion_S, Direccion, Largo_Pasillo)

    Tablero = Lista_Tablero_S_C[0]
    Posicion_S = Lista_Tablero_S_C[1]
    Caso_de_movimiento = Lista_Tablero_S_C[2]
    
    if Caso_de_movimiento == 1: ## !
        print("Has sido atrapado por los guardias")
        Flag = False

    elif Caso_de_movimiento == 2: ## *
        print("Lograste llegar a tu objetivo, se iniciara la etapa final")
        Flag = False ## por mientras
    
    else: ## X el juego continua
        Logica_Tablero.Imprimir_Tablero(Tablero)
