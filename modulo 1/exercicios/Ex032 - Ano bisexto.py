#Verifiar se o ano e bisexto

from datetime import date

ano = int(input('Qual ano quer analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year


    #condicoes para o ano ser bissexto
    # ser divisel por 4 - se o resto da divisao for igual a 0
    # nao pode ser multiplo de 100 (ex:1900,1700) - se o resto da divisao por 100 for igual a 0 nao e bissexto
    # nao pode ser muitiplo de 400 - o resto da divisao por 400 nao pode ser 0
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} e bissexto!'.format(ano))
else:
    print('O ano nao e bissexto!')

