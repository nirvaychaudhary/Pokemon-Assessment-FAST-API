import requests
from app import crud, schemas
from app.database import engine, Base, get_db
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from app.v1 import router as router_v1

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Fetch pokemons data once after each time server reloads
    response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=100")
    if response.status_code == 200:
        pokemons = response.json().get("results", [])
        async for db in get_db():
            for poke in pokemons:
                poke_data = requests.get(poke["url"]).json()
                pokemon = schemas.PokemonCreate(
                    name=poke_data["name"],
                    image=poke_data["sprites"]["back_default"],
                    type=poke_data["types"][0]["type"]["name"]
                )
                await crud.create_pokemon(db, pokemon)

    yield

app.router.lifespan_context = lifespan

app.include_router(router_v1, prefix='/api/v1')