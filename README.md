# calculadora_de_vendas
Aplicação desktop em Python com CustomTkinter para cálculo de preço de venda. Permite informar custo de compra, ICMS, quantidade, margem de lucro e custos adicionais opcionais, com formatação automática de valores, navegação por Enter e exibição clara do preço final em interface moderna e intuitiva.

# 📊 Calculadora de Preço de Venda

Aplicação desktop desenvolvida em **Python** utilizando **CustomTkinter**, focada no cálculo de preço de venda de produtos de forma simples, rápida e visualmente agradável. Ideal para estudantes, pequenos empreendedores e profissionais que precisam definir preços considerando custos, impostos e margem de lucro.

---

## 🧠 Objetivo do Projeto

O objetivo deste projeto é facilitar o cálculo do preço de venda unitário, evitando erros comuns ao precificar produtos e oferecendo uma interface intuitiva, moderna e funcional.

---

## 🚀 Funcionalidades

* Interface gráfica moderna com **modo escuro**
* Cálculo automático do **preço de venda unitário**
* Campos para:

  * Nome do produto
  * Preço de compra
  * Valor do ICMS
  * Quantidade
  * Margem de lucro (%)
  * Outros custos (opcional)
* Opção de **exibir ou ocultar custos adicionais**
* Formatação automática de valores monetários (R$) em tempo real
* Navegação entre campos usando a tecla **Enter**
* Cálculo automático ao pressionar Enter no último campo
* Validação de campos numéricos
* Tela de resultado com destaque visual:

  * Custos exibidos em vermelho
  * Margem e preço final exibidos em verde
* Tratamento de erros para evitar cálculos inválidos

---

## 🖥️ Interface

A interface foi construída com **CustomTkinter**, oferecendo:

* Layout limpo e organizado
* Melhor experiência visual em comparação ao Tkinter padrão
* Componentes modernos e responsivos

---

## 🛠 Tecnologias Utilizadas

* **Python 3**
* **CustomTkinter**
* **Tkinter**
* **Regex (expressões regulares)** para validações e formatação

---

## 📦 Requisitos

Antes de executar o projeto, certifique-se de ter instalado:

* Python 3.8 ou superior
* Biblioteca CustomTkinter

Instalação da dependência:

```bash
pip install customtkinter
```

---

## ▶️ Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Acesse a pasta do projeto:

```bash
cd seu-repositorio
```

3. Execute o arquivo principal:

```bash
python app.py
```

---

## 📐 Lógica de Cálculo

O cálculo do preço de venda é feito da seguinte forma:

1. Soma dos custos totais:

   * Preço de compra
   * ICMS
   * Outros custos (se houver)

2. Cálculo do custo unitário:

```
(custo_total) / quantidade
```

3. Aplicação da margem de lucro:

```
preço_final = custo_unitário * (1 + margem / 100)
```

---

## 🎯 Público-Alvo

* Pequenos empreendedores
* Estudantes de Sistemas de Informação, Administração ou áreas afins
* Profissionais de vendas e precificação
* Pessoas que desejam praticar Python com interface gráfica

---

## 📌 Possíveis Melhorias Futuras

* Exportação do resultado em PDF ou Excel
* Histórico de cálculos
* Cadastro de produtos
* Suporte a outros impostos
* Versão instalável (.exe)

---

## 📄 Licença

Este projeto é livre para uso e estudo. Sinta-se à vontade para modificar, melhorar e compartilhar.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Caso queira melhorar o projeto, abra uma issue ou envie um pull request.

---

Desenvolvido com 💙 em Python
