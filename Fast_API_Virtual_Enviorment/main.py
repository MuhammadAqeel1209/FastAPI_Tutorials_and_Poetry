from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from model import Band, BandCreate, Album
from db import getSession, init_db
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/band_create/")
def create_band(band_data: BandCreate, session: Session = Depends(getSession)):
    band = Band(name=band_data.name, genre=band_data.genre)
    session.add(band)
    session.flush()
    for album_data in band_data.albums:
        album = Album(
            title=album_data.title,
            releasedDate=album_data.releasedDate,
            band_id=band.id
        )
        session.add(album)

    session.commit()
    return {"message": "Band and albums created successfully!", "band_id": band.id}


@app.get('/band/{band_id}/')
async def get_band_by_id(band_id: int, session: Session = Depends(getSession)) -> Band:
    band = session.get(Band, band_id)
    if not band:
        raise HTTPException(status_code=404, detail="Band not found")
    return band


@app.get('/bands/')
async def get_all_bands(session: Session = Depends(getSession)) -> list[dict]:
    statement = select(Band)
    results = session.exec(statement).all()
    bands_with_albums = [
        {
            "id": band.id,
            "name": band.name,
            "genre": band.genre,
            "albums": [
                {"id": album.id, "title": album.title, "releasedDate": album.releasedDate}
                for album in band.albums
            ],
        }
        for band in results
    ]
    return bands_with_albums
