def calcular_media(p_nota1, p_nota2):
    media = (p_nota1 + p_nota2) / 2
    print('A média é: ', media)

arg_nota1 = float(input('Digite a primeira nota:'))
arg_nota2 = float(input('Digite a segunda nota:'))
calcular_media(arg_nota1, arg_nota2)