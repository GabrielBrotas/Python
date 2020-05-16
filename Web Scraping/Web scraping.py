import requests  # permite pegar o url de uma pagina
from bs4 import BeautifulSoup
import pandas  # faz uma tabulacao nos dados

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.0535&lon=-118.2453#.XopMq8hKjcc')
soup = BeautifulSoup(page.content, 'html.parser') # faz a web mais facil de ler as estruturas
            # pegar o conteudo da pag e analisar como uma pagina html

# print(soup) o resultado disso vai ser o codigo da web, se clicar no site com o botao direito e ir em 'View page source'
             # vai aparecer o mesmo codigo

week = soup.find(id="seven-day-forecast-body")
# para saber o id abrir a inspecao de elementos e clicar na imagem q tem o simbolo do icone do percusor do mouse(primeira opcao)
# vai permitir saber os dados de cada bloco. neste caso botar em cima do bloco em que pega todos os dias da semana com a temperatura
# clicar no bloco e o codigo vai ser destacado no elemento. no codigo vai ter a descricao do id e colocar na variavel week

# print(week) vai mostrar tudo que tem dentro do bloco week

# dentro do bloco 'seven-day-forecast-body' a gente vai procurar a classe que esta os itens, todos esses itens estao dentro de uma classe

items = week.find_all(class_="tombstone-container")  # dentro do bloco que tem o id, procurar todas as classes que tem em 'tombstone-container'
# para achar a classe olhar do mesmo jeito que encontro o id, indo no bloco e procurando o nome class
print(items[0])  # vai pegar o primeiro bloco da 'lista'
# no primeiro item procurar a classe 'period-name' que pode descobrir colocando o mouse com o inspetor em cima do nome ou dando print
# no items[0] e ver a classe que quer buscar
print()
print(items[0].find(class_='period-name'))
print(items[0].find(class_='period-name').get_text())  # pegar apenas o nome que tem contido na classe 'period-name' do item[0]
print(items[0].find(class_='short-desc').get_text())  # pegar apenas o nome que tem contido na classe 'short-desc'
print(items[0].find(class_='temp').get_text())  # pegar apenas o nome que tem contido na classe 'temp'
print()
# todos estes dados estao contido na lista items, entao basta fazer um loop para mostrar todos

period_names = [item.find(class_='period-name').get_text() for item in items]
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
temperature = [item.find(class_='temp').get_text() for item in items]
print()
print(period_names)
print(short_descriptions)
print(temperature)
print()

weather_stuff = pandas.DataFrame(
    {
        'period': period_names,
        'short_descriprtions': short_descriptions,
        'temperature': temperature,
    })

print(weather_stuff)

weather_stuff.to_csv('weather.csv')  # para criar um arquivo csv, xlsx, etc..
# quando rodar o programa vai criar um arquivo na pasta. so abrir
# Para pegar os dados de outra localizacao basta apenas trocar o url, tem q ser no mesmo site para ter as mesmas condicoes














