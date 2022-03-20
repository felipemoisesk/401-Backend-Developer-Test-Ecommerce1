maxDigit = input('Digite um número de 1 a 9: ')

d1 = f'{maxDigit}'
d2 = f'{maxDigit}'
d3 = f'{maxDigit}'
d4 = f'{maxDigit}'

numax = int(d1 + d2 + d3 + d4)

#print(type(numax))
print(numax)
#print(list(str(numax)))
listanumeros = []
numeros = []
for numero in range(1000, numax+1, 1):
    algarismos = list(str(numero))
    somanumero = int(algarismos[0]) + int(algarismos[1]) + int(algarismos[2]) + int(algarismos[3])
    if somanumero == 21:
        if int(algarismos[0]) <= int(maxDigit) and int(algarismos[1]) <= int(maxDigit) and int(algarismos[2]) <= int(maxDigit) and int(algarismos[3]) <= int(maxDigit):
#            listanumeros.append(algarismos)
            numeros.append(numero)
        else:
            pass
#print (listanumeros)
print (numeros)
print (len(numeros))