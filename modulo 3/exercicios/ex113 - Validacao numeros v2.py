# Reescreva a funcao leiaint() que fizemos no desafio 104, incluindo agora a possibilidade da digitacao de um numero do tipo invalido
# Cria uma funcao leiaFloat()


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO, por favor digite um numero inteiro valido')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida')
        else:
            return n


n = leiaInt('Digite um inteiro: ')
print(f'O valor inteiro digitado foi {n}')