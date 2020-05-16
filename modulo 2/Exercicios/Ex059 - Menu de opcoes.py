# prpgrama que leia 2 valores e mostre um menu na tela
#  1 somar, 2 multiplicar, 3 maior, 4 menor e 5 sair

n1 = int(input('valor 1: '))
n2 = int(input('valor 2: '))

c = 0
s = 0

print('''numero 1 = {} e numero 2 = {}. Qual operacao realizar?'
      [1] soma
      [2] multiplicacao
      [3] maior
      [4] menor
      [5] sair'''.format(n1, n2))

while c != 5:

    c = int(input('Digite a operacao: '))

    if c == 1:
        s = n1 + n2
        print('A soma de n1 e n2: ', s)

    elif c == 2:
        m = n1 * n2
        print('A multiplicacao de n1 e n2: ', m)

    elif c == 3:
        if n1 > n2:
            print('O maior numero: ', n1)
        elif n2 > n1:
            print('O maior numero: ', n2)
        else:
            print('Os numeros sao iguais')

    elif c == 4:
        if n1 < n2:
            print('O menor numero: ', n1)
        elif n2 < n1:
            print('O menor numero: ', n2)
        else:
            print('Os numeros sao iguais')
    elif c == 5:
        print('EXIT')
    else:
        print('Digite uma opcao valida')
