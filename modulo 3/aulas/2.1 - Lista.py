# pode criar listas a partir de ranges

valores = list(range(4, 11))  # Cria de forma ordenada de 4 ate 10, o ultimo nao conta
print(valores)

valor = list(range(4, 21, 2))  # Range(Start, Stop, Step)
print(valor)

lista = [2, 4, 9, 5, 3, 4, 6, 5, 7]
lista.sort()  #vai organizar os valores da lista e manter ela neste formato
print(lista)
lista.sort(reverse=True)  #para organizar de forma inversa
print(lista)


