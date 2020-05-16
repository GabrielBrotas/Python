
#leia o primeiro termo de uma PA e a razao da PA
#N o final mostre os 10 primeiros digitos dessa progressao

primeiro = int(input('Primeiro termo da PA: '))
razao = int(input('Razao da PA: '))

decimo = primeiro + (10 - 1) * razao  # Formula para encontrar o termo 10 termo da PA, calcular o enesimo, se querer o termo 20 calcular 20 -1

for c in range(primeiro, decimo + razao, razao):
    print(c, end=' -> ')
print('FIM')