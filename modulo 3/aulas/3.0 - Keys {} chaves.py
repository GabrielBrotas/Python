# As chaves sao usadas como dicionario, ao inves de terem o endereco com indices numericos sao defenidos com titulos
# tuplas - () IMUTAVEIS
# listas - [] Mutaveis e compostas
# Keys/Dicionarios - {} Mutaveis e indices com titulos

dados ={'nome': 'Gabriel', 'idade': 19}  #ao inves de se indice 0 e 1 sera indice nome e gabriel

print(dados)
print(dados['nome'])
print(dados['idade'])

# Para adicionar valores:
dados['sexo'] = 'M'  # vai criar o indice sexo.
print(dados)

# deletar valores
del(dados['idade'])
print(dados)
