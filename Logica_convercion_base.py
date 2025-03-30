def Conversion_binario_decimal(binario):

    decimal = 0
    longitud =  len(binario)

    for i in range(longitud):
        bit = binario[i]
        if bit not in('0' , '1'):
            print("Binario no valido")
            return None
        
        decimal += int(bit) * (2 ** (longitud - i - 1))
    return decimal

def Conversion_octal_decimal(octal):

    decimal = 0
    longitud =  len(octal)

    for i in range(longitud):
        digito = octal[i]
        if digito not in ('01234567'):
            print("Octal no valido")
            return

        decimal += int(digito) * (8  (longitud - i - 1))
    return decimal

def Conversion_hexa_decimal(hexa):

    decimal = 0
    longitud = len(hexa)
    tabla_hex = { '0': 0, '1':1, '2': 2, '3':3, '4': 4, '5':5, '6': 6, '7':7, '8': 8, '9':9, 'A': 10, 'B':11, 'C': 12, 'D':13, 'E': 14, 'F': 15}

    hexa = hexa.upper()

    for i in range(longitud):
        digito = hexa[i]
        if digito not in tabla_hex:
            print("Hexa no valido")
            return
        decimal += tabla_hex[digito] * (16  (longitud - i - 1))
    return decimal