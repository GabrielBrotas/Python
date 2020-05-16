def contador(* num):  # O asterisco no contador significa que pode receber diversos valores e vai colocar dentro de uma tupla
    for valor in num:
        print(f' {valor} ', end='')

    print(f'Recebi os valores {num} e sao ao todo {len(num)}')
    print('Fim')


contador(2, 1, 7)
contador(4, 0, 4, 6, 9, 8)


def soma(* valores):
    s = 0
    for n in valores:
        s+= n
    print(f'somando os valores{valores} tems {s}')


soma(1, 2, 3)
soma(4, 5, 6, 7)
