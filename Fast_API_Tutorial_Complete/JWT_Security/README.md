# FastAPI Authentication Example

This project demonstrates how to implement authentication in FastAPI using OAuth2 and JWT tokens.

## Features
- User authentication with hashed passwords
- JWT-based authentication
- Token-based access control
- Secured endpoints requiring authentication

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/fastapi-auth-example.git
   cd fastapi-auth-example
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install fastapi uvicorn passlib[bcrypt] python-jose
   ```

## Running the Application
Start the FastAPI server using Uvicorn:
```sh
uvicorn main:app --reload
```

## API Endpoints

### 1. Obtain Token
- **Endpoint:** `POST /token`
- **Description:** Authenticate a user and generate an access token.
- **Request:**
  ```sh
  curl -X POST "http://127.0.0.1:8000/token" \
       -H "Content-Type: application/x-www-form-urlencoded" \
       -d "username=johndoe&password=secret"
  ```
- **Response:**
  ```json
  {
    "access_token": "your_jwt_token",
    "token_type": "bearer"
  }
  ```

### 2. Get Current User
- **Endpoint:** `GET /users/me`
- **Description:** Retrieve the details of the authenticated user.
- **Request:**
  ```sh
  curl -X GET "http://127.0.0.1:8000/users/me" \
       -H "Authorization: Bearer your_jwt_token"
  ```

### 3. Get User Items
- **Endpoint:** `GET /users/me/items`
- **Description:** Retrieve the user's items (requires authentication).
- **Request:**
  ```sh
  curl -X GET "http://127.0.0.1:8000/users/me/items" \
       -H "Authorization: Bearer your_jwt_token"
  ```

## Security
- Passwords are securely hashed using `bcrypt`
- JWTs are used for secure authentication
- Protected endpoints require a valid token

## License
This project is licensed under the MIT License.

