
# comando basico para colorir padrao ANSI
# \033[0;33;44m
# contra barra 033 [, a sequencia depois e style, text, back,
# style seria 0, 1, 4 e 7
# 0 sem estilo / 1 negrito / 4 underline / 7 negativo
# o texto seria a cor
# 30 white / 31 red / 32 green / 33 yellow / 34 blue / 35 purple / 36 light blue / 37 gray
# back seria as cores de background com os mesmos padrao do texto porem de 40 a 47
# finalizar o codigo com `m` no final

#comando para fundo branco e letra preta
# \033[7;30m - o 7 serve de inversor, o fundo preto vai pra a letra e a letra branca vai para o fundo

#exemplo

print('\033[31mOla Mundo\033[m') #deixar fundo vermelho e tirar formatacao no final
print('\033[1;31;40mOla Mundo\033[m') #se nao tirar a formatacao o fundo branco vai cobrir a linha toda

a = 3
b = 5

print('os valores sao \033[32m{}\033[m e \033[35m{}\033[m'.format(a,b))

print('o valor de a vale {}{}{} congratulations'.format('\033[32m', a, '\033[m'))

