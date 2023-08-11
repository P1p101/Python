def calcular_potencia(p_base, p_expoente):
    p_resultado = p_base ** p_expoente
    return p_resultado

base = float('Digite a base: ')
expoente = float(input('Digite o expoente: '))
resultado = calcular_potencia(base, expoente)
print('O resultado da potenciação é: ', resultado)
