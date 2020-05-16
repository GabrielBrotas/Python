# Programa que leia varios numeros inteiros e so pare quando digitar 999
# mostre quantos numeros foram digitados e a soma entre eles desconsiderando o flag

c = 0
soma = 0

while True:

    num = int(input('Digite um numero: ' ))
    if num == 999:
        break
    c += 1
    soma += num

print(f'Voce digitou {c} numeros e a soma entre eles e {soma}')