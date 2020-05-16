# Fazer a tabuada de um valor escolhido pelo usario e so parar quando o valor escolhido for negativo
from time import sleep

num = int(input('Deseja ver a tabuada de qual valor? '))
m = 0

while True:
    if num < 0:
        break

    print('-=' * 20)

    for c in range(0, 11):
        m = num * c

        print(f'{num} x {c} = {m}')

    print('-=' * 20)

    num = int(input('Deseja ver a tabuada de qual valor? '))

print('Fim da tabela')
