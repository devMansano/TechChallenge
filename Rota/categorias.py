from fastapi import APIRouter
from Dados.Scrap import get_all_categories
import pandas as pd
from Dados.gera_base import banco_dados

listar = banco_dados()  # Retorna dados dos livros do BD
router = APIRouter(prefix="/api/v1/categorias", tags=["Categorias"])

# GET /api/v1/categories: Lista todas as categorias de livros disponíveis
@router.get("/", summary="Categorias", description="Retorna todas as categorias de livros disponíveis no site.")
def listar_categorias(): 
    df = listar
    categorias = df["category"].dropna().unique().tolist()
    categorias.sort()

    return {"categorias": categorias}