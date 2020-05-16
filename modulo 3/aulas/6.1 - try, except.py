try:    # o python vai tentar realizar este comando
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b     # caso aconteca qualquer erro de valor ou divisao por 0, etc.. Ele vai pular para o comando except

except (ValueError, TypeError):   # caso aconteca erro de valor ou de tipo
    print('Tivemos um problema com os tipos de dados que voce digitou')

except ZeroDivisionError:   # pode ter diversos except para tratar diferentes tipos de erro
    print(f'Nao tem como dividir um numero por zero')

except KeyboardInterrupt:
    print('O usuario preferiu nao informar os dados')

except Exception as erro:
    print(f'erro encontrado {erro.__cause__}')
else:
    print(f'O resultado = {r}')
finally:
    print('Volte sempre! Obrigado!')    # o finally vai acontecer sempre independente de o try der certo ou errado, comando opcional