# Par ou impar com o computador. O jogo so sera interrompido quando o jogador perder
# mostre o total de vitorias consecutivas que ele conquistou no final do jogo

from random import randint

vitorias = 0

while True:
    # --------------------- escolha de par ou impar--------------------
    escolha = str(input('Voce escolhe par ou impar? ')).strip().upper()[0]
    while escolha not in 'IiPp':
        print('digite uma opcao valida!')
        escolha = str(input('Voce escolhe par ou impar? ')).strip().upper()[0]

     # --------------- jogada do computador e usuario -------------------
    pc = randint(0, 10)

    jogador = input('Digite sua jogada: ')
    while jogador.isnumeric() == False:
        print('digite uma valor valido!')
        jogador = input('Digite sua jogada: ')

    jogada = int(jogador)

    #------------------ condicoes --------------------------------

    if escolha in 'Pp' and ((jogada+pc)%2) == 0:
        print('Voce Ganhou!')
        vitorias += 1
    elif escolha in 'Ii' and ((jogada+pc)%2) != 0:
        print('Voce Ganhou!')
        vitorias += 1
    else:
        print('Voce Perdeu')
        break
print(f'Voce teve uma sequencia de {vitorias} vitorias')




