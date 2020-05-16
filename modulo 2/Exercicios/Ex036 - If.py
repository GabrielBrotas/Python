# Programa para aprovar um emprestimo bancario para a compra de uma casa
# Perguntar o valor da casa, o salario do comprador, e em quantos anos ele vai pagar
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou entao o emprestimo sera negado

valor = float(input('Valor da casa: R$ '))
sal = float(input('Salario: R$ '))
anos = int(input('Quantos anos para pagar? '))

prest = valor / (anos * 12)

print('Valor da Casa: R$', valor)
print('Salario do Comprador: R$', sal)
print('O valor mensal da prestação será: {:.2f}'.format(prest))

if prest >= (sal * 30/100):
    situ = 'maior'
    situ2 = 'Negado'
else:
    situ = 'menor'
    situ2 = 'Aprovado'

print('O valor da prestação é R${:.2f}, é {} que 30% do seu salário, emprestimo {} '.format(prest, situ, situ2))

