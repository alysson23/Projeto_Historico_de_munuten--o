import pandas as pd
import matplotlib.pyplot as plt
x = ''
while True:
    arquivo = pd.read_excel(r"C:\Users\Alysson\OneDrive\Desktop/planilha.xlsx")
    x = input(str("Digite o nome do produto "))
    dados_filtrados = arquivo["Produtos"] == x
    isempty = dados_filtrados.empty
    print('Is the DataFrame empty :', isempty)
    if isempty == False:
        print(arquivo[dados_filtrados])