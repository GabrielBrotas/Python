

situacao = {'aluno': str(input('Nome: ')), 'media': float(input('Media: '))}

print(f'nome: {situacao["aluno"]}')
print(f'Media: {situacao["media"]}')
if situacao['media'] >= 7:
    print('Aprovado')
else:
    print('Reprovado')



