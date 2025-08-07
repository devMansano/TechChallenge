from fastapi import APIRouter
from Scrapping.Scrap import get_all_categories

router = APIRouter(prefix="/categories", tags=["Categorias"]) # Cria um roteador com prefixo /categories e a tag "Categorias" para documentação no Swagger

@router.get("/", summary="Listar todas as categorias") # Define o endpoint GET /categories/
def list_categories():
    categories = get_all_categories() # Chama a função que retorna todas as categorias extraídas do site
    return {"categories": categories} # Retorna o resultado em formato JSON
