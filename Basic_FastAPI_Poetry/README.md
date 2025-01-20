# FastAPI Project with Poetry

## Overview
This project demonstrates a simple API built with FastAPI, using Poetry as the dependency and project manager. The API provides basic CRUD operations for managing items in a mock database.

## Features
- **GET**: Retrieve all items or a specific item by ID.
- **POST**: Add a new item to the database.
- **PUT**: Update an existing item by ID.
- **DELETE**: Remove an item by ID.

## Prerequisites
Ensure the following are installed on your system:
- Python 3.7+
- [Poetry](https://python-poetry.org/): Dependency management and packaging tool.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

## Running the Application

1. Start the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

2. Open your browser and navigate to the following URL to access the interactive API documentation:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## API Endpoints

### 1. Root Endpoint
- **URL**: `/`
- **Method**: `GET`
- **Description**: Welcome message.
- **Response**:
  ```json
  {
    "message": "Welcome to FastAPI!"
  }
  ```

### 2. Get All Items
- **URL**: `/get_items`
- **Method**: `GET`
- **Response Model**: List of items.
- **Response**:
  ```json
  [
    {
      "name": "Item1",
      "price": 100,
      "quantity": 10
    },
    {
      "name": "Item2",
      "price": 200,
      "quantity": 5
    }
  ]
  ```

### 3. Get Item by ID
- **URL**: `/items/{item_id}`
- **Method**: `GET`
- **Response Model**: Single item.
- **Response**:
  ```json
  {
    "name": "Item1",
    "price": 100,
    "quantity": 10
  }
  ```
- **Error Response**:
  ```json
  {
    "message": "Item not found"
  }
  ```

### 4. Create an Item
- **URL**: `/items`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "name": "NewItem",
    "price": 300,
    "quantity": 15
  }
  ```
- **Response**:
  ```json
  {
    "name": "NewItem",
    "price": 300,
    "quantity": 15
  }
  ```

### 5. Update an Item
- **URL**: `/items/{item_id}`
- **Method**: `PUT`
- **Request Body**:
  ```json
  {
    "name": "UpdatedItem",
    "price": 400,
    "quantity": 20
  }
  ```
- **Response**:
  ```json
  {
    "name": "UpdatedItem",
    "price": 400,
    "quantity": 20
  }
  ```
- **Error Response**:
  ```json
  {
    "detail": "Item not found"
  }
  ```

### 6. Delete an Item
- **URL**: `/items/{item_id}`
- **Method**: `DELETE`
- **Response**:
  ```json
  {
    "message": "Item 1 deleted successfully",
    "deleted_item": {
      "name": "Item1",
      "price": 100,
      "quantity": 10
    }
  }
  ```
- **Error Response**:
  ```json
  {
    "detail": "Item not found"
  }
  ```

## Project Structure
```
project_name/
├── main.py          # FastAPI application code
├── pyproject.toml   # Poetry configuration file
├── README.md        # Project documentation
```

## Managing Dependencies

- Add a new dependency:
  ```bash
  poetry add <package_name>
  ```

- Add a development dependency:
  ```bash
  poetry add --dev <package_name>
  ```

- Update dependencies:
  ```bash
  poetry update
  ```

## Testing
You can write tests using `pytest`.

1. Install `pytest`:
   ```bash
   poetry add --dev pytest
   ```

2. Run tests:
   ```bash
   pytest
   ```

## Deployment
FastAPI applications can be deployed using Uvicorn, Docker, or any cloud provider. For production, use a robust ASGI server like Daphne or Uvicorn behind a reverse proxy like Nginx.


