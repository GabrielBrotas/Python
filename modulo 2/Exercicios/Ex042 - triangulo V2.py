r1 = float(input('digite o valor de um lado do triangulo: '))
r2 = float(input('digite o valor de outro lado do triangulo: '))
r3 = float(input('digite o valor de outro lado do triangulo: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triangulo do tipo', end=' ')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 != r3:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('nao se pode formar um trinagulo pois um lado é maior q a soma de dois')