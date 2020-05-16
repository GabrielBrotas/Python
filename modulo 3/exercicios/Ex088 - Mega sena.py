# Programa que ajude um jogador na mega sena. o programa vai perguntar quantos jogos serao gerados e vai sortear 6 numeros entre 1 a 60
# para cada jogo, cadastrando tudo em uma lista composta

from random import randint
from time import sleep

print('-='*20)
print(f'{"MEGA SENA":^40}')
print('-='*20)

lista = []
num = 0

jogos = int(input('Quantos jogos serao gerados? '))

for n in range(0, jogos):
    while len(lista) < 6:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)

    print(f'jogo {n+1}: {sorted(lista)}')
    sleep(1)
    lista.clear()


