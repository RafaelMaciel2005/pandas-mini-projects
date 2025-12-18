# 📦 Controle de Estoque com Pandas

## 📌 Descrição do Projeto

Este projeto tem como objetivo simular um **controle básico de estoque** utilizando a biblioteca **Pandas (Python)**. Ele foi desenvolvido com foco em **análise de dados**, aplicando regras simples de negócio para identificar produtos que precisam de reposição e gerar um arquivo final em formato **CSV**.

---

## 🎯 Objetivos

* Criar um DataFrame representando o estoque de produtos
* Calcular o **valor total em estoque** por produto
* Identificar produtos com **estoque abaixo do mínimo**
* Criar uma coluna de **status de reposição**
* Exportar os dados tratados para um arquivo **CSV**

---

## 🧠 Regra de Negócio

* Estoque mínimo definido: **10 unidades**
* Produtos com quantidade menor que o mínimo recebem o status **REPOR**
* Produtos com quantidade igual ou superior recebem o status **OK**

---

## 🛠 Tecnologias Utilizadas

* **Python 3**
* **Pandas**