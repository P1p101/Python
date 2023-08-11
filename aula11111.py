def contar_digitos(p_numero):
    p_digitos = len(str(p_numero))
    return p_digitos




numero = int(input('Digite um número: '))
qtde_digitos = contar_digitos(numero)
print('O número possui', qtde_digitos, 'Dígitos.')