# Programa que leia sete valores numericos e cadastre os em uma lista unica que mantenha separados os valores pares e impares
# mostre os valores pares e impares de forma crescente

lista = [[], []]
num = 0

for n in range(0, 7):
    num = int(input(f'Digite o {n+1} valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

print(f'Os valores pares digitados foram: {sorted(lista[0])}')
print(f'Os valores impares digitados foram: {sorted(lista[1])}')



