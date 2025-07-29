from pydantic import BaseModel

class Book(BaseModel):
    Id: int
    title: str
    price: str
    availability: str
    rating: str
    url: str
    image_url: str
    category: str
