from fastapi import Body, FastAPI, Form,File,UploadFile

app = FastAPI()


@app.post("/login/")
async def login(username: str = Form(...), password: str = Body(...)):
    print("password", password)
    return {"username": username}
@app.post("/files/")
async def create_file(
    files: list[bytes] = File(..., description="A file read as bytes")
):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfile/")
async def create_upload_file(
    files: list[UploadFile] = File(..., description="A file read as UploadFile")
):
    return {"filename": [file.filename for file in files]}
