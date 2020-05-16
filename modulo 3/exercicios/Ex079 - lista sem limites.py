# Programa em q o usuario possa adicionar valores numericos em uma lista, Caso o numero ja exista ele nao sera adicionado
# no final serao exibidos todos os valores unicos em ordem crescente


lista = []
resp = ''
old = 0
while True:
    old = int(input('Digite um valor: '))

    if old in lista:
        print('Valor repetido, nao vou adicionar...')
    else:
        lista.append(old)
        print('Valor adicionado com sucesso...')

    resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
    while resp not in 'SsNn':
        print('Digite uma opcao valida!')
        resp = input('Deseja continuar? [S/N] ').strip().upper()[0]

    if resp in 'Nn':
        break

print('-='*20)
print(f'Voce digitou os valores {sorted(lista)}')
