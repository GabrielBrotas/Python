# Programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero ate 20.
# Ler um numero no teclado (entre 0 e 20) e mostra lo por extenso

extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    while num > 20 or num < 0:
        print('Digite um numero valido: ')
        num = int(input('Digite um numero entre 0 e 20: '))

    print(f'Voce digitou o numero {extenso[num]}')
