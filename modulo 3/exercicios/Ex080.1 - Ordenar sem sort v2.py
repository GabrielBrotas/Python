lista = []

for c in range(0, 5):
    n = int(input('Digite um valor: '))

    if c == 0 or n > lista[-1]:  # so for a primeira posicao ou o numero for maior que o ultimo entao
        lista.append(n)          # apenas adicionar o valor
        print('Adicionado na ultima posicao da lista...')
    else:
        pos = 0     # analisar a posicao
        while pos < len(lista):  #percorrer a lista
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posicao {pos} da lista... ')
                break
            pos += 1
print('-='*20)
print(f'Os valores da lista de forma ordenada: {lista}')
