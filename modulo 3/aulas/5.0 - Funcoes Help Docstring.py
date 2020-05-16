# help(print)  # help mostra a docstring, o manual da funcao


def contador(i, f, p):  # entre as 3 aspas duplas vai colocar a docstring(manual) da funcao
    """
    -> Faz uma contagem e mostra na tela.
    i = inicio da contagem
    f = final
    p = passo
    return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('Fim')


contador(0, 100, 10)
help(contador)
