# programa que tenha uma funcao fatorial() que receba dois parametros: o primeiro que indique o numero a calcular e o outro chamado show
# que sera um valor logico(opcional) indicando se sera mostrado ou nao na tela o processo de calculo do fatorial


def fatorial(num=1, show = False):
    f = 1
    print('-'*20)

    if show:
        for c in range(num, 0, -1):
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
            f *= c
    else:
        for c in range(num, 1, -1):
            f *= c
    return f


# Programa princial
print(fatorial(4, show=True))
