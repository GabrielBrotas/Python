#pode importar uma biblioteca de duas forma
#a primeira e a de pegar todas as funcoes de uma biblioteca por exemplo( import math )
#a segunda e para pegar uma funcao especifica dentro de uma biblioteca ex( from(math(import(factorial))) o que ocupa menos espaco


#import math ---------               para importar uma biblioteca
from math import ceil, floor,sqrt         #caso so queira importar alguams funcoes de uma biblioteca fazer assim
        #caso importe a biblioteca inteira tem q colocar o nome dela na frente, ex{math.ceil(raiz)}
        #caso importe apenas uma ou mais funcao de uma biblioteca nao colocar o nome dela na frente ex { ceil(raiz) }


num = int(input('digite um numero: '))
raiz = sqrt(num) #quando digita math. mostra todas as funcoes que vem nessa biblioteca, sqrt = raiz quadrada
                     # caso tire a biblioteca math do codigo vai sumir as opcoes de math
print('a raiz de {} e igual a = {:.2f}'.format(num, raiz))
print('a raiz de {} e igual a = {}'.format(num, ceil(raiz))) # o comando ceil arredonda o valor para cima
print('a raiz de {} e igual a = {}'.format(num, floor(raiz))) # o comando floor arredonda o valor para baixo

#para verificar todas as bibliotecas apenas ir no site do python, selecionar docs e escolher a versao do python
#para verificar a versao do python clicar word + r e digitar `cmd` e escrever `pyhton --version`
#selecionando a versao ir em `library reference`
# vai mostrar todas as bibliotecas por categoria e se clicar em uma os exemplos e funcao de cada

import random
num = random.random() #random.random gera um numero aleatorio entre 0 e 1
num2 = random.randint(1, 10) #randint e um numero aleatorio e inteiro, com a condicao entre 1 e 10.
print(num, num2)

