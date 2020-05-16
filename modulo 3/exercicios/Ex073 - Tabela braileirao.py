
# crie uma tupla com os 20 primeiros colocados da tabela do brasileirao na ordem de colocacao e mostre:
# a) os 5 primeiros colocados
# b) Os ultimos 4 colocados
# c) Lista na ordem alfabetica com os times
# d) Em que posicao ta o chapecoense

times = ('Palmeiras', 'Flamengo', 'Internacional', 'Gremio', 'Sao Paulo',
         'Atletico MG', 'Athletico PR', 'Cruzeiro', 'Botafogo', 'Santos', 'Bahia',
         'Fluminense', 'Corinthias', 'Chapecoense', 'Ceara SC', 'Vasco da Gama',
         'Sport Recife', 'America MG', 'Ec Vitoria', 'Parana')

print(f'Os 5 primeiros colocados foram: {times[:5]}, Respectivamente')

# caso fosse listar os times ao inves de deixar na linha usar o camando for
# for t in times:
    # print(t)

print(f'Os ultimos colocados foram{times[-4:]}')
print(f'Times em ordem alfabetica: {sorted(times)}')


print(f'O Chapecoense esta na posicao {times.index("Chapecoense")}')





