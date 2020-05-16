valor = int(input('Valor a ser sacado: R$'))
total = valor
ced = 50  # comeca com a cedula de 50
totced = 0

while True:
    if total >= ced:    # se o saque estiver maior que a cedula de 50
        total = total - ced    # subtrair uma nota de 50 do montante
        totced = totced + 1     # somar +1 ao total de cedulas

    else:

        if totced > 0:  #considerar apenas as notar que foram sacadas
            print(f'Total de {totced} cedulas de R${ced}')   #total de cedulas sacadas de 50,20,10...

        if ced == 50:   #se a cedula era de 50, vai analisar a de 20 agora
            ced = 20

        elif ced == 20:  #se a cedula era de 20, vai analisar a de 10 agora
            ced = 10

        elif ced == 10:
            ced = 1

        totced = 0     #zerar as celulas sempre que mudar
        if total == 0:  #quando zerar o saque sair do while
            break

print('fim')

