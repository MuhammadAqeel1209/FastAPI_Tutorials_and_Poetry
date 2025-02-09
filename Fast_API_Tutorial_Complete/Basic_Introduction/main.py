from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get():
    return {"message": "Hello, World!"}

@app.post("/")
async def post():
    return {"message": "Hello, World! From Post Route!"}

@app.put("/")
async def put():
    return {"message": "hello from the put route"}