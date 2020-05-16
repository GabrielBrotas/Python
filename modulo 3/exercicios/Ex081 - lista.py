# colocar varios numeros em uma lista
# motre quantos digitos foram digitados, a lista de valores, ordenada de forma decrescente e se o valor 5 foi digitado ou nao nessa lista


lista = []
c = 0
num = 0
five = 'O numero 5 nao faz parte desta lista...'
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    c += 1

    if num == 5:
        five = 'O numero 5 faz parte desta lista...'


    sn = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while sn not in 'SsNn':
        print('Digite um valor valido')
        sn = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if sn in 'Nn':
        print('=-'*20)
        break




print(lista)
lista.sort(reverse=True)
print(lista)
print(five)