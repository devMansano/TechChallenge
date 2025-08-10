from fastapi import APIRouter, Query

router = APIRouter(prefix="/api/v1/id/{Id}", tags=["Bem-Vindo"])

# GET /api/v1/id/{id}: Retorna detalhes completos de um livro específico pelo ID.
@router.get("/", summary="Busca por ID", description="Retorna detalhes completos de um livro específico pelo ID.")
def buscar_ID(Id: int):
    livro = books[books["Id"] == Id]
    
    if livro.empty:
        return {"message": "Livro não encontrado"}
    
    return livro.iloc[0].to_dict()
