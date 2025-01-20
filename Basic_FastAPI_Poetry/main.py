from  fastapi import FastAPI
from pydantic import BaseModel
from typing import List
app = FastAPI()

#  Make Model 
class Items(BaseModel):
    name : str
    price : int
    quantity : int
    

# Mock Database
items = {}

@app.get("/")
def getData():
    return {"message": "Welcome to FastAPI!"}

@app.get("/get_items",response_model=List[Items])
def get_all_items():
    if not items:
        return []
    return list(items.values())

@app.get("/items/{item_id}",response_model=Items)
def get_item(item_id:int):
    if item_id not in items:
        return {"message": "Item not found"}
    return items[item_id]
    


@app.post("/items",response_model=Items)
def create_item(item: Items):
    item_id = len(items) + 1
    items[item_id] = item
    return  item

@app.put("/items/{item_id}",response_model=Items)
def update_item(item_id: int, updated_item: Items):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = updated_item
    return updated_item

@app.delete('/items/{item_id}',response_model=dict)
def delete_items(item_id : int):
    if not item_id in items:
        raise HTTPException(status_code=404, detail="Item not found")
    delete_item = items.pop(item_id)
    return {"message": f"Item {item_id} deleted successfully", "deleted_item": deleted_item}

