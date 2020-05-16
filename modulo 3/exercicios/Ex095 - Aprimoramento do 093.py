# aprimore o cadastro de jogadores para que funcione com diversos jogadores,
# incluindo um sistema de visualizacao de detalhes do aproveitamento de cada jogador

lista = []
gols = []
dados = {}

from operator import itemgetter

while True:
    dados['nome'] = str(input('Digite o nome do jogador: ')).strip().title()
    qtd = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    for c in range(0, qtd):
        gols.append(int(input(f'    Quantos gols na partida {c}: ')))

    dados['gols'] = gols[:]
    lista.append(dados.copy())
    dados.clear()
    gols.clear()
# ----------------------------------------------------------------------------------
    sn = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while sn not in 'SsNn':
        sn = str(input('Digite uma opcao valida [S/N] ')).upper().strip()[0]
    if sn in 'Nn':
        break
# ----------------------------------------------------------------------------------
print('=-'*20)
print(f'{"cod":<5}{"nome":<15}{"gols":<20}{"total":<5}')
for n, v in enumerate(lista):
    print(f'{n:<5}{lista[n]["nome"]:<15}{str(lista[n]["gols"]):<15}{sum(lista[n]["gols"]):>10}')

print('=-'*20)
while True:
    opc = int(input('Deseja ver os dados de qual jogador?'))
    if opc == 999:
        break
    else:
        print(f'---  levantamento do jogador {lista[opc]["nome"]}  ---')
        for p, n in enumerate(lista[opc]["gols"]):
            print(f'No jogo {p} fez {lista[opc]["gols"][p]}')

print('=-'*20)
print('FIM')
print('=-'*20)
