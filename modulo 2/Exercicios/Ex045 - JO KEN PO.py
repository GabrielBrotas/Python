from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)

print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] tesoura''')

jogada = int(input('Qual sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print('-=' * 20)

if pc == 0:
    if jogada == 0:
        print('EMPATE')
    elif jogada == 1:
        print('Voce Ganhou!!!')
    elif jogada == 2:
        print('O Computador Ganhou!!!')
    else:
        print('jogada invalida')
elif pc == 1:
    if jogada == 0:
        print('O Computador Ganhou!!!')
    elif jogada == 1:
        print('EMPATE')
    elif jogada == 2:
        print('Voce Ganhou!!!')
    else:
        print('jogada invalida')
elif pc == 2:
    if jogada == 0:
        print('Voce Ganhou!!!')
    elif jogada == 1:
        print('O Computador Ganhou!!!')
    elif jogada == 2:
        print('EMPATE')
    else:
        print('jogada invalida')

print('-='*20)

