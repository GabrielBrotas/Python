valor = [4, 3, 8, 6, 2, 8, 6, 9]

print(valor)
if 8 in valor:
    valor.remove(8)  # Ele vai remover o primeiro valor 8 contando da esquerda para direita e os restantes vao manter
print(valor)

valores = []
valores.append(8)
valores.append(5)
valores.append(4)
print(valores)

for n in valores:
    print(f'{n}...', end=' ')

for c, v in enumerate(valores):  # enumarate valores vai pegar o endereco 1 , 2 , 3

    print(f'\nNa posicao {c} encontrei o valor {v}')  # c vai pegar o endereco e v o que tem dentro do endereco

print('fim')
