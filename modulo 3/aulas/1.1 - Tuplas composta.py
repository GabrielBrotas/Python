# As tuplas sao imutaveis nao pode adicionar/alterar elementos durante o codigo
# Elas aceitar numero e strings juntas
# As tuplas podem ser deletas por completo, mas nao pode apenas um elemento
pessoa = ('Gabriel', 19, 'M', 65.50)
print(pessoa)
del(pessoa)  # vai deletar a lista porem nao pode fazer del(pessoa[0]) apenas a lista inteira

a = (2, 5, 4)
b = (5, 8, 1, 2)

c = a + b  # vai junta as duas tuplas, nao somar
d = b + a  # a + b != de b + a

print(c)
print(c.index(8))
print(d)
print(d.index(8))  # em qual posicao ta o numero 8 nessa tupla

print(c)
print(c.index(5, 1))  # como ja tem um 5 ta na posicao 0 agora vai comecar a partir da posicao 1
print(c.count(5))  # contar quantos numeros 5 tem na nova tupla

