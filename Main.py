from fastapi import FastAPI
from Rota import book, categorias
from Scrapping.Scrap import get_all_categories, extract_books_from_category
from Modelo.Livro import Book
import pandas as pd
from typing import List
import os

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

@app.get("/api/v1/books", response_model=List[Book])
def get_livros():
    return books.to_dict(orient="records")

@app.get("/api/v1/books/{Id}", summary="Obter detalhes de um livro por ID")
def buscar_ID(Id: int):
    livro = books[books["Id"] == Id]
    
    if livro.empty:
        return {"message": "Livro não encontrado"}
    
    return livro.iloc[0].to_dict()
