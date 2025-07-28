from fastapi import APIRouter, Query
from typing import Optional
from Scrapping.Scrap import get_all_categories, extract_books_from_category
import pandas as pd

router = APIRouter(prefix="/books", tags=["Livros"])

@router.get("/", summary="Listar livros", description="Lista livros por categoria ou todos")
def list_books(category: Optional[str] = Query(None, description="Nome da categoria para filtrar")):
    categories = get_all_categories()
    books = []

    for cat in categories:
        name = cat["name"]
        link = cat["url"]

        if category and category.lower() != name.lower():
            continue

        books.extend(extract_books_from_category(name, link))

        if category:
            break

    return {"total": len(books), "books": books}

def export_csv():
    categorias = get_all_categories()
    all_books = []

    for cat in categorias:
        all_books.extend(extract_books_from_category(cat["name"], cat["url"]))

    df = pd.DataFrame(all_books)
    df.to_csv("books_complete.csv", index=False, encoding='utf-8-sig')
    return {"message": f"Exportado com sucesso. Total: {len(df)} livros"}