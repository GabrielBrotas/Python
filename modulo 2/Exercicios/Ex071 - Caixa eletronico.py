# Simulacao de um caixa eletronico, perguntar o valor que vai ser sacado e o programa vai informar quantas celulas de cada serao entregues
# o caixa possui nota de 50, 20, 10 e 1

saque = int(input('Qual o valor a ser sacado? R$'))

n1 = saque // 50
saque = saque - (n1*50)

n2 = saque // 20
saque = saque - (n2*20)

n3 = saque // 10
saque = saque - (n3*10)

n4 = saque // 1
saque = saque - (n4*1)

print(f'''Voce tirou:
{n1} notas de 50
{n2} notas de 20
{n3} notas de 10
{n4} notas de 1
''')