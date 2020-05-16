# programa que tenha uma funcao chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa
# retornando um valor literal indicando se a pessoa tem voto negado, opcional ou obrigatorio nas eleicoes

# < 65 anos o voto opcional
# < 18 anos obrigatorio
# > 18 opcional


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if 65 > idade >= 18:
        return print(f" pessoa com idade {idade} tem voto OBRIGATORIO")
    elif idade < 16:
        return print(f" pessoa com idade {idade} tem voto NEGADO")
    elif 18 > idade >= 16 or idade >= 65:
        return print(f" pessoa com idade {idade} tem voto OPCIONAL")


voto(int(input('Ano de nascimento: ')))


