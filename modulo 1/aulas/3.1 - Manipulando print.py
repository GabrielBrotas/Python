n1 = int(input('digite um numero: '))
n2 = int(input('digite um outro: '))
sum = n1 + n2
m = n1 * n2
dv = n1 / n2
dvint = n1 // n2
exp = n1 ** n2
       # para limitar o numero de casas decimais em uma divisao por exemplo se coloca :.3f, 3 de casa e f de float
print('a soma e: {} \n o produto e: {} \n a divisao: {:.1f}'.format(sum,m,dv), end=' <> ')  # o ,end serve para nao quebrar a linha
print('a divisao inteira e: {}, e a potencia: {}'.format(dvint, exp))                 #a debaixo vai ficar em cima
                                                                        #contra barra n `\n` serve para quebrar a linha

