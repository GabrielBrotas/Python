# Programa que leia um numero real qualquer e mostre sua proporcao inteira
from math import trunc

num = float(input('digite um numero: '))

print(trunc(num)) #trunc mostra a parte inteira de um numero, poderia tambem usar o comando floor
print(int(num)) #outra forma simples

# Programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, mostre o cumprimento da hipotenusa

from math import sqrt, hypot

co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))

hp = sqrt((co**2+ca**2)) # ou poderia ser (co ** 2 + ca ** 2) ** (1/2)

hi = hypot(co, ca) #maneira mais simples com o math

print('hipotenusa: {:.3f}'.format(hp))
print('hipotenusa: {:.3f}'.format(hi))


# leia um angulo qualquer e mostre o seu valor do seno,cosseno e tangente

from math import cos, sin, tan, radians

ang = float(input('\nangulo: '))

seno = sin(radians(ang))  #Transforma o angulo em radianos e faz o seno dele
cose = cos(radians(ang))
tang = tan(radians(ang))

print('seno : {:.3f} \ncosseno: {:.3f}  \ntangente: {:.3f}'.format(seno, cose, tang))

