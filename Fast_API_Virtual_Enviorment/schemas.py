from enum import Enum
from datetime import date
from pydantic import BaseModel, Field, validator

class GenreURL(str, Enum):
    ROCK = 'rock'
    ELECTRONIC = 'electronics'
    SHOEGAZA = 'shoegaza'
    HIPHOP = 'hip-hop'

class Album(BaseModel):
    title: str
    releasedDate: date

class Bands(BaseModel):
    name: str
    genre: GenreURL
    album: list[Album] = []

class BandCreate(Bands):
    @validator('genre', pre=True)
    def validate_genre(cls, v):
        if isinstance(v, str):
            v = v.lower()
        if v not in GenreURL._value2member_map_:
            raise ValueError(f"Invalid genre: {v}")
        return GenreURL(v)

class BandWithId(Bands):
    id: int
