# Programa onde 4 jogadores joguem um dado e tenham resultados aleatorios. Guarde esses resultados em um dicionario. No final,
# coloque esse resultado em ordem, sabendo que o vencedor tirou o maior numero do dado

from random import randint
from time import sleep
from operator import itemgetter # Para pegar um indice de um dicionario

dados = {'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}
ranking = []
for c, k in dados.items():
    print(f'O {c} tirou {k} nos dados')
    sleep(1)
print('=-'*20)    # filtrar os valores, do indice 1  na ordem inversa(maior para o menor
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print(ranking)

for i, v in enumerate(ranking):
    print(f'o {i+1} lugar: {v[0]} com {v[1]}')

