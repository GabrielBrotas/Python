# funcao contador() que receba tres parametros: inicio, fim e passo e realize a contagem.
# a) de 1 ate 10 de 1 em 1
# b) de 10 ate 0, de 2 em 2
# C) uma contagem personalizada

from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('=-'*20)
    print(f'Contagem de {i} ate {f} de {p} em {p}')

    # caso o inicio seja maior do que o fim ------------------
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += p
        print('FIM')
    # ---------------------------------------------------------
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= p
        print('Fim')


# PROGRAMA PRINCIPAL
contador(0, 100, 10)
contador(10, 0, 2)
print('Agora e a sua vez.')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)



