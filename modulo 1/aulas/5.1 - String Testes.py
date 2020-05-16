frase = 'Curso em Video Python'
print(frase)
print(frase.split())
dividido = frase.split()
print(dividido[0][3]) #na primeira palavra pegar a letra 3

print(frase[9])  # 9 e a decima letra
print(frase[9:14])
print(frase[:14])
print(frase[14:])
print(frase[:14:2])
print(frase[::2])

print(frase.upper().count('O')) #jogar a frase para maiusculo e contar as letras O maiucula

print(len(frase))
print(frase.find('Video'))
print('Video' in frase)

frase = frase.replace('Python', 'Android')

print(len(frase))

print('''este e apenas um testa para     
      mostrar que pode quebrar linha
      caso queira escrever um
      texto muito longo sem ficar 
      em uma unica linha''') #colocar aspas triplas para quebrar a linha para um texto longo """  """

