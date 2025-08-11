from fastapi import APIRouter, Query

router = APIRouter(prefix="", tags=["Bem-vindo"])

# EndPoint inicial da API para recebimento de usuários
@router.get("/", summary="Bem-vindo")
def root():
    return {"message": "Bem-vindo a API de Livros!"}
