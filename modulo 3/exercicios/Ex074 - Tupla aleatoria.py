# programa que vai gerar 5 numeros aleatorios e colocar em uma tupla
# mostre a listagem desses numeros e indique o menor e maior valor


from random import randint

aleatorio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Os valores sorteados foram: ', end="")

for n in aleatorio:
    print(f"{n}", end=" ")

print('\nO menor valor dessa lista', sorted(aleatorio)[0])
print('O maior valor dessa lista', sorted(aleatorio)[-1])

#ouuu

print('\nO menor valor dessa lista', min(aleatorio))
print('O maior valor dessa lista', max(aleatorio))
