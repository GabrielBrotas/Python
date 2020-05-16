c = ('\033[m',          # 0 sem cor
     '\033[0;30;41m',   # 1 vermelho
     '\033[7;30m')       # 2 branco


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 0)
    print(c[2], end='')
    help(com)
    print(c[0], end='')

def titulo(msg, cor=0):
    tam = len(msg)
    print(c[cor], end='')
    print('-'*tam)
    print(f'  {msg}')
    print('-'*tam)
    print(c[0], end='')


# Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYTHON', 1)
    comando = str(input("Funcao ou biblioteca > "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
titulo('ATE LOGO', 1)