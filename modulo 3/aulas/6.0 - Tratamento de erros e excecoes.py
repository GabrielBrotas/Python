# a = int(input('Numerador: '))   # se tentarmos colocar uma letra aqui vai da erro de valor ValueError
# b = int(input('Denominador: '))    # se colocar 0 aqui vai acontecer uma excecao ZeroDivisionError - divisao por zero
# r = a/b
# print(f'A divisao de {a} por {b} vale = {r}')

# para tratar erros a gente usa o comando try, except, else

try:    # o python vai tentar realizar este comando
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b     # caso aconteca qualquer erro de valor ou divisao por 0, etc.. Ele vai pular para o comando except

except Exception as erro:   # poderia colocar apenas except:  , porem criou uma variavel para demonstrar o erro que ta aparecendo
    print(f'Erro encontrado = {erro.__class__}')  # mostrar a classe do erro

else:             # Se a operacao de try der certo ele vai realizar o comando else tambem, comando opcional
    print(f'O resultado foi = {r}')

finally:
    print('Volte sempre! Obrigado!')    # o finally vai acontecer sempre independente de o try der certo ou errado, comando opcional
