import urllib.request
import urllib


try:
    site = urllib.request.urlopen('https://www.google.com.br')

except urllib.error.URLError:
    print('O site nao esta disponivel')

else:
    print('Consegui acessar')