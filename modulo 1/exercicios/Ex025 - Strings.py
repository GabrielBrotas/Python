# Programa que leia uma frase e mostra quantas vezes aparece a letra 'A', primeira posicao e ultima posicao

text = str(input("digite uma frase: ")).strip()

print('letra `A` aparece {} vezes.'.format(text.lower().count('a')))
print('letra `A` aparece primeiro na posicao {}.'.format(text.lower().find('a')+1))
print('letra `A` aparece primeiro na posicao {}.'.format(text.lower().rfind('a')+1))

