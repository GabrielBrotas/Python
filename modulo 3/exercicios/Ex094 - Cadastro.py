# programa que leia nome, sexo e idade de varias pessoas, guardando os dados de cada um em um dicionario e todos os dicionarios em uma lista
# mostre: a) Quantas pessoas foram cadastradas b) A media de idade do grupo c) uma lista com todas as mulheres
# d) uma lista com todas as pessoas com idade acima da media

pessoas = {}
lista = []

while True:
    pessoas['nome'] = str(input('Nome: ')).title().strip()
    pessoas['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while pessoas['sexo'] not in 'MmFf':
        pessoas['sexo'] = str(input('Digite uma opcao valida [M/F] ')).upper().strip()[0]

    pessoas['idade'] = int(input('idade: '))
    lista.append(pessoas.copy())


# -------------------------------------------------------------------------------
    sn = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while sn not in 'SsNn':
        sn = str(input('Digite um valor valido [S/N]: ')).strip().upper()[0]
    if sn in 'Nn':
        break
# -------------------------------------------------------------------------------
print('=-'*20)
print(f'O grupo tem {len(lista)} pessoas')

media = 0
for n, v in enumerate(lista):
    media += lista[n]['idade']
print(f'A media de idade deste grupo: {media/len(lista)}')

mulheres = []
for n, v in enumerate(lista):
    if lista[n]['sexo'] in 'Ff':
        mulheres.append(lista[n]['nome'])

print(f'As mulheres cadastradas: ', end='')
for n in mulheres:
    print(f'{n} ', end=', ')
print()
print('Lista de pessoas acima da media: ')
for n, v in enumerate(lista):
    if lista[n]['idade'] > media/len(lista):
        print(f'nome = {lista[n]["nome"]}; sexo = {lista[n]["sexo"]}; idade = {lista[n]["idade"]}')








