# Programa que receba uma funcao chama maior() que receba varios parametros inteiros. seu programa tem q analisar todos os valores
# e dizer qual deles é o maior.

def maior(* num):
    print('=-'*30)
    print('Analisando os valores passados...')
    for n in num:
        print(f'{n} ', end='')
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {max(num)}')


maior(4, 5, 9, 7, 6)
maior(2, 4, 5, 7, 1, 6, 8)
maior(6)

