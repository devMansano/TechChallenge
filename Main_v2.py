from fastapi import FastAPI
from Rota import book, categorias
from Scrapping.Scrap import get_all_categories, extract_books_from_category
from Modelo.Livro import Book
import pandas as pd
from typing import List
import os
import uvicorn
from pydantic import BaseModel
from typing import Optional

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
app = FastAPI(title="Books to Scrape API", version="1.0")

# Inclui os endpoints das rotas
app.include_router(categorias.router)
app.include_router(book.router)

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
class BookSearchRequest(BaseModel):
    # Id: Optional[int] = None
    title: Optional[str] = None
    category: Optional[str] = None

@app.get("/api/v1/search", summary="Buscar livros por título e/ou categoria via JSON")
def buscar_livros_json(request: BookSearchRequest):
    df = pd.read_csv(CSV)

    # Filtra por título, se fornecido
    if request.title:
        df = df[df["title"].str.contains(request.title, case=False, na=False)]

    # Filtra por categoria, se fornecida
    if request.category:
        df = df[df["category"].str.contains(request.category, case=False, na=False)]

    # if df.empty:
    #     return {"message": "Nenhum livro encontrado com os critérios fornecidos"}

    return df.to_dict(orient="records")


# • GET /api/v1/categories: Lista todas as categorias de livros disponíveis
@app.get("/api/v1/categories", summary="Listar categorias disponíveis no CSV")
def listar_categorias():
    df = pd.read_csv(CSV)
    
    categorias = df["category"].dropna().unique().tolist()
    categorias.sort()

    return {"categorias": categorias}






if __name__ == "__main__":
    uvicorn.run("Main:app", host="0.0.0.0", port=8000, reload=True)
