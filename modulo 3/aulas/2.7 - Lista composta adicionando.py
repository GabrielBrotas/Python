galera = []
dados = []

for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade:')))
    galera.append(dados[:])
    dados.clear()
print(galera)
print(dados)

# lista com maiores de idade

for p in galera:
    if p[1] > 18:
        print(f'{p[0]} e maior de idade...')
