from fastapi import FastAPI,HTTPException
from enum  import Enum
app = FastAPI()

class GenreURL(Enum):
    ROCK = 'rock'
    ELECTRONIC = 'electronics'
    SHOEGAZA = 'shoegaza'
    HIPHOP =  'hip-hop'

BANDS = [
    {'Id' : 1,'Name':"The Klinks",'Genre': 'Rock'},
    {'Id' : 2,'Name':"Alphex Twins",'Genre': 'Electronic'},
    {'Id' : 3,'Name':"Slowdive",'Genre': 'Shoegaza'},
    {'Id' : 4,'Name':"Wu Tang Clain",'Genre': 'Hip-Hop'},
]

@app.get("/bands")
async def getData() -> list[dict]:
    return BANDS

@app.get("/band/{band_id}")
async def getSingleBand(band_id : int):
    band = next((b for b in BANDS if b['Id'] == band_id),None)
    if band is None:
        raise HTTPException(status_code=404,detail="Not Found")
    return band

@app.get("/band/genre/{band_genre}")
async def getSingleBand(band_genre : GenreURL):
    return [b for b in BANDS if b['Genre'].lower() == band_genre.value]
  