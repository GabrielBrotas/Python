
filme = {'nome': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}

print(filme.values())  # Vai mostrar os valores, star wars, 1977, george lucas
print(filme.keys())  # mostra os indices
print(filme.items())  # mostra tudo

for k, v in filme.items():
    print(f'o {k} é {v}')

# dicionario composto
locadora = [{'nome': 'Star Wars', 'ano': 1977, 'diretor': 'George lucas'},
            {'nome': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whendon'},
            {'nome': 'Matrix', 'ano': 1999, 'diretor': 'Machowski'}]

print(locadora[1]['nome'])  # no 2 endereco da lista pegar o nome do dicionario


