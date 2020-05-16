def teste():
    x = 8
    print(f'Na funcao teste, n vale {n}')
    print(f'Na funcao teste, x vale {x}')


def funcao():
    n = 8
    print(f'n dentro vale {n}')  # o valor q alterar em n dentro dessa funcao nao vai alterar a do programa princial
                                 # n aqui vai ser um escopo local e fora um global, variaveis com nome igual mas valores diferentes

# Programa principal
n = 2
print(f'No programa principal, n vale {n}')
funcao()
teste()
print(f'No programa principal, x vale {x}')  # vai dar erro pois x foi declarado apenas na funcao teste, ela e uma variavel local
                                             # ja o n e uma variavel global pois foi declarada no programa principal