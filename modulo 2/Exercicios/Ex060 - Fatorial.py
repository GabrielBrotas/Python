
n = int(input('Numero para verificar fatorial: '))

print('Voce escolheu: ')

soma = 0
num = n

while num != 0:
    num = num - 1
    fact = n * num
    soma += fact
    print('{} * {} = {}'.format(n, num, fact), end=' ->-> ')


print('\nO fatorial de {} vale: {}'.format(n, soma))