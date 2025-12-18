"""
1 - Crie um DataFrame contendo:

    produto

    quantidade vendida

    valor da venda

    data da venda

2- Salve os dados em um arquivo vendas.csv.

3 - Leia o arquivo CSV.

    Calcule:

    O faturamento total

    O produto mais vendido (em quantidade)

    A receita total por mês
"""

import pandas as pd
from IPython.display import display

#Criando DataFrame
total_vendas = pd.DataFrame ({

    "Produto": ["Smartphone", "Carregador", "Capinha", "Caixa de som", "Controle PS5"],
    "Quantidade vendida": [31, 23, 68, 46, 17],
    "Valor Venda": [899.90, 39.90, 23.90, 133.90, 499.90],
    "Data Venda": ["2025/01/01", "2025/01/04", "2025/03/23", "2025/03/11", "2025/05/04"]

})

#Salvando em CSV
total_vendas.to_csv("arquivos_projetos/total_vendas.csv", index = False)

#Lendo Data Frame
vendas = pd.read_csv("arquivos_projetos/total_vendas.csv")

#Calculando faturamento total
faturamento_total = (vendas["Quantidade vendida"] * vendas["Valor Venda"]).sum()
display(f"Faturamento total R${faturamento_total}")

#Encontrando o produto mais vendido em quantidade
mais_vendido = vendas.groupby("Produto")["Quantidade vendida"].sum().idxmax()
print(f"Mais Vendido: {mais_vendido}")

#Encontrando a receita total por mês
vendas["Data Venda"] = pd.to_datetime(vendas["Data Venda"])
vendas["Faturamento"] = vendas["Quantidade vendida"] * vendas["Valor Venda"]
receita_mensal = vendas.groupby(vendas["Data Venda"].dt.month)["Faturamento"].sum()
print(receita_mensal)
