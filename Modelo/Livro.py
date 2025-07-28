from pydantic import BaseModel

class Book(BaseModel):
    title: str
    price: str
    availability: str
    rating: str
    url: str
    image_url: str
    category: str
