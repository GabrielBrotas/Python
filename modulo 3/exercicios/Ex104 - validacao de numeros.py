def LeiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! Digite um numero inteiro valido!')
        if ok:
            break
    return valor


# programa principal
n = LeiaInt('Digite um numero: ')
print(f'Voce acabou de digitar {n}')