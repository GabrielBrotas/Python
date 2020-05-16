# programa que leia a idade e o sexo de varias pessoas, a cada pessoa cadastrada perguntar se quer continuar
# mostre quantas pessoas tem mais de 18 anos, quantos homens foram cadastrados e quantas mulheres tem menos de 20 anos

anos = 0
homens = 0
mulheres = 0

while True:
    idade = int(input('Qual sua idade? '))
    sexo = str(input('Qual seu sexo [M] ou [F]? ')).strip().upper()[0]
    while sexo not in 'FfMm':
        sexo = str(input('Qual seu sexo [M] ou [F]? ')).strip().upper()[0]

    if idade > 18:
        anos += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulheres += 1

    escolha = str(input('Deseja continuar os cadastros? [S]/[N]: ')).strip().upper()[0]
    while escolha not in 'SsNn':
        print('Digite uma opcao valida')
        escolha = str(input('Deseja continuar os cadastros? [S]/[N]: ')).strip().upper()[0]

    if escolha == 'N':
        break

print(f'{anos} pessoas tem mais que 18 anos')
print(f'{homens} homens foram cadastrados')
print(f'{mulheres} mulheres tem menos de 20 anos')

