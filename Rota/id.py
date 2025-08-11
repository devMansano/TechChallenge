from fastapi import APIRouter
from Dados.gera_base import banco_dados

router = APIRouter(prefix="/api/v1/id", tags=["Busca por Identificador"])

df = banco_dados()  # agora df é um DataFrame

# GET /api/v1/id/{id}: Retorna detalhes completos de um livro específico pelo ID.
@router.get("/{Id}", summary="Busca por ID", description="Retorna detalhes completos de um livro específico pelo ID.")
def buscar_ID(Id: int):
    livro = df[df["Id"] == Id]
    
    if livro.empty:
        return {"message": "Livro não encontrado"}
    
    return livro.iloc[0].to_dict()
