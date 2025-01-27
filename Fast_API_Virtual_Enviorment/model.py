from sqlmodel import SQLModel, Field, Relationship
from enum import Enum
from datetime import date
from typing import List, Optional


class GenreURL(str, Enum):
    ROCK = 'rock'
    ELECTRONIC = 'electronic'
    SHOEGAZE = 'shoegaze'
    HIPHOP = 'hip-hop'


class AlbumBase(SQLModel):
    title: str
    releasedDate: date


class Album(AlbumBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    band_id: Optional[int] = Field(default=None, foreign_key="band.id")
    band: "Band" = Relationship(back_populates="albums")


class BandBase(SQLModel):
    name: str
    genre: GenreURL


class BandCreate(BandBase):
    albums: List[AlbumBase] = []


class Band(BandBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    albums: List[Album] = Relationship(back_populates="band")
