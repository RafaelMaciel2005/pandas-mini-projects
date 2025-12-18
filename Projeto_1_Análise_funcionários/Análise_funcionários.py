import pandas as pd
from IPython.display import display

#criando DataFrame.
funcionarios = pd.DataFrame({

    "Nome": ["Rafael", "Ronney", "Denira", "Leoni"],
    "Departamento": ["Financeiro", "RH", "Gerente", "Financeiro"],
    "Idade": [20, 30, 53, 66],
    "Salário": [5500.00, 4290.00, 7640.00, 3200.00]

})

#salvando em CSV.
funcionarios.to_csv("arquivos_projetos/funcionarios.csv", index = False)

#lendo o DataFrame.
func = pd.read_csv("arquivos_projetos/funcionarios.csv")

#Calculando a média de cada departamento.
media_dep = func.groupby("Departamento")["Salário"].mean()
display(f"média salarial por departamento: {media_dep}:")

#O funcionário com o maior salário.
func_maior_salario = func.loc[func["Salário"].idxmax()]
display(f"Maior Salário: {func_maior_salario}")

#Descobrindo a idade media dos funcionarios.
idade_media_funcionarios = func["Idade"].mean()
display(f"Idade media dos funcionarios: {idade_media_funcionarios}")