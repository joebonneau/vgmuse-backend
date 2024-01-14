from datetime import date

from pydantic import BaseModel, Field

from . import PyObjectId


class OST(BaseModel):
    id: PyObjectId | None = Field(alias="_id", default=None)
    game: str
    composers: list[str]
    release_date_usa: date
    release_date_jp: date
    commercially_available: bool

class OSTCollection(BaseModel):
    osts: list[OST]
