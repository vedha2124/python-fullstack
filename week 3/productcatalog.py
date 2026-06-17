from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Product Catalog API")
class ProductIn(BaseModel):
    name: str
    category: str
    price: float

class PriceUpdate(BaseModel):
    price: float          
products = []

def get_next_id():
    highest = 0
    for product in products:
        if product["id"] > highest:
            highest = product["id"]
    return highest + 1

@app.get("/")
def home():
    return {"message": "Welcome! Open /docs to try the API."}

@app.post("/products")
def add_product(product: ProductIn):
    new_product = {
        "id": get_next_id(),
        "name": product.name,
        "category": product.category,
        "price": product.price,
    }
    products.append(new_product)
    return new_product

@app.get("/products")
def list_products(search: str = None, category: str = None):
    result = []
    for product in products:
        if search is not None and search.lower() not in product["name"].lower():
            continue
        if category is not None and product["category"].lower() != category.lower():
            continue
        result.append(product)
    return result

@app.put("/products/{product_id}/price")
def update_price(product_id: int, new_price: PriceUpdate):
    for product in products:
        if product["id"] == product_id:
            product["price"] = new_price.price
            return product
    raise HTTPException(status_code=404, detail="Product not found")


@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            return {"message": "Product deleted"}
    raise HTTPException(status_code=404, detail="Product not found")