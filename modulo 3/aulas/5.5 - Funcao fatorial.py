def fatorial(num=1):
    f = 1
    for c in range(num, 1, -1):
        f *= c
    return f


n = int(input('Digite um numero: '))
print(f'O fatorial de {n}: {fatorial(n)}')

