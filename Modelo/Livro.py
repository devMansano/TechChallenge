from pydantic import BaseModel

class Book(BaseModel): # Modelo de dados para representar um livro extraído
    Id: int
    title: str
    price: str
    availability: str
    rating: str
    url: str
    image_url: str
    category: str
