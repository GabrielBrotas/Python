# programa que leia o nome e peso de varias pessoas guardando tudo em uma lista e no final mostre:
# a) quantas pessoas foram cadastradas, b) Uma listagem com as pessoas mais pesadas, c)uma listagem com as pessoas mais leves

dados = []
pessoas = []

pes = 0
lev = 0
pesado = []
leve = []

while True:
# --------------------- inserir dados --------------------------------------
    dados.append(str(input('Nome: ')).strip().title())
    dados.append((float(input('peso: '))))
    pessoas.append(dados[:])

    if len(pessoas) == 1:
        pes = lev = dados[1]
        pesado.append(dados[:])
        leve.append(dados[:])
    else:
        if dados[1] > pes:
            pesado.clear()
            pesado.append(dados[:])
            pes = dados[1]
        elif dados[1] == pes:
            pesado.append(dados[:])
            pes = dados[1]
        elif dados[1] < lev:
            leve.clear()
            leve.append(dados[:])
            lev = dados[1]
        elif dados[1] == lev:
            leve.append(dados[:])
            lev = dados[1]

    dados.clear()
# ---------------------------- Continuar s ou n ---------------------------
    sn = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while sn not in 'SsNn':
        print('Digite uma opcao valida!')
        sn = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if sn in 'Nn':
        break
# -------------------------------------------------------------------------

print('=-'*20)
print('fim dos cadastros')

print(f'Ao total foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi {pes}. Peso de', end=' ')

for c in pesado:
    print(c[0], end=', ')

print(f'\nO menor peso foi {lev}. Peso de', end=' ')
for n in leve:
    print(n[0], end=', ')



# print(pessoas)
# print(pesado)
# print(leve)
# print(pes)
# print(lev)


