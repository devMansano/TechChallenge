from fastapi import APIRouter
from Dados.gera_base import banco_dados
from typing import List 
from Dados.modelo import Tipagem

listar = banco_dados()  # Retorna dados dos livros do BD

router = APIRouter(prefix="/livros", tags=["Listar Livros"])

# GET /api/v1/books: Lista todos os livros disponíveis na base de dados.
@router.get("/api/v1/livros", summary="Livros", description="Exibe todos os Livros do Site.", response_model=List[Tipagem])
def get_livros():
    return listar.to_dict(orient="records")