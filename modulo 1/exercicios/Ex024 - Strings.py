#programa que leia o nome de uma cidade e diga se ela comeca ou nao com SANTO

cd = 'SANTO'

nome = str(input('Digite o nome de uma cidade: ')).strip()
nome = nome.upper()

print(cd in nome)

# programa que leia o nome de uma pessoa e diga se tem Silva nela

name = str(input('Digite seu nome: ')).strip().title()
name2 = 'Silva'

print('Seu nome tem silva? {}'.format(name2 in name))