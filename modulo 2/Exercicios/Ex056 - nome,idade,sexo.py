# programa que leia o nome,idade e sexo de 4 pessoas. No final mostre:
# A media de idade do grupo
# Qual o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos

i = 0
media = 0
old = ''
qtdmulher = 0

for c in range(0, 4):

    nome = str(input('Digite um nome: ')).strip()
    idade = int(input('Idade: '))



    s = int(input(''' Qual seu sexo?
     [ 1 ] Masculino
     [ 2 ] Feminino 
     sexo: '''))

    if s == 1:
        sexo = 'masculino'
    elif s == 2:
        sexo = 'feminino'


    media += idade

    if idade > i and s == 1:
        old = nome

    if idade < 20 and s == 2:
        qtdmulher += 1

    i = idade

mediagrupo = (media / 4)

if old == '':
    old = 'Não tem homem neste grupo!'


print('a media da idade do grupo e: ', mediagrupo)
print('o nome do homem mais velho e : ', old)
print('{} mulheres tem idade menor que 20 anos.'.format(qtdmulher))



