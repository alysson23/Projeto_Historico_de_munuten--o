import pandas as pd
x = ''
while True:
    arquivo = pd.read_excel(C:\Users\Alysson\OneDrive\Documents\meuprojtoGitHub\Projeto_Historico_de_munuten--o/planilha)
    x = input(str("Digite o nome do produto "))
    dados_filtrados = arquivo["Produtos"]
    for c in dados_filtrados:
        if x == c:
            dados_filtrados = arquivo["Produtos"] == x
            print(arquivo[dados_filtrados])
            break
    print("Não contém")
    resposta = " "
    while resposta not in "SN":
        resposta = str(input("Você deseja continuar [S/N] ")).strip().upper()[0]
    if resposta == "N":
        break