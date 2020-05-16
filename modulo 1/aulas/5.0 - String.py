# Cada caracter em um texto fica armazenado em uma caixa que contem um endereco (0,1,2,3,4...)
# Exemplo frase = 'Curso em Video python' nessa string o endereco vai de 0 ate 20, contendo 21 caracteres
# isto serva para fazer fatiamentos

# Fatiamento ------------------------------------------------------------------------------------------------------------------
# Ex: frase[9], vai mostrar o caracter V, quando coloca entre [] pega um endereco no array/string
# Ex: frase[9:14], vai mostrar 'Video', a letra o ta no endereco 13 entao tem q colocar no cochete 14 pois ele nao pega o ultimo
# EX: frase[9:21], = 'Video python'
# Ex: frase[9:21:2], vai pular de 2 em 2 as casas = 'Vdopto' ,
# Ex: frase[:5], quando omite o inicio ele considera a primeira casa [0:5]
# Ex: frase[15:], quando omite o final ele considera a ultima casa [15:21]
# Ex: frase[9::3], quando tem dois ponto 2x mostra q vai pegar do 9 ate o final pulando 3 casas
# ------------------------------------------------------------------------------------------------------------------

# len(frase) - mostra o tamanho da frase, lenght
# frase.count('o') - contar a quantidade de o q tem na string, ele diferencia maiuscula de minusculas, O != o
# frase.count('o',0,13) - vai contar a qntd de o com o fatiamento de 0 ate 12, pois nao conta o caracter de num 13
# frase.find('deo') - vai mostrar onde q comecou o 'deo' ou seja, 11 na string 'Curso em Video Python'
#       caso coloque frase.find('Android') ele vai retornar -1 pois nao encontrou essa string na frase
#       'Curso' in frase, vai retornar True or False, serve como um operador de analise

# Transformacao ---  'Curso em Video Python'
# frase.replace('Python','Android') - vai substituir os nomes
# frase.upper() - vai transformar todas as letras em maiusculas
# frase.lower() - todas as letras em minusculas
# frase.capitalize() - vai deixar todas as letras minusculas e so a primeira da frase em maiuscula - 'Curso em video python'
# frase.title() - vai deixar a primeira letra de cada palavra maiuscula - 'Curso Em Video Python'

# frase.strip() - vai remover os primeiros espacoes e ultimos de uma frase, sao espacos inuteis
#               Ex: '   Aprenda Python   ' -- 'Aprenda Python'
# frase.rstrip() - vai remover apenas os ultimos espacos da direita, r - right
# frase.lstrip() - vai remover apenas os ultimos espacos da direita, l - left

# Divisao --------------------------------------------------------------------------------------------
# frase.split() - vai separar todas as palavras de um texto ex ('Curso em Video Python')
# o split vai separar em 4 pedacos(novo endereco) - Curso(1) em(2) Video(3) Python(4)

# Juncao -----------------------------------------------------------------------------------------
# '-'.join(frase) - vai colocar entre os espacos este caracter '-' = 'Curso-em-Video-Python)
