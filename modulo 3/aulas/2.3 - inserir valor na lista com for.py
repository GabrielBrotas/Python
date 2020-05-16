valores = list()

for cont in range(0, 5):
    valores.append(int(input('digite um valor: ')))
print(valores)

for c, v in enumerate(valores):
    print(f'na posicao {c} encontrei o valor {v} ')


