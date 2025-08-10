from fastapi import FastAPI,Query,HTTPException
from Rota import book, categorias, bem_vindo
from Modelo.Livro import Book
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import time

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

"""
# GET /api/v1/books: Lista todos os livros disponíveis na base de dados.
@app.get("/api/v1/books", summary="Livros", description="Exibe todos os Livros do Site.", response_model=List[Book])
def get_livros():
    return books.to_dict(orient="records")

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


# GET /api/v1/health: Verifica status da API e conectividade com os dados.
@app.get("/api/v1/health", summary="Conexão", description="Retorna o Status atual da conexão com a base de dados.")
def health():
    start = time.time() # Marca o início da execução para calcular o tempo de resposta
    try:
        
        if books is None or books.empty: # Verifica se o DataFrame 'books' está carregado e não está vazio
            raise HTTPException(status_code=500, detail="Dados não estão disponíveis")

        response_time = time.time() - start # Calcula o tempo de resposta em milissegundos
        
        return { # Retorna o status da API com tempo de resposta
            
            "status": "ok",
            "message": "API ativa e dados carregados",
            "response_time_ms": int(response_time * 1000)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao acessar dados: {str(e)}") # Em caso de erro, retorna uma exceção HTTP com status 500
"""
        
# Inicia o servidor da API com uvicorn
if __name__ == "__main__":
    uvicorn.run("Main:app", host="127.0.0.1", port=8000, reload=True)