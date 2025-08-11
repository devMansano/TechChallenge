from fastapi import APIRouter, HTTPException
import time
from Dados.gera_base import banco_dados

listar = banco_dados()  # Retorna dados dos livros do BD

router = APIRouter(prefix="/api/v1/conexao", tags=["Conexão"])

# GET /api/v1/health: Verifica status da API e conectividade com os dados.
@router.get("/", summary="Conexão", description="Retorna o Status atual da conexão com a base de dados.")
def health():
    start = time.time() # Marca o início da execução para calcular o tempo de resposta
    try:
        
        if listar is None or listar.empty: # Verifica se o DataFrame 'books' está carregado e não está vazio
            raise HTTPException(status_code=500, detail="Dados não estão disponíveis")

        response_time = time.time() - start # Calcula o tempo de resposta em milissegundos
        
        return { # Retorna o status da API com tempo de resposta
            
            "status": "ok",
            "message": "API ativa e dados carregados",
            "response_time_ms": int(response_time * 1000)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao acessar dados: {str(e)}") # Em caso de erro, retorna uma exceção HTTP com status 500