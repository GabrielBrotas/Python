# Programa que crie uma matriz de dimensao 3x3 e preencha com os valores lidos pelo teclado
# mostre a matriz na tela com a formatacao correta

lista = [[0, 0], [0, 1], [0, 2],
         [1, 0], [1, 1], [1, 2],
         [2, 0], [2, 1], [2, 2]]
print(lista)

endereco = 0
num = 0

for n, v in lista:

    num = int(input(f'Digite um valor para [{n},{v}]: '))
    lista[endereco] = num
    endereco += 1

print('-='*20)

print(f'''[ {lista[0]} ] [ {lista[1]} ] [ {lista[2]} ]
[ {lista[3]} ] [ {lista[4]} ] [ {lista[5]} ]
[ {lista[6]} ] [ {lista[7]} ] [ {lista[8]} ]
''')
print('-='*20)
