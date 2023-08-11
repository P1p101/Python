import pandas as pd

baseDeDados = pd.read_exel(r"C:\Users\pietr\OneDrive\Área de Trabalho\BaseTeste.csv")
print(baseDeDados)

totalGasto = baseDeDados["ValorFinal"].sum()
qtdadeComprada = baseDeDados["Quantidade"].sum()
precoMedio = totalGasto / qtdadeComprada

print('total gasto:', totalGasto)
print('quantidade comprada', qtdadeComprada)
print(f'Preço médio dos produtos: {precoMedio: . 2f}')
