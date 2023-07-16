
import datetime
from typing import Optional

from pydantic import BaseModel, Field


# base de las peliculas


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(max_length=10, min_length=2,)
    overview: str = Field(max_length=50, min_length=2)
    year: int = Field(le=datetime.date.today().year)
    rating: float = Field(le=10.0, ge=0.0)
    category: str = Field(max_length=10, min_length=5)

    class Config:
        schema_extra = {
            "example": {
                "title": "Avatar",
                "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
                "year": datetime.date.today().year,
                "rating": 7.8,
                "category": "Acción"
            }
        }
