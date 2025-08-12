from fastapi import APIRouter, Query
from typing import Optional
from Dados.gera_base import banco_dados
from typing import List, Optional
from Dados.modelo import Tipagem
from Dados.gera_base import banco_dados

listar = banco_dados()  # Retorna dados dos livros do BD

router = APIRouter(prefix="/api/v1/busca", tags=["Buscar por Título ou Categoria"])

# GET /api/v1/books/search?title={title}&category={category}: Busca livros por título e/ou categoria
# Endpoint de busca com filtros
@router.get("/", summary="Busca Livro e/ou Categoria", description="Realiza uma busca no site pelo nome do livro e/ou Categoria. É possível busar de forma independente ou utilizar ambas as informações.", response_model=List[Tipagem])
def busca_livros(
    titulo: Optional[str] = Query(None),
    categoria: Optional[str] = Query(None)
):
    livros_filtrados = listar

    if titulo or categoria:
        mascara = False
        if titulo:
            mascara |= livros_filtrados['title'].str.contains(titulo, case=False, na=False)
        if categoria:
            mascara |= livros_filtrados['category'].str.contains(categoria, case=False, na=False)
        livros_filtrados = livros_filtrados[mascara]

    return livros_filtrados.to_dict(orient="records")

