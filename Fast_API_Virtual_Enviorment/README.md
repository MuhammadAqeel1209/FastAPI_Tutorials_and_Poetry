# FastAPI Basics and Beyond

This README covers the foundational aspects of FastAPI, from installation to working with API routes, Swagger documentation, and database interactions using SQLModel.

---

## FastAPI #1: Installation / API Routes / Swagger Docs

### Installation
To install FastAPI, use pip:
```bash
pip install fastapi[all]
```
You also need an ASGI server like `uvicorn`:
```bash
pip install uvicorn
```

### Create a Virtual Environment
To create a virtual environment named `venv-fastapi`, run the following command in your terminal:
```bash
python -m venv venv-fastapi
```

Activate the virtual environment:
- **Windows**:
  ```bash
  .\venv-fastapi\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source venv-fastapi/bin/activate
  ```

### API Routes
Create your first FastAPI app in `main.py`:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```
Run the server:
```bash
uvicorn main:app --reload
```
Access the API at `http://127.0.0.1:8000`.

### Swagger Docs
Interactive API documentation is auto-generated and available at `/docs`:
```
http://127.0.0.1:8000/docs
```
Alternative ReDoc documentation is available at `/redoc`:
```bash
http://127.0.0.1:8000/redoc
```

---

## FastAPI #2: Path Parameters / Data Validation with Type-Hints & Enums

### Path Parameters
Path parameters are part of the URL path. FastAPI automatically validates their types:
```python
@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}
```

### Data Validation with Type-Hints
FastAPI uses Python's type-hinting for validation:
```python
from typing import Optional

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
```

### Enums for Fixed Values
Enums ensure a set of allowed values:
```python
from enum import Enum

class ItemType(str, Enum):
    food = "food"
    drink = "drink"

@app.get("/items/{item_type}")
def get_item(item_type: ItemType):
    return {"item_type": item_type}
```

---

## FastAPI and Pydantic: Model Classes and Nested Models

### Pydantic Model Classes
Define models for request and response data validation:
```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: Optional[float] = None

@app.post("/items/") 
def create_item(item: Item):
    return item
```

### Nested Models
Models can be nested:
```python
class User(BaseModel):
    username: str
    email: str

class ItemWithUser(Item):
    owner: User

@app.post("/items-with-owner/")
def create_item_with_owner(item: ItemWithUser):
    return item
```

---

## FastAPI and Pydantic: URL Query Parameters for Filtering

### URL Query Parameters
Use query parameters for filtering:
```python
@app.get("/items/")
def get_items(q: Optional[str] = None, limit: int = 10):
    return {"query": q, "limit": limit}
```

---

## FastAPI: Request Body and POST Requests | Pydantic Pre-Validators

### Request Body
FastAPI allows complex request body validation:
```python
@app.post("/create-user/")
def create_user(user: User):
    return {"message": "User created successfully", "user": user}
```

### Pydantic Pre-Validators
Add preprocessing to models:
```python
from pydantic import Field, validator

class Product(BaseModel):
    name: str = Field(..., title="Product Name")
    price: float

    @validator("price")
    def check_price(cls, value):
        if value <= 0:
            raise ValueError("Price must be greater than 0")
        return value

@app.post("/create-product/")
def create_product(product: Product):
    return product
```

---

## FastAPI & SQLModel: Database Interaction in FastAPI Apps

### Installation
Install SQLModel:
```bash
pip install sqlmodel
```

### Database Models
Create models using SQLModel:
```python
from sqlmodel import SQLModel, Field

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int
```

### Database Session
Setup the database session:
```python
from sqlmodel import Session, create_engine

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SQLModel.metadata.create_all(engine)

@app.on_event("startup")
def startup_event():
    SQLModel.metadata.create_all(engine)
```

### CRUD Operations
```python
@app.post("/heroes/")
def create_hero(hero: Hero):
    with Session(engine) as session:
        session.add(hero)
        session.commit()
        session.refresh(hero)
        return hero

@app.get("/heroes/")
def read_heroes():
    with Session(engine) as session:
        heroes = session.query(Hero).all()
        return heroes
```

---

## Conclusion

This guide provides a comprehensive overview of using FastAPI with features like Pydantic models, validation, query parameters, and SQLModel for database interaction. Explore the FastAPI documentation for more advanced features!
```
