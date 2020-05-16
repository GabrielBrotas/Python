n1 = int(input('digite um numero: '))  # int para definir o valor do input como um numero inteiro
print(type(n1))                        # type para verificar na tela o tipo da variavel n1
n2 = int(input('digite outro valor: '))
print(type(n2))

s= n1+n2

print('a soma de n1 + n2 é:', s)
print('a soma de', n1, 'e', n2, ' vale:', s)
print('a soma de {} e {} vale {}'.format(n1, n2, s))  # se tem 3 chaves no texto o .format vai seguir a ordem das chaves

