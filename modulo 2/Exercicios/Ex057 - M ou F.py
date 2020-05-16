# programa que leia o sexo de uma pessoa, so pode aceitar M ou F



print('''Qual seu sexo?
     M - Masculino
     F - Feminino''')

sexo = ''

while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite a opcao: ')).strip().upper()
    if sexo != 'F' and sexo != 'M':
        print('Digite uma opcao valida!')

if sexo == 'M':
    print('Masculino')
if sexo == 'F':
    print('Feminino')

# --------------------------------------------
# outra forma

sex = str(input('Qual o seu sexo: masculino ou feminino: ')).strip().upper()[0]  # [0] para pegar apenas a primeira letra
while sex not in 'MmFf':
    sex = str(input('Dados invalidos. digite uma opcao valida: ')).strip().upper()[0]
print(sex)

