from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, status

class Product(BaseModel):
    id: int
    name: str
    price: float

products = []

app = FastAPI()

@app.post("/products", status_code = 201)
def create_products(product: Product):
    products.append(product)
    return product

@app.get("/products")
def get_products():
    return products

@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="product not found")

@app.put("/products/{product_id}")
def update_product(product_id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product.id == product_id:
            products[index] = updated_product
            return updated_product
        
    raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product.id == product_id:
            products.remove(product)
            return {"message": "Product deleted successfully"}
        
    raise HTTPException(status_code=404, detail="Product not found")

