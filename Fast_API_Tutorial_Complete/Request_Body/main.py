from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

class Item(BaseModel):
    name: str
    description: str | None
    price: float
    tax : float | None
    
@app.post("/items/")
async def create_item(item: Item):
    items = item.dict()
    if item.tax:
        price_tax = item.price + item.tax
        items.update({"Price_tax": price_tax})
    return items

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item,q :str |None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result