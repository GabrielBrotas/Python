# sortear um dos quatro alunos para apagar o quadro, ler os nomes e escrever um aleatorio

import random

al1 = str(input('primeiro nome: '))
al2 = str(input('segundo nome: '))
al3 = str(input('terceiro nome: '))
al4 = str(input('quarto nome: '))

lista = [al1, al2, al3, al4] #o chochete cria uma lista / array

escolhido = random.choice(lista)  # Escolhe um entre a lista

print('o escolhido foi: ', escolhido)

random.shuffle(lista)   # Shuffle faz com que a lista altere a ordem
print('a ordem sera: ', lista)




