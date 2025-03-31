import Logica_convercion_base, re

def es_binario(cadena):
    patron = r"^[01]+$"  
    return bool(re.fullmatch(patron, cadena))

def es_octal(cadena):
    patron = r"^[0-7]+$"  
    return bool(re.fullmatch(patron, cadena))

def es_hexa(cadena):
    patron = r"^[0-9A-Fa-f]+$"  
    return bool(re.fullmatch(patron, cadena))

def Pedir_Accion_Base(Largo_Pasillo): ## retorna el movimiento que se quiere hacer en la base correspondiente
    Movimiento = ""
    Flag = True

    if 0 < Largo_Pasillo and Largo_Pasillo <= 20:
        Movimiento = input("Escribe la cantidad de pasos que quieres moverte en formato Binario: ")
        while Flag:
            if es_binario(Movimiento):
                return Movimiento
            else:
                Movimiento = input("Escriba un numero binario, intente nuevamente:")

    elif 20 < Largo_Pasillo and Largo_Pasillo <= 100:
        Movimiento = input("Escribe la cantidad de pasos que quieres moverte en formato Octal: ")
        while Flag:
            if es_octal(Movimiento):
                return Movimiento
            else:
                Movimiento = input("Escriba un numero Octal, intente nuevamente:")

    elif Largo_Pasillo > 100:
        Movimiento = input("Escribe la cantidad de pasos que quieres moverte en formato Hexadecimal: ")
        while Flag:
            if es_hexa(Movimiento):
                return Movimiento
            else:
                Movimiento = input("Escriba un numero Hexadecimal, intente nuevamente:")

def Pedir_Accion_Direccion():
    Flag = True
    accion = ""
    direccion = {'w': 0 ,'a': 1,'s': 2,'d' : 3 }

    while Flag:
        print("Ingresa una Accion!\nw: moverse hacia arriba\na: moverse hacia izquierda\ns:moverse hacia la abajo\nd:moverse a la derecha\n-1: salir")
        accion = input("")

        if accion != "w" and accion != "a" and accion != "s" and accion != "d" and accion != "-1":
            print("---------------------------------------")
            print("input incorrecto, reintetar")
            print("Ingresa una Accion!\nw: moverse hacia arriba\ns: moverse hacia abajo\na:moverse hacia la izquierda\nd:moverse a la derecha\n-1: salir")
            accion = input("")
        else:
            Flag = False

    if accion == "-1":
        return "-1"
    
    return direccion[accion]

def Comprobacion_inputs(Base, Posicion_S , Largo_Pasillo, direccion):
    if 0 < Largo_Pasillo and Largo_Pasillo <= 20 :
        Movimiento_decimal = Logica_convercion_base.Conversion_binario_decimal(Base)
    
    elif 20 < Largo_Pasillo and Largo_Pasillo <= 100:
        Movimiento_decimal = Logica_convercion_base.Conversion_octal_decimal(Base)

    elif Largo_Pasillo > 100:
        Movimiento_decimal = Logica_convercion_base.Conversion_hexa_decimal(Base)


    Flag = True

    if direccion == "-1":
        return "-1"
    
    while Flag:
        if direccion == 0 : ## arriba    
            if Posicion_S[0] -  Movimiento_decimal < 0:
                print("Movimiento fuera de los limites en direccion w, porfavor, reintentar")
                Base = Pedir_Accion_Base(Largo_Pasillo)
                if 0 < Largo_Pasillo and Largo_Pasillo <= 20:
                    Movimiento_decimal = Logica_convercion_base.Conversion_binario_decimal(Base)
                elif 20 < Largo_Pasillo and Largo_Pasillo <= 100:
                    Movimiento_decimal = Logica_convercion_base.Conversion_octal_decimal(Base)
                elif Largo_Pasillo > 100:
                    Movimiento_decimal = Logica_convercion_base.Conversion_hexa_decimal(Base)
            else:
                Flag = False
                return Movimiento_decimal
        
        elif direccion == 2 : ## abajo
            if Posicion_S[0] +  Movimiento_decimal > 10:
                print("Movimiento fuera de los limites en direccion s, porfavor, reintentar")
                Base = Pedir_Accion_Base(Largo_Pasillo)
                if 0 < Largo_Pasillo and Largo_Pasillo <= 20:
                    Movimiento_decimal = Logica_convercion_base.Conversion_binario_decimal(Base)
                elif 20 < Largo_Pasillo and Largo_Pasillo <= 100:
                    Movimiento_decimal = Logica_convercion_base.Conversion_octal_decimal(Base)
                elif Largo_Pasillo > 100:
                    Movimiento_decimal = Logica_convercion_base.Conversion_hexa_decimal(Base)
                    
            else:
                Flag = False
                return Movimiento_decimal
        
        elif direccion == 1 : ## izquierda
            if Posicion_S[1] -  Movimiento_decimal < 0:
                print("Movimiento fuera de los limites en direccion a, porfavor, reintentar")
                Base = Pedir_Accion_Base(Largo_Pasillo)
                if 0 < Largo_Pasillo and Largo_Pasillo <= 20:
                    Movimiento_decimal = Logica_convercion_base.Conversion_binario_decimal(Base)
                elif 20 < Largo_Pasillo and Largo_Pasillo <= 100:
                    Movimiento_decimal = Logica_convercion_base.Conversion_octal_decimal(Base)
                elif Largo_Pasillo > 100:
                    Movimiento_decimal = Logica_convercion_base.Conversion_hexa_decimal(Base)
            else:
                Flag = False
                return Movimiento_decimal
            
        elif direccion == 3 : ## derecha
            if Posicion_S[1] +  Movimiento_decimal > Largo_Pasillo - 1:
                print("Movimiento fuera de los limites en direccion d, porfavor, reintentar")
                Base = Pedir_Accion_Base(Largo_Pasillo)
                if 0 < Largo_Pasillo and Largo_Pasillo <= 20:
                    Movimiento_decimal = Logica_convercion_base.Conversion_binario_decimal(Base)
                elif 20 < Largo_Pasillo and Largo_Pasillo <= 100:
                    Movimiento_decimal = Logica_convercion_base.Conversion_octal_decimal(Base)
                elif Largo_Pasillo > 100:
                    Movimiento_decimal = Logica_convercion_base.Conversion_hexa_decimal(Base)
            else:
                Flag = False
                return Movimiento_decimal

