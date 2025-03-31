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
    longitud = len(octal)

    for i in range(longitud):
        digito = octal[i]
        
        if digito not in '01234567':  
            print("Octal no válido")
            return None 
        
        decimal += int(digito) * (8 ** (longitud - i - 1))  

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
        decimal += tabla_hex[digito] * (16 ** (longitud - i - 1))
    return decimal
## Para Hackeo##

def Conversion_decimal_binario(decimal):
    if decimal == 0:
        return "0"

    binario = ""
    while decimal > 0:
        resto = decimal % 2
        binario = str(resto) + binario
        decimal //= 2

    return binario

def Conversion_decimal_octal(decimal):
    if decimal == 0:
        return "0"

    octal = ""
    while decimal > 0:
        resto = decimal % 8
        octal = str(resto) + octal
        decimal //= 8

    return octal

def Conversion_decimal_hexa(decimal):
    if decimal == 0:
        return "0"
    tabla = "0123456789ABCDEF"
    hexa = ""
    while decimal > 0:
        resto = decimal % 16
        hexa = tabla[resto] + hexa
        decimal //= 16

    return hexa