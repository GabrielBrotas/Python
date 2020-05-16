estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())  # O copy seria o fatiamento [:] para nao criar um link com as chave

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()

