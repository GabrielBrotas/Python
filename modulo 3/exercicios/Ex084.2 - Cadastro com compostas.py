temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()

    resp = str(input('Quer continuar? ')).upper().strip()[0]
    if resp in 'Nn':
        break
print('=-'*20)
print(f'Ao todo voce cadastrou {len(princ)} pessoas')
print(f'O maior peso foi {mai}kg. Peso de', end=' ')

for p in princ: #varrer a lista principal para ver quem tem o maior peso
    if p[1] == mai:
        print(f'{p[0]}', end=' ')

print(f'\nO menor peso foi de {men}KG.', end='')
for c in princ:
    if c[1] == men:
        print(f'{c[0]}', end='')
