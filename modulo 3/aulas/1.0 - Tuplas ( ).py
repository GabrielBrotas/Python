
# Tuplas sao imutaveis, nao se pode substituir um valor enquanto o programa estiver rodando
# oq foi definido no inicio permanece ate o final

lanche = ('hamburguer', 'pizza', 'suco', 'refri')
print(lanche[1])
print(lanche[-1])  #-1 mostra o ultimo elemento

print(sorted(lanche))  #para organizar a lista em ordem alfabetica porem nao vai mudar os iten

for comida in lanche:
    print(f'comi bastante {comida}')    # A variavel comida vai percorrer cada valor na lista lanche, vai pegar os nomes
print('estou gordo')

for cont in range(0, len(lanche)):
    print(cont)                         # vai pegar o endereco da lista (0,1,2...) por causa das ()
print('fim')

for food in range(0, len(lanche)):
    print(lanche[food], f'na posicao {food}')                 # vai pegar na lista lanche o endereco food 0,1,2,3...
print('end')


