# programa que tenha um funcao chamada ficha() q receba dois parametros opcionais, o nome de um jogador e quantos gols ele fez
# mostre a ficha do jogador mesmo que algum dado nao tenha sido informado corretamente


def ficha(nome="<unknow>", gols=0):
    print(f'O jogador {nome} fez {gols} gols')



n = str(input('Nome: '))
g = str(input('Quantidade de gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)





