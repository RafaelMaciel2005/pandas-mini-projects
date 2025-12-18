"""
1 - gere um DataFrame com informações de funcionários contendo:
        - nome
        -departamento
        -idade
        -salário

2 - Salve esse DataFrame em um arquivo CSV dentro da pasta data/.

3 - Leia o arquivo CSV usando Pandas.

    Calcule:

        O salário médio por departamento

        O funcionário com o maior salário

        A idade média dos funcionários
"""
import pandas as pd
from IPython.display import display

#criando DataFrame
funcionarios = pd.DataFrame({

    "Nome": ["Rafael", "Ronney", "Denira", "Leoni"],
    "Departamento": ["Financeiro", "RH", "Gerente", "Vendedor"],
    "Idade": [20, 30, 53, 66],
    "Salário": [5500.00, 4290.00, 7640.00, 3200.00]

})

#salvando em CSV
funcionarios.to_csv("arquivos_projetos/funcionarios.csv", index = False)