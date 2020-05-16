# contagem regressiva para o estouro de fogos de artificil de 10 ate 1, com uma pausa de 1s entre eles

from time import sleep

for c in range(10, 0, -1):
    print(c)
    sleep(1)

print('KABUUUUMMMMMM')

