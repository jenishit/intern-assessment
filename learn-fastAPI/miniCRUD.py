from fastapi import FastAPI, status
from pydantic import BaseModel

app =FastAPI()

class Product(BaseModel):
    name: str
    price: float

products = []

@app.post("/products")
def create_product(product: Product):
    products.append(product)
    return product

@app.get("/products")
def get_products():
    return products

@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item():
    return {"message": "Item created"}