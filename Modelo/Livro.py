from pydantic import BaseModel

# Criação de classe para validação do tipo de dados
class Book(BaseModel):
    Id: int             # ID do livro
    title: str          # Título do livro
    price: str          # Preço
    availability: str   # Disponibilidade
    rating: str         # Avaliação
    url: str            # URL para detalhes do livro
    image_url: str      # URL da imagem da capa
    category: str       # Categoria do livro
