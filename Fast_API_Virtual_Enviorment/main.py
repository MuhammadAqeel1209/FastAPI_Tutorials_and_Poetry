from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def getData() -> dict[str,str]:
    return {"message":"FAST API"}
