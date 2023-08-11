def converter_dolar_para_real(pvalor_dolar, pcotacao):
    pvalor_real = pvalor_dolar * pcotacao
    return pvalor_real

valor_dolar = float(input('Digite o valor em dólar: '))
cotacao = float(input('Digite a cotação em dólar: '))
valor_real = converter_dolar_para_real(valor_dolar, cotacao)
print(f'O valor em reais é: {valor_real:.2f}')
