import pandas as pd
from IPython.display import display

#Criando Data Frame
dados_estoque = pd.DataFrame({

    "Produto": ["Teclado", "Mouse", "Monitor", "HeadSet", "Webcam"],
    "Quantidade": [15, 8, 5, 20, 3],
    "Preco_Unitario": [120.00, 80.00, 900.00, 250.00, 300.00]

})

#Salvando arquivo
dados_estoque.to_csv("arquivos_projetos/dados_estoque.csv", index = False)

#Criando a coluna Valor_Total.
dados_estoque["Valor_Total"] = dados_estoque["Quantidade"]*dados_estoque["Preco_Unitario"]

#Criando a coluna STATUS.
estoque_minimo = 10

dados_estoque["Status"] = "OK"
dados_estoque.loc[dados_estoque["Quantidade"] < estoque_minimo, "Status"] = "REPOR"

#Filtrando produtos que precisam de reposição e que estão OK.
produtos_repor = dados_estoque[dados_estoque["Status"] == "REPOR"]
produtos_OK = dados_estoque[dados_estoque["Status"] == "OK"]


#Salvando arquivo após tratamento de dados.
dados_estoque.to_csv("arquivos_projetos/dados_estoque_Final.csv", index = False)

#Exibindo resultados.
print("ESTOQUE COMPLETO:")
display(dados_estoque)

print("\n PRODUTOS PARA REPOSIÇÃO:")
display(produtos_repor)

print("\nProdutos que estão OK:")
display(produtos_OK)
