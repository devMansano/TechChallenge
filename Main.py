from fastapi import FastAPI
from Rota import book, categorias
from Scrapping.Scrap import get_all_categories, extract_books_from_category
import pandas as pd
from typing import List

app = FastAPI(title="Books to Scrape API", version="1.0")
books = pd.read_csv("books_complete.csv")

# Inclui os endpoints das rotas
app.include_router(categorias.router)
app.include_router(book.router)

@app.get("/")
def root():
    return {"message": "Bem-vindo à API de Livros!"}

# Endpoint para listar os livros
@app.get("/Books", response_model=List[extract_books_from_category])
def get_livros():
    return books.to_dict(orient="records") 

@app.get("/BuscarLivro")
def buscar_livros():
    print("oi")

@app.get("/export", summary="Exporta todos os livros para CSV")
def export_csv():
    categorias = get_all_categories()
    all_books = []

    for cat in categorias:
        all_books.extend(extract_books_from_category(cat["name"], cat["url"]))

    df = pd.DataFrame(all_books)
    df.to_csv("books_complete.csv", index=False, encoding='utf-8-sig')

    return {"message": f"Exportado com sucesso. Total: {len(df)} livros"}
