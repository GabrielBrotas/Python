
valores = [1, 2, 3, 4, 5, 6]


def dobra(lst):  # ja que a lista e imutavel nao precisa empacotar ela com o *
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


print(valores)
dobra(valores)
print(valores)
