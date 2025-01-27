from fastapi import FastAPI,HTTPException
from schemas import Bands,GenreURL,BandCreate,BandWithId
app = FastAPI()


BANDS = [
    {'id': 1, 'name': "The Klinks", 'genre': 'Rock'},
    {'id': 2, 'name': "Alphex Twins", 'genre': 'Electronic'},
    {
        'id': 3,
        'name': "Slowdive",
        'genre': 'Shoegaza',
        'album': [
            {
                'title': 'First',
                'releasedDate': '2024-01-01'
            }
        ]
    },
    {'id': 4, 'name': "Wu Tang Clan", 'genre': 'Hip-Hop'},
]


@app.get("/bands")
async def getData(has_album : bool = False,genre:GenreURL|None = None) -> list[BandWithId]:
    band_List =  [BandWithId(**b) for b in BANDS]
    if has_album:
        band_List = [band for band in band_List if 'album' in band]
        
    if genre:
        band_List = [band for band in band_List if band['genre'].lower() == genre.value] 
        
    return band_List  


@app.get("/band/{band_id}")
async def getSingleBand(band_id : int):
    band = next((BandWithId(**b) for b in BANDS if b['id'] == band_id),None)
    if band is None:
        raise HTTPException(status_code=404,detail="Not Found")
    return band

@app.get("/band/genre/{band_genre}")
async def getSingleBand(band_genre : GenreURL):
    return [BandWithId(**b) for b in BANDS if b['genre'].lower() == band_genre.value]
  

@app.post("/band_create/")
async def createBand(band_data : BandCreate)->BandWithId:
    id = BANDS[-1]['id'] + 1
    band = BandWithId(id=id, **band_data.model_dump()).model_dump()
    BANDS.append(band)
    return band