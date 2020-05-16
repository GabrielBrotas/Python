# +  = adiçao
# -  = subtração
# *  = multiplicação
# /  = divisao
# ** = potencia ex( 5 ** 2 = 25) ou pelo comando pow(5,2) = 25
# // = divisao inteira ( é a divisao sem virgula ex ( 5/2 =2.5 e 5//2 = 2)
# %  = resto da divisao ( exemplo: 5/2 = 1, pois é o que restou da divisao)

#raiz quadrada de um termo = num**(1/2) ex( 9**(1/2) = 3)
#raiz cubica num**(1/3) ex 8**(1/2) = 2

#operadores com variaveis
# exemplo:
print('='*20) #resultado vai ser '=' 20 vezes

nome = input('digite um nome: ')
print('Prazer em te conhecer {:20}!'.format(nome))   # vai escrever o nome com 20 espacoes no minimo, levando a exclamacao para o final
print('Prazer em te conhecer {:>20}!'.format(nome))  #vai alinhar o nome a direita, em 20 espaçoes
print('Prazer em te conhecer {:<20}!'.format(nome))  #vai alinha a esquerda
print('Prazer em te conhecer {:^20}!'.format(nome))  #vai centralizar entre os 20 espaçoes
print('Prazer em te conhecer {:=^20}!'.format(nome))  #para colocar igual nos espaços vazios entre os 20



