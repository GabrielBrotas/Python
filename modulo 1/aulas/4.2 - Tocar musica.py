#Instalar a biblioteca primeirp

from pygame import mixer       # Para iniciar o modulo
mixer.init()                   # Copiar o arquivo mp3 e colar na pasta `aula` q esta os arquivo do python
mixer.music.load('birds.mp3')  # Comando para carregar a musica
mixer.music.play()
input('agora ouve?')           # Para nao fechar o programa ate fechar


