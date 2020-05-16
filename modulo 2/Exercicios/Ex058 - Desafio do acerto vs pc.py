# computador pensar em um numero de 0 a 10 e o jogador vai chutar palpite ate acertar
# mostrar o numero de tentativas necessarias para vencer

print('=-'*20)
print('\nBem vindo ao jogo do acerto')
print('\n{}{}Computador{} vs {}Player{}{}'.format('-='*5, '\033[31m', '\033[m', '\033[33m', '\033[m', '=-'*5))

from random import randint

pc = 0
player = 1
c = 0

while pc != player:

    pc = randint(0,10)
    player = int(input('digite um numero de 0 a 10: '))
    print('o Pc jogou {} e voce {}. Tente novamente'.format(pc, player))
    c += 1
print('PARABENS, VOCE ACERTOU NA TENTATIVA {}!!!'.format(c))

