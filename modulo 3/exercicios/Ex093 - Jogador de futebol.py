# Programa que leia gerencie o aproveitamento de um jogador de futebol, leia o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitas em cada partida, No final tudo isso sera mostrado em um dicionario,
# incluindo o total de gols feitos durante o campeonato

dados = {'nome': str(input('Digite o nome do jogador: ')).strip().title()}
qtd = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

gols = []

for c in range(0, qtd):
    gols.append(int(input(f'    Quantos gols na partida {c}: ')))

dados['gols'] = gols[:]
dados['total'] = sum(gols)
print('=-'*20)
print(dados)
print('=-'*20)
for v, n in dados.items():
    print(f'O campo {v} tem valor {n}')
print('=-'*20)
print(f'O jogador {dados["nome"]} jogou {len(dados["gols"])} jogos: ')

for i, v in enumerate(dados["gols"]):
    print(f'    =>na partida {i} fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols')


