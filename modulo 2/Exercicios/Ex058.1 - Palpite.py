from random import randint

computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10')
print('Tente adivinhar qual foi')

acertou = False
palpite = 0

while not acertou:
    jogador = int(input('Digite um numero entre 0 e 10: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Menos...')
        elif jogador < computador:
            print('Mais')
print('Acertou com {} tentativas. Parabens'.format(palpite))
