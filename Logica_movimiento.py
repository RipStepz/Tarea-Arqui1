import Logica_convercion_base

def Pedir_Accion():
    
    Flag = True
    
    while Flag:
        print("Ingresa una Accion!\nw: moverse hacia arriba\ns: moverse hacia abajo\na:moverse hacia la izquierda\nd:moverse a la derecha\n-1: salir")
        accion = input("")
    
    
    while Flag:
        if accion != "w" or accion != "s" or accion != "a" or accion != "d" or accion != "-1":
            print("Input equivocado, por favor, ingreg")

def Comprobacion_inputs(Binario, Posicion_S , Largo_Pasillo , direccion):
    Movimiento_decimal = Logica_convercion_base.Conversion_binario_decimal(Binario)

def Mover_En_binario(Binario, tablero, Posicion_S , ):
    Movimiento_decimal = Logica_convercion_base.Conversion_binario_decimal(Binario)
    Retorno = [] ## primera posicion tablero, segunda posicion "S"

Pedir_Accion()