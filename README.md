# TechChallenge
# 📚 TechChallenge

API desenvolvida com **FastAPI** para consultar e exportar informações sobre livros disponíveis no site [Books to Scrape](http://books.toscrape.com/).  
O projeto realiza **web scraping** para coletar dados, armazena-os em um arquivo `.csv` e disponibiliza-os via **endpoints REST**.

---

## ⚙️ Requisitos

- **Python 3.11+**
- **Bibliotecas obrigatórias:**
  - `beautifulsoup4`
  - `pandas`
  - `fastapi`
  - `uvicorn`
  - `pydantic`
  - `requests`

---

## 📥 Instalação e Execução

- **Clonar o repositório e entrar no diretório:**
```bash
git clone https://github.com/devMansano/TechChallenge.git
cd TechChallenge

```


- **🚀 Funcionalidades**
- `📖 Listar livros por categoria ou todos os disponíveis.

- `🔍 Buscar livros por título e/ou categoria.

- `🏷️ Listar categorias disponíveis no site.

- `🆔 Consultar livro por ID.

- `💾 Exportar todos os livros para CSV.

- `🩺 Verificar status de saúde da API.

-**🛠️ Tecnologias Utilizadas**
FastAPI — Framework web rápido e moderno.

Requests — Requisições HTTP.

BeautifulSoup4 — Extração de dados HTML.

Pandas — Manipulação e exportação de dados.


-**📌 Endpoints Principais**
Método	Endpoint	Descrição

- `GET	/	--> Mensagem de boas-vindas

- `GET	/categories	--> Lista todas as categorias

- `GET	/books -->	Lista todos os livros (ou filtra por categoria)

- `GET	/api/v1/id/{Id} -->	Busca livro por ID

- `GET	/api/v1/search?title=&category -->	Busca por título e/ou categoria

- `GET	/api/v1/health -->	Verifica status da API


-**📤 Exportar para CSV**
- `A função export_csv() em Rota/Book.py coleta todos os livros do site e exporta para o arquivo books_complete.csv:


-**📄 Licença**
- `Este projeto é apenas para fins educacionais.
O site Books to Scrape é destinado a práticas de web scraping e não contém dados reais.