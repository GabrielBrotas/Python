# Programa que leia o nome, ano de nascimento e a carteira de trabalho e casdastre - os (com idade) em um dicionario
# se por acaso a carteira de trabalho for diferente de 0, o dicionario recebera tambem o ano de contratacao e o salario
# Calcule e acrescente, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

dados = {'nome': str(input('Nome: '))}
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0) nao tem: '))

if dados['ctps']  != 0:
    dados['contrato'] = int(input('Ano de contratacao: '))
    dados['salario'] = float(input('Salario: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contrato'])) + 35 - datetime.now().year
print('=-' * 20)

for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')


