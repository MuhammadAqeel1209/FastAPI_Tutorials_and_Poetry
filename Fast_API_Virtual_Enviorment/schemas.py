from enum  import Enum
from datetime import date
from pydantic import BaseModel

class GenreURL(Enum):
    ROCK = 'rock'
    ELECTRONIC = 'electronics'
    SHOEGAZA = 'shoegaza'
    HIPHOP = 'hip-hop'

class Album(BaseModel):
    title : str
    releasedDate : date

class Bands(BaseModel):
    id: int
    name: str
    genre: str
    album : list[Album] = []