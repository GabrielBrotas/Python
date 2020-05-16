from datetime import date

atual = date.today().year
nasc = int(input('Qual seu ano de nascimento? '))

idade = atual - nasc

ano = int(nasc + 18)

print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))

if idade == 18:
    print('Voce deve se alistar agora!')
elif idade > 18:
    print('Voce pasou da hora de se alistar, compareça ao tiro de guerra imediatamente')
else:
    print('voce nao precisa se alistar agora, apenas em {}.'.format(ano))
