from fastapi import APIRouter
from Scrapping.Scrap import get_all_categories

router = APIRouter(prefix="/categories", tags=["Categorias"])

@router.get("/", summary="Listar todas as categorias")
def list_categories():
    categories = get_all_categories()
    return {"categories": categories}
