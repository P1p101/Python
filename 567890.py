def calcular_area_triangulo(p_base, p_altura):
    area = (p_base * p_altura) / 2
    return area

base = float(input('Digite a base do triângulo: '))
altura = float(input('Digite a altura do triângulo: '))
area = calcular_area_triangulo(base, altura)
print('A área do triângulo é: ', area)
