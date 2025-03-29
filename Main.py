import Logica_Tablero

Largo_Pasillo = Logica_Tablero.Obtener_Largo_Tablero()
Cantidad_Guardias = Logica_Tablero.Obtener_Cantidad_Guardias()

Tablero = Logica_Tablero.Generar_Tablero(Largo_Pasillo)
Tablero = Logica_Tablero.Generar_Snake(Tablero)
Tablero = Logica_Tablero.Generar_Objetivo(Largo_Pasillo,Tablero)
Tablero = Logica_Tablero.Generar_Guardias(Largo_Pasillo, Cantidad_Guardias, Tablero)

Logica_Tablero.Imprimir_Tablero(Tablero)