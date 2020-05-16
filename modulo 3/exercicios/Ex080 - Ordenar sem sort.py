# Programa onde o usuario digite 5 valores numerios e cadastre os em uma lista ja na posicao correta
# sem usar o sort mostre a lista de forma ordenada

lista = []
mai = 0
men = 0
num = 0

for c in range(0, 5):
    num = int(input('Digite um numero: '))

    if c == 0:
        lista.append(num)
        print(f'Valor {num} adicionado na posicao 0 da lista...')
        mai = men = num
    elif num > mai:
        lista.insert(lista.index(mai)+1, num)
        mai = num
        print(f'valor {num} adicionado na posicao {lista.index(mai)+1}')
    elif num < men:
        lista.insert(0, num)
        print(f'Valor {num} adicionado na posicao 0 da lista')
    else:
        for v, b in enumerate(lista):
            if num <= b:
                lista.insert(v, num)
                print(f'Valor {num} adicionado na pos {v+1}')
                break
print(lista)








