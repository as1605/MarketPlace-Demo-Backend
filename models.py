from pydantic import BaseModel


class Product(BaseModel):
    title: str
    category: str
    price: int
    location: str
    description: str
    isNegotiable: bool