def Mover_En_binario(Binario, Tablero, Posicion_S, Direccion, Largo_Pasillo):
    Movimiento_decimal = Comprobacion_inputs(Binario, Posicion_S , Largo_Pasillo, Direccion)
    Retorno = [] ## primera posicion tablero, segunda posicion "S"
    
    x = Posicion_S[1]
    y = Posicion_S[0]
    Caso_de_movimiento = 0 ## si es 0 significa que cayo en "X", si es 1 cayo en "!", si es 2 cayo en "*"

    if Direccion == 0: ## arriba
        
        if Tablero[y - Movimiento_decimal][x] == "!":
            Caso_de_movimiento = 1
        
        elif Tablero[y - Movimiento_decimal][x] == "*":
            Caso_de_movimiento = 2
        else:
            Tablero[y][x] = "x"
            Tablero[y - Movimiento_decimal][x] = "S"
            Caso_de_movimiento = 0

        Retorno.append(Tablero)
        Retorno.append([y - Movimiento_decimal , x])
        Retorno.append(Caso_de_movimiento)
        
        return Retorno
    
    elif Direccion == 2: ## abajo
        if Tablero[y + Movimiento_decimal][x] == "!":
            Caso_de_movimiento = 1
        
        elif Tablero[y + Movimiento_decimal][x] == "*":
            Caso_de_movimiento = 2
        else:
            Tablero[y][x] = "x"
            Tablero[y + Movimiento_decimal][x] = "S"
            Caso_de_movimiento = 0

        Retorno.append(Tablero)
        Retorno.append([y + Movimiento_decimal , x])
        Retorno.append(Caso_de_movimiento)
        
        return Retorno
    
    elif Direccion == 1: ## izquierda
        if Tablero[y][x - Movimiento_decimal] == "!":
            Caso_de_movimiento = 1
        
        elif Tablero[y][x - Movimiento_decimal] == "*":
            Caso_de_movimiento = 2
        else:
            Tablero[y][x] = "x"
            Tablero[y][x - Movimiento_decimal] = "S"
            Caso_de_movimiento = 0

        Retorno.append(Tablero)
        Retorno.append([y, x - Movimiento_decimal])
        Retorno.append(Caso_de_movimiento)

        return Retorno
    
    elif Direccion == 3: ## derecha
        if Tablero[y][x + Movimiento_decimal] == "!":
            Caso_de_movimiento = 1
        
        elif Tablero[y][x + Movimiento_decimal] == "*":
            Caso_de_movimiento = 2
        else:
            Tablero[y][x] = "x"
            Tablero[y][x + Movimiento_decimal] = "S"
            Caso_de_movimiento = 0

        Retorno.append(Tablero)
        Retorno.append([y, x + Movimiento_decimal])
        Retorno.append(Caso_de_movimiento)
        
        return Retorno