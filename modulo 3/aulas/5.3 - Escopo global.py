def teste(b):
    global a   # neste caso nao vai criar um escopo local para o a, o a de fora vai ser igual o de fora, um escopo global
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


# Programa principal
a = 5
teste(a)
print(f'A fora vale {a}')