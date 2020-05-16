n = input('Digite algo: ')
numero = int(input("digite um numero: "))
num1 = float(input("digite um numero decimal: "))
nome = str(input("digite algum nome: "))


print(type(n))        # mostrar o tipo de 'n', se é int, float, bool, str...
print(n.isnumeric())   # vai dizer se n é numerico ou nao, imprimindo true or false
print(n.isalpha())     # vai dizer se n é alfabetico ou nao, imprimindo true or false
print(n.isalnum())     # vai dizer se n é alfabetico e numerico, os dois junto, ou nao, imprimindo true or false
print(n.isupper())     # vai dizer se n esta tudo maiusculo ou nao, imprimindo true or false
print(n.islower())     # vai dizer se n esta tudo minusculo ou nao, imprimindo true or false
print(n.capitalize())  # vai dizer se tem maiuscula e minuscula, imprimindo true or false