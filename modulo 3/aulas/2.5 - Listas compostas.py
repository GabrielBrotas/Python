teste = []
teste.append('Gabriel')
teste.append(19)
print(teste)

galera = []
galera.append(teste[:])  # para copiar os dados de uma lista precisa do [:] se nao vai criar uma ligacao e quando mudar a lista original
print(galera)  # tambem vai mudar a lista composta q pegou o link

teste[0] = 'Pedro'
teste[1] = '21'
galera.append(teste[:])  # vai colocar ao lado da lista copiadad e gabriel a lista copiada de pedro
print(galera)

print(galera[0])  # Primera lista da lista composta
print(galera[1])
print(galera[0][0])     # Primero valor da lista na lista composta
print(galera[1][0])
print(galera[0][0][0])  # Primeiro caraceter do primeiro valor da primeira lista composta
print(galera[1][0][0])

