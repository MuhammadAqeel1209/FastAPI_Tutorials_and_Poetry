from fastapi import FastAPI
from enum import Enum
app = FastAPI()

@app.get("/users")
async def list_users():
    return {"message": "list users route"}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}

@app.get("/user/me")
async def get_user_latest():
    return {"message": "This is Current User"}

class FoodEnum(str,Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"
    
@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "you are healthy"}

    if food_name.value == "fruits":
        return {
            "food_name": food_name,
            "message": "you are still healthy, but like sweet things",
        }
    return {"food_name": food_name, "message": "i like chocolate milk"}