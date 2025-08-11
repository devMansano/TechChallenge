# 📚 TechChallenge - API para Consulta de Livros

![FastAPI](https://img.shields.io/badge/FastAPI-v2.1.0-green)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Status](https://img.shields.io/badge/status-active-brightgreen)

---

## 🔎 Sobre o Projeto

Esta API, construída com **FastAPI**, realiza web scraping no site [Books to Scrape](http://books.toscrape.com/) para coletar dados de livros, armazená-los localmente em um arquivo `.csv` e disponibilizá-los via endpoints REST.

O objetivo principal é demonstrar o fluxo completo de integração entre coleta de dados (scraping), manipulação e armazenamento, e disponibilização via API para consumo por cientistas de dados, desenvolvedores e demais interessados.

---

## ⚙️ Funcionalidades

- 📖 Listar todos os livros ou filtrá-los por categoria.
- 🔍 Buscar livros por título e/ou categoria.
- 🏷️ Listar todas as categorias disponíveis.
- 🆔 Consultar um livro pelo seu ID único.
- 🩺 Verificar o status da API e conectividade com o banco de dados.
- 💾 Exportar dados completos para CSV (via geração automática no backend).

## ⚙️ Requisitos

- Python 3.11+
- Git (opcional, para clonar o repositório)

## 🛠 Tecnologias Utilizadas

| Tecnologia      | Descrição                              |
|-----------------|--------------------------------------|
| FastAPI         | Framework web moderno e rápido       |
| Requests        | Requisições HTTP para scraping       |
| BeautifulSoup4  | Extração de dados HTML                |
| Pandas          | Manipulação e exportação de dados    |
| Uvicorn         | Servidor ASGI para execução da API   |
| Pydantic        | Validação de modelos e dados         |


---

## 📥 Instalação e Execução

- **Clonar o repositório e entrar no diretório:**
```bash
git clone https://github.com/devMansano/TechChallenge.git
cd TechChallenge

```

## 📁 Estrutura do Projeto

```plaintext
TechChallenge/
├── Main.py                # Arquivo principal que inicia a API FastAPI
├── requirements.txt       # Dependências do projeto
├── books_complete.csv     # Banco de dados local gerado via scraping
├── Scrapping/             # Módulo responsável pelo scraping e geração do CSV
│   ├── Scrap.py           # Funções para extrair categorias e livros do site
│   └── gera_base.py       # Criação e leitura do CSV com os dados coletados
├── Rota/                  # Endpoints da API organizados em módulos
│   ├── bem_vindo.py       # Rota raiz com mensagem de boas-vindas
│   ├── book.py            # Rota para listagem geral de livros
│   ├── categorias.py      # Rota para listar categorias disponíveis
│   ├── conexao.py         # Endpoint para checar saúde da API / status da base
│   └── id.py              # Busca de livro pelo ID
├── Modelo/                # Modelos Pydantic para validação de dados
│   └── Livro.py           # Definição do modelo Book
└── README.md              # Documentação do projeto (este arquivo)

- **🚀 Funcionalidades
- 📖 Listar livros por categoria ou todos os disponíveis.
- 🔍 Buscar livros por título e/ou categoria.
- 🏷️ Listar categorias disponíveis no site.
- 🆔 Consultar livro por ID.
- 💾 Exportar todos os livros para CSV.
- 🩺 Verificar status de saúde da API.


**🛠️ Tecnologias Utilizadas**
- FastAPI — Framework web rápido e moderno.
- Requests — Requisições HTTP.
- BeautifulSoup4 — Extração de dados HTML.
- Pandas — Manipulação e exportação de dados.


**📌 Endpoints Principais**
Método	Endpoint	Descrição

- GET	/	--> Mensagem de boas-vindas
- GET	/categories	--> Lista todas as categorias
- GET	/books -->	Lista todos os livros (ou filtra por categoria)
- GET	/api/v1/id/{Id} -->	Busca livro por ID
- GET	/api/v1/search?title=&category -->	Busca por título e/ou categoria
- GET	/api/v1/health -->	Verifica status da API


**📤 Exportar para CSV**
- A função export_csv() em Rota/Book.py coleta todos os livros do site e exporta para o arquivo books_complete.csv:


Repositório GitHub:
https://github.com/devMansano/TechChallenge

**📄 Licença**
- Este projeto é apenas para fins educacionais.
O site Books to Scrape é destinado a práticas de web scraping e não contém dados reais.