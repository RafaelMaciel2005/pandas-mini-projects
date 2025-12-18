import pandas as pd
from IPython.display import display


dados_estoque = pd.DataFrame({

    "Produto": ["Teclado", "Mouse", "Monitor", "HeadSet", "Webcam"],
    "Quantidade": [15, 8, 5, 20, 3],
    "Preco_Unitario": [120.00, 80.00, 900.00, 250.00, 300.00]

})

dados_estoque.to_csv("arquivos_projetos/dados_estoque.csv", index = False)