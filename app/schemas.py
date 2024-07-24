from pydantic import BaseModel, Field
from typing import Optional
class PokemonCreate(BaseModel):
    name:str
    image:str
    type:str

class PokemonUpdate(BaseModel):
    name: Optional[str] = Field(None, example="New Pokemon Name")
    image: Optional[str] = Field(None, example="test_image.png")
    type: Optional[str] = Field(None, example="fire")

class Pokemon(BaseModel):
    id:int
    name:str
    image:str
    type:str
    class Config:
        orm_mode = True

        