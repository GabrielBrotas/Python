#leia o nome de uma pessoa completo e mostre o primeiro e ultimo nome

nome = str(input('digite um nome: ')).title().strip()

name = nome.split()
ult = int(len(name) - 1)

print('Seu nome: ', nome)
print('Primeiro: ', name[0])
print('Ultimo: ', name[ult])



