# faca o computador pensar em um numero entre 0 e 5 e o usuario tem que tentar advinhar qual o numero escolhido
# mostre na tela se acertou ou nao

import random

num = random.randint(0, 5)
num2 = int(input('Digite um numero de 0 a 5: '))

print(num, num2)

if num == num2:
    print('\nParabens, Voce acertou!!')
else:
    print('\ntente novamente.')

print('\nend game')

