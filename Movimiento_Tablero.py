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

binario = "1101"
decimal = Conversion_binario_decimal(binario)
print(decimal)