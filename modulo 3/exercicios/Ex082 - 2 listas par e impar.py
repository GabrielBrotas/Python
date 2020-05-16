# programa que leia varios numeros e coloque em uma lista, depois crie duas listas extas que vao conter apenas os valores pares e
# valores impares digitados respectivamente
# mostre o conteudo das 3 listas geradas

lista = []
sn = ''
a = []
b = []

while True:

    lista.append(int(input('Digite um valor: ')))      # inserir valor em a

    # -------------------- Continuar ou Nao ----------------------------
    sn = str(input('Deseja Continuar? ')).strip().upper()[0]
  
    while sn not in 'SsNn':
        print('Digite uma opçao valida! ')
        sn = str(input('Deseja Continuar? ')).strip().upper()[0]
        
    if sn in 'Nn':
        print('=-'*20)
        break
    # -------------------- ---------------------------------------------

for c, v in enumerate(lista):  # Transeferir os pares e impares
    if v % 2 == 0:
        a.append(v)
    else:
        b.append(v)

print(f'A lista completa: {lista}')
print(f'A lista com numeros pares: {a}')
print(f'A lista com numres impares {b}')


