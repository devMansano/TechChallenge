from fastapi import FastAPI
from Rota import book, categorias, bem_vindo, conexao
from Modelo.Livro import Book
import uvicorn
from Scrapping.gera_base import banco_dados

#banco_dados()
# Inicializa a API
# Documentação Swagger
app = FastAPI(
    title="API para Consulta de Livros no Site http://books.toscrape.com/",
    description="""
        API para consulta e atualização dos livros a partir de um site e criação de um banco de dados em .CSV.
        Essa API foi desenvolvida para demonstrar o fluxo completo de integração entre cientistas de dados, banco de dados e retorno via API.
    """,
    version="2.1.0",
    contact={
        "name": "Equipe de Desenvolvimento",
        "email": "diogo@teste.com; matheus@teste.com; paulo@teste.com",
        "url": "https://github.com/devMansano/TechChallenge/tree/main"
    }
)

# Inclui os endpoints das rotas
app.include_router(categorias.router)
app.include_router(book.router)
app.include_router(bem_vindo.router)
app.include_router(conexao.router)

"""


# GET /api/v1/books/search?title={title}&category={category}: Busca livros por título e/ou categoria
# Endpoint de busca com filtros
@app.get("/api/v1/search", summary="Busca Livro e/ou Categoria", description="Realiza uma busca no site pelo nome do livro e/ou Categoria. É possível busar de forma independente ou utilizar ambas as informações.", response_model=List[Book])
def search_books(
    title: Optional[str] = Query(None),
    category: Optional[str] = Query(None)
):
    filtered_books = books

    if title:
        filtered_books = filtered_books[
            filtered_books['title'].str.contains(title, case=False, na=False)
        ]

    if category:
        filtered_books = filtered_books[
            filtered_books['category'].str.contains(category, case=False, na=False)
        ]

    return filtered_books.to_dict(orient="records")

# GET /api/v1/categories: Lista todas as categorias de livros disponíveis
@app.get("/api/v1/categories", summary="Categorias", description="Retorna todas as categorias de livros disponíveis no site.")
def listar_categorias(): 
    df = pd.read_csv(CSV)
    
    categorias = df["category"].dropna().unique().tolist()
    categorias.sort()

    return {"categorias": categorias}


"""
        
# Inicia o servidor da API com uvicorn
if __name__ == "__main__":
    uvicorn.run("Main:app", host="127.0.0.1", port=8000, reload=True)