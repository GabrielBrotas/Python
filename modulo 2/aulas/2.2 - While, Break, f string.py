
n = s = 0

while True: #para criar um loop infinito
    n = int(input('Digite um numero: '))
    if n == 999:
        break #break faz ele sair do while, do loop
    s = s + n

print(f'A soma vale {s}')  # Ao inves de colocar .format() coloca um f minusculo antes das aspas e o valor que quer que apareca dentro

nome = 'jose'
idade = '18'

print(f'{nome:-^20} tem {idade:^20} anos')
