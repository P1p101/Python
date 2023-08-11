import statistics



def calcular_desvio_padrao(p_valores):
    p_desvio_padrao = statistics.stdev(p_valores)
    return p_desvio_padrao



valores = []
qtde_valores = int(input('Digite a quantidade de valores: '))
for i in range(qtde_valores):
    valor = float(input('Digite um valor: '))
    valores.append(valor)

desvio_padrao = calcular_desvio_padrao((valores))
print('O desvio padrão dos valores é', desvio_padrao)