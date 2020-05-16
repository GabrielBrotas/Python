# Funcao chamada escreva() que receba um texto qualquer como parametro e mostre uma mensagem com tamanho adaptavel


def escreva(txt):
    print('-'*(len(txt)+6))
    print(f'   {txt}')
    print('-'*(len(txt)+6))


escreva('Ola Mundo meu nome gabriel')