from fastapi import FastAPI,Query,HTTPException
from Rota import book, categorias
from Scrapping.Scrap import get_all_categories, extract_books_from_category
from Modelo.Livro import Book
from pydantic import BaseModel
from typing import List, Optional
import os
import uvicorn
import time
import pandas as pd

CSV = "books_complete.csv"

# Verifica se o CSV existe. Se não, faz scraping e cria o arquivo.
if os.path.exists(CSV):
    books = pd.read_csv(CSV)
else:
    categorias_list = get_all_categories()
    all_books = []
    IDrecorrente = 0
    for cat in categorias_list:
        livros, IDrecorrente = extract_books_from_category(cat["name"], cat["url"], IDrecorrente)
        all_books.extend(livros)
    df = pd.DataFrame(all_books)
    df.to_csv(CSV, index=False, encoding='utf-8-sig')
    books = df

# Inicializa a API
# Documentação Swagger
app = FastAPI(
    title="API para Consulta de Livros no Site http://books.toscrape.com/",
    description="""
        API para consulta e atualização dos livros a partir de um site e criação 
        de um banco de dados em .CSV.
        Essa API foi desenvolvida para demonstrar o fluxo completo de integração
        entre cientistas de dados, banco de dados e retorno via API.
    """,
    version="2.1.0",
    contact={
        "name": "Equipe de Desenvolvimento",
        "email": "diogo@empresa.com; matheus@empresa.com; paulo@empresa.com",
        "url": "https://github.com/devMansano/TechChallenge/tree/main"
    },
    license_info={  # Opcional
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    }
)

#app = FastAPI(title="Books to Scrape API", version="1.0")

# Inclui os endpoints das rotas
app.include_router(categorias.router)
app.include_router(book.router)

# EndPoint inicial da API para recebimento de usuários
@app.get("/")
def root():
    return {"message": "Bem-vindo à API de Livros!"}


# GET /api/v1/books: Lista todos os livros disponíveis na base de dados.
@app.get("/api/v1/books", response_model=List[Book])
def get_livros():
    return books.to_dict(orient="records")


# GET /api/v1/books/{id}: Retorna detalhes completos de um livro específico pelo ID.
@app.get("/api/v1/books/{Id}", summary="Obter detalhes de um livro por ID")
def buscar_ID(Id: int):
    livro = books[books["Id"] == Id]
    
    if livro.empty:
        return {"message": "Livro não encontrado"}
    
    return livro.iloc[0].to_dict()


# GET /api/v1/books/search?title={title}&category={category}: Busca livros por título e/ou categoria
# Endpoint de busca com filtros
@app.get("/api/v1/search", response_model=List[Book])
def search_books(
    title: Optional[str] = Query(None),
    category: Optional[str] = Query(None)
):
    filtered_books = books

    if title:
        filtered_books = filtered_books[
            filtered_books['title'].str.contains(title, case=False, na=False)
        ]

    if category:
        filtered_books = filtered_books[
            filtered_books['category'].str.contains(category, case=False, na=False)
        ]

    return filtered_books.to_dict(orient="records")

# GET /api/v1/categories: Lista todas as categorias de livros disponíveis
@app.get("/api/v1/categories", summary="Listar categorias disponíveis no CSV")
def listar_categorias(): 
    df = pd.read_csv(CSV)
    
    categorias = df["category"].dropna().unique().tolist()
    categorias.sort()

    return {"categorias": categorias}


# GET /api/v1/health: Verifica status da API e conectividade com os dados.
@app.get("/api/v1/health")
def health():
    start = time.time() # Marca o início da execução para calcular o tempo de resposta
    try:
        
        if books is None or books.empty: # Verifica se o DataFrame 'books' está carregado e não está vazio
            raise HTTPException(status_code=500, detail="Dados não estão disponíveis")

        response_time = time.time() - start # Calcula o tempo de resposta em milissegundos
        
        return { # Retorna o status da API com tempo de resposta
            
            "status": "ok",
            "message": "API ativa e dados carregados",
            "response_time_ms": int(response_time * 1000)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao acessar dados: {str(e)}") # Em caso de erro, retorna uma exceção HTTP com status 500


# Inicia o servidor da API com uvicorn
if __name__ == "__main__":
    uvicorn.run("Main:app", host="127.0.0.1", port=8000, reload=True)