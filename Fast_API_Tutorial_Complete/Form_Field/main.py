from fastapi import Body, FastAPI, Form


app = FastAPI()


@app.post("/login/")
async def login(username: str = Form(...), password: str = Body(...)):
    print("password", password)
    return {"username": username}
