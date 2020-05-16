# Programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiusculas, o nome com todas as letras minusculas, quantas
# quantas letras ao tem sem considerar espacos, quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()  # strip para cortar os espacos vazios do inicio e fim

print('Seu nome: ', nome.upper())
print('Seu nome: ', nome.lower())

print('Seu nome tem {} quantidade de letras'.format(len(nome) - nome.count(' ')))

dv = nome.split()

print('Seu primeiro nome {} tem {} quantidade de letras.'.format(dv[0], len(dv[0])))
#outra opcao
print('Seu primeiro nome tem {} de letras.'.format(nome.find(' ')))  # Vai mostrar a posicao do primeiro espaco depois do primeiro nome

