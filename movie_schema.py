from pydantic import BaseModel, Field
from typing import Optional

class MovieBase(BaseModel):
    title: str = Field(..., max_length=15, min_length=5)
    overview: str = Field(..., max_length=45, min_length=15)
    year: int = Field(..., le=2022)
    rating: float = Field(..., ge=1, le=10)
    category: str = Field(..., min_length=3, max_length=20)

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True