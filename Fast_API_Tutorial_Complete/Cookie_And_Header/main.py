from fastapi import FastAPI,Cookie,Header

app = FastAPI()

@app.get("/items/")
async def get_items(
    cookie_id : str |None = Cookie(None),
    accept_encoding : str | None = Header(None),
    user_agent : str | None = Header(None) ,
    sec_ch_ua: str | None = Header(None),
    x_token: list[str] | None = Header(None),
):
    return {
        "cookie_id": cookie_id,
        "accept_encoding": accept_encoding,
        "user_agent": user_agent,
        "sec_ch_ua": sec_ch_ua,
        "x_token": x_token,
    }