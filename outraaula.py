import math

def calcular_media_geometrica(numeros):

    produto = 1
    for num in numeros:
        produto *= num
    media_geometrica = math.pow(produto, 1/len(numeros))
    return media_geometrica

numeros = []
qtde_numeros = int(input('Digite a quantidade de números: '))
for i in range(qtde_numeros):
     num = float(input('Digite um número: '))
     numeros.append(num)

media_geometrica = calcular_media_geometrica(numeros)
print(f'A média geométrica dos números é: {media_geometrica:.2f}')
