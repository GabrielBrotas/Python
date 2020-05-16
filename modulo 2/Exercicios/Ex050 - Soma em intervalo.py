#programa que leia 6 numeros inteiro e mostre a soma dos que forem apenas par

soma = 0

for c in range(0, 6):

    num = int(input('digite um numero: '))

    if (num % 2) == 0:
        soma += num         #antes de somar tem que definir a soma como 0

print('a soma dos numeros pares deu {}{}{}'.format('\033[31m', soma, '\033[m'))
