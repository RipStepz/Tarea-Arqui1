import Logica_Tablero

Largo_Pasillo = Logica_Tablero.Obtener_Largo_Tablero()
Tablero = Logica_Tablero.Generar_Tablero(Largo_Pasillo)
Tablero = Logica_Tablero.Generar_Snake(Tablero)
Logica_Tablero.Imprimir_Tablero(Tablero)