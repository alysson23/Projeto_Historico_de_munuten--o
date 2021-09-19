import pandas as pd
import matplotlib.pyplot as plt
x = ''
while True:
    arquivo = pd.read_excel(r"C:\Users\Alysson\OneDrive\Desktop/planilha.xlsx")
    x = input(str("Digite o nome do produto "))
    dados_filtrados = arquivo["Produtos"]
    for c in dados_filtrados:
        if x == c:
            dados_filtrados = arquivo["Produtos"] == x
            print(arquivo[dados_filtrados])
            arquivo[dados_filtrados].clear()