def converter_polegadas_para_cm(polegadas):
    cm = polegadas * 2.54
    return cm

polegadas = float(input('Digite o valor em polegadas: '))
cm = converter_polegadas_para_cm(polegadas)
print('O valor em centímetros é: ', cm)
