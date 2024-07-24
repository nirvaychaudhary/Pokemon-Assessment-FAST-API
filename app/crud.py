from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from . import models
from . import schemas

async def get_pokemon(db: AsyncSession, pokemon_id: int):
    result = await db.execute(select(models.Pokemon).filter(models.Pokemon.id == pokemon_id))
    return result.scalars().first()

async def get_pokemons(db: AsyncSession, skip: int=0, limit: int=10):
    result = await db.execute(select(models.Pokemon).offset(skip).limit(limit))
    return result.scalars().all()

async def create_pokemon(db: AsyncSession, pokemon: schemas.PokemonCreate):
    result = models.Pokemon(**pokemon.model_dump())
    db.add(result)
    await db.commit()
    await db.refresh(result)
    return result


async def update_pokemon(db: AsyncSession, pokemon_id: int, pokemon: schemas.PokemonUpdate):
    result = await db.execute(select(models.Pokemon).where(models.Pokemon.id == pokemon_id))
    query_result = result.scalars().first()
    
    if not query_result:
        return None
    
    if pokemon.name is not None:
        query_result.name = pokemon.name
    if pokemon.image is not None:
        query_result.image = pokemon.image
    if pokemon.type is not None:
        query_result.type = pokemon.type
    
    await db.commit()
    await db.refresh(query_result)
    return query_result

async def delete_pokemon(db: AsyncSession, pokemon_id: int):
    result = await db.execute(select(models.Pokemon).filter(models.Pokemon.id == pokemon_id))
    query_result = result.scalars().first()
    if query_result is None:
        return None
    await db.delete(query_result)
    await db.commit()
    return query_result  


async def get_pokemons_by_filter(db: AsyncSession, name: str = None, type: str = None):
    query = select(models.Pokemon)
    if name:
        query = query.filter(models.Pokemon.name.ilike(f"%{name}%"))

    if type:
        query = query.filter(models.Pokemon.type.ilike(f"%{type}%"))

    result = await db.execute(query)
    return result.scalars().all()