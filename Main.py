from fastapi import FastAPI
from Rota import bem_vindo, conexao, id, listar_categorias, listar_livros, titulo_categoria
import uvicorn
from Dados.gera_base import banco_dados

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
app.include_router(bem_vindo.router)
app.include_router(listar_livros.router)
app.include_router(id.router)
app.include_router(listar_categorias.router)
app.include_router(titulo_categoria.router)
app.include_router(conexao.router)
        
# Inicia o servidor da API com uvicorn
if __name__ == "__main__":
    uvicorn.run("Main:app", host="0.0.0.0", port=8000, reload=True)