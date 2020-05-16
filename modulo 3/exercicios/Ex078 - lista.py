# leia 5 valores numericos e guarde os em uma lista
# mostre qual o maior e menor valor e suas posicoes

lista = []
men = 0
mai = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor na pos {c}: ')))

    if c == 0:
        mai = men = lista[c]
    else:
        if lista[c] > mai:
            mai = lista[c]
        if lista[c] < men:
            men = lista[c]

print('-='*20)
print('Voce digitou os valores:', lista)

print(f'O maior valor foi {mai} e esta nas posicoes ', end=' ')
for i, v in enumerate(lista):
    if v == mai:
        print(f'{i+1}...', end=' ')
print(f'\nO menor valor foi {men} e esta nas posicoes ', end=' ')
for o, b in enumerate(lista):
    if b == men:
        print(f'{o}...', end=' ')



