from fastapi import APIRouter, Query
from typing import Optional
from Dados.Scrap import get_all_categories, extract_books_from_category
from Dados.gera_base import banco_dados
from pydantic import BaseModel
from typing import List, Optional
from Modelo.Livro import Book

listar = banco_dados()  # Retorna dados dos livros do BD

router = APIRouter(prefix="/books", tags=["Livros"])

# GET /api/v1/books: Lista todos os livros disponíveis na base de dados.
@router.get("/api/v1/books", summary="Livros", description="Exibe todos os Livros do Site.", response_model=List[Book])
def get_livros():
    return listar.to_dict(orient="records")