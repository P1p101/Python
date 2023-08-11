def contar_palavras_frase(p_frase):
    p_palavras = p_frase.split()
    p_qtde_palavras = len(p_palavras)
    return p_qtde_palavras




frase = input("Digite uma frase: ")
qtde_palavras = contar_palavras_frase(frase)
print("A frase possui", qtde_palavras,"palavras.")