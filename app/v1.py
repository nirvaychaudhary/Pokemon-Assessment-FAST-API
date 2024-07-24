from app import crud, schemas
from app.database import engine, Base, get_db
from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.get("/pokemons", response_model=list[schemas.Pokemon])
async def read_pokemons(skip: int = 0, limit: int = 20, db: AsyncSession = Depends(get_db)):
    pokemons = await crud.get_pokemons(db, skip=skip, limit=limit)
    return pokemons

@router.post("/pokemons", response_model=schemas.Pokemon)
async def create_pokemon(pokemon: schemas.PokemonCreate, db: AsyncSession = Depends(get_db)):
    pokemons = await crud.create_pokemon(db, pokemon)
    return pokemons

@router.get("/pokemons/search", response_model=list[schemas.Pokemon])
async def search_pokemons(name: str = None, type: str = None, db: AsyncSession = Depends(get_db)):
    pokemons = await crud.get_pokemons_by_filter(db, name=name, type=type)
    return pokemons

@router.patch("/pokemons/{pokemon_id}", response_model=schemas.Pokemon)
async def update_pokemon(pokemon_id: int, pokemon: schemas.PokemonUpdate, db: AsyncSession = Depends(get_db)):
    pokemons = await crud.update_pokemon(db, pokemon_id, pokemon)
    if pokemons is None:
        raise HTTPException(status_code=404, detail="ID not found")
    return pokemons

@router.delete("/pokemon/{pokemon_id}", response_model=schemas.Pokemon)
async def delete_pokemon(pokemon_id: int, db: AsyncSession = Depends(get_db)):
    pokemons = await crud.delete_pokemon(db, pokemon_id)
    if pokemons is None:
        raise HTTPException(status_code=404, detail='ID not found')
    return pokemons