from fastapi import FastAPI

app = FastAPI()

BANDS = [
    {'Id' : 1},
]

@app.get("/")
async def getData() -> dict[str,str]:
    return {"message":"FAST API"}

@app.get("/about")
async def about() -> str:
    return "A Great Company"