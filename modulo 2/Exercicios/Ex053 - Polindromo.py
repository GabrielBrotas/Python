#programa que leia uma frase e dizer se ela for um polindromo, ler de tras pra frente e a mesma coisa
# ex APOS A SOPA / A SACADA DA CASA / A TORRE DA DERROTA / O LOBO AMA O BOLO / ANOTARAM A DATA DA MARATONA

from time import sleep

frase = str(input('Digite a frase: ')).lower().strip()
frente = ''
verso = ''

for a in range(0, len(frase)):

    if frase[a] != ' ':       # outra forma de analisar a frase sem espacos é usar o comando split para separar cada palavra e depois
        frente += frase[a]    # usar o comando join ( junto = ''.join(frase) ) que vai juntar a frase sem espaços na variavel junto
        print(frente)
        sleep(0.2)            # outra forma de inverter é ( inverso = junto[::-1] ) que vai pegar do inicio ao fim e virar de tras pra frente


for b in range(len(frase)-1, -1, -1):

    if frase[b] != ' ':
        verso += frase[b]
        print(verso)
        sleep(0.2)


if frente == verso:
    print('ESTA FRASE E UM POLINDROMO !!')
else:
    print('Esta frase nao e um polindromo')
