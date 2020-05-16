# Leia o comprimento de 3 retas e diga se pode formar um triangulo ou nao
# Condicoes matematicas, se a o cumprimento de uma reta for maior q a soma do comprimento das outras 2 nao pode

d1 = float(input('digite o d1: '))
d2 = float(input('digite o d2: '))
d3 = float(input('digite o d3: '))

if d1 < d2 + d3 and d2 < d1 + d3 and d3 < d1 + d2:
    print('podem formar um triangulo')
else:
    print('nao podem formar')