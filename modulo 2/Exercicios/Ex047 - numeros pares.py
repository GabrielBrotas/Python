# numeros pares de 1 a 50

inicio = int(input('De: '))
fim = int(input('ate: '))

if inicio < fim:

    if (inicio % 2) == 0 and (fim % 2) == 0:  # se o primeiro e ultimo for numeros pares, ex 2 ate 10
        fim = fim + 1                         # como o ultimo (10) ele nao conta, acrescenta 1 para contar
        for c in range(inicio, fim, 2):       # pulando de 2 em 2
            print(c, end=' ')  # end = ' ' para deixar na linha

    elif (inicio % 2) == 0 and (fim % 2) != 0:  # se o inicio for par e o fim impar conta normalmente, ex 2 ate 11
        for c in range(inicio, fim, 2):
            print(c, end=' ')

    elif (inicio % 2) != 0 and (fim % 2) == 0:  # se o inicio for impar e o fim par, ex 1 ate 10
        inicio = inicio + 1                     # vai ficar de 2 ate 11
        fim = fim + 1
        for c in range(inicio, fim, 2):
            print(c, end=' ')

    elif (inicio % 2) != 0 and (fim % 2) != 0:  # se o inicio e o fim forem impar, ex 1 ate 11
        inicio = inicio + 1                     # vai ficar de 2 ate 11
        for c in range(inicio, fim, 2):
            print(c, end=' ')

else: # caso o fim seja maior q o inicio
    print('Numero inicial maior que final, INVALIDO!')

