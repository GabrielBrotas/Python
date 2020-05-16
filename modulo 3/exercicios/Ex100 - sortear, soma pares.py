# Um programa que tenha uma lista chamada numeros e duas funcoes chamadas sorteia() e somaPar(). A primeira funcao vai sortear 5 numeros
# e vai coloca los dentro da lista e a segunda funcao vai mostrar a soma entre todos os valores pares sorteados pela funcao anterior

from random import randint
from time import sleep

numeros = []


def sorteia(lst):  # sortear 5 numeros e colocar dentro da lista
    print('Sorteando 5 valores para a lista...', end=' ')
    sleep(0.5)
    for c in range(0, 5):
        num = randint(0, 10)
        print(num, end=' ')
        lst.append(num)
        sleep(0.5)
    print('PRONTO!')


def somaPar(lst):
    print(f'Somando os valores pares de {lst}, temos ', end='')
    s = 0
    for c in lst:
        if c % 2 == 0:
            s += c
    print(s)


sorteia(numeros)
somaPar(numeros)

