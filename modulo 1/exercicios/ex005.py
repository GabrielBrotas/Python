#programa que leia um numero inteiro e mostre seu sucessor e antecessor

num = int(input('digite um numero: '))

print('numero digitado:', num, '\nantecessor:', num-1, '\nsucessor: ', num+1)

#programa que leia um numero e mostre o seu dobro, triplo e raiz quadrada

num2 = int(input('digite um numero: '))

print('numero digitado: ', num2, '\ndobro: ', num2*2, '\ntriplo: ', num2*3, '\nraiz: ', num2**(1/2))
print('\nnumero digitado: {} \ndobro: {} \ntriplo:{} \nraiz: {:.3f}'.format(num2,num2*2,num2*3,num2**(1/2)))

#programa que leia a nota de dois alunos e mostre a media

nota1 = float(input('\nprimeira nota: '))
nota2 = float(input('segunda nota: '))

print('a media e: {}'.format((nota1+nota2)/2))
