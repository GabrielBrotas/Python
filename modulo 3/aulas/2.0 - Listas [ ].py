# Listas sao variaveis compostas que sao mutaveis, podem ser alterado os valores internos e adicionar ou remover novos valores

lanche = ['hamburguer', 'refri', 'suco', 'pizza']

print(lanche)
lanche[1] = 'Batata'  # Para substituir o endereco 1
print(len(lanche))
lanche.append('torta')  # Comando para adicionar um valor na lista
print(lanche)
print(len(lanche))

print(lanche[1])
lanche.insert(1, 'pastel')  # Inserir(no endereco 1, o pastel
print(lanche)
print(lanche[1])

del(lanche[1]) # Para deletar um item da lista
print(lanche)
# ouu
lanche.pop(1)  # Normalmente o comando pop deleta o ultimo item, porem pode ser usado para deletar um endereco
print(lanche)
lanche.pop()
print(lanche)

if 'pizza' in lanche:  # Se a pizza nao tiver no lanche daria erro por isso o comando if
    lanche.remove('pizza')  # Para remover um elemento
print(lanche)



