# com a matriz feita no ex086 motre
# a) a soma de todos os valores pares digitados, b) a soma dos valores da terceira coluna, c) O maior valor da segunda linha

lista = [[0, 0], [0, 1], [0, 2],
         [1, 0], [1, 1], [1, 2],
         [2, 0], [2, 1], [2, 2]]
endereco = 0
num = 0
pares = 0

for n, v in lista:

    num = int(input(f'Digite um valor para [{n},{v}]: '))
    if num % 2 == 0:
        pares += num
    lista[endereco] = num
    endereco += 1

print('-='*20)
print(f'''[ {lista[0]} ] [ {lista[1]} ] [ {lista[2]} ]
[ {lista[3]} ] [ {lista[4]} ] [ {lista[5]} ]
[ {lista[6]} ] [ {lista[7]} ] [ {lista[8]} ]
''')
print('-='*20)
print(f'A soma dos valores pares : {pares}')

terc = lista[6] + lista[7] + lista[8]
print(f'a soma dos valores da terceira coluna: {terc}')

maior = max(lista[3:6])
print(f'o maior valor da segunda coluna: {maior}')
