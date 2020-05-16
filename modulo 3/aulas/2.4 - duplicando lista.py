a = [2, 3, 4 ,7]
b = a
# neste caso se alterar o valor de b tambem vai mudar o valor de a por q isso vai criar uma ligacao entre eles
# exemplo
b[2] = 8
print(a)
print(b)

# para alterar os valores deve fazer assim:
c = [4, 9, 7, 8]
d = c[:]  #o b vai receber uma copia de todos os valores de a, nao da lista em si
d[2] = 8
print(c)
print(d)
