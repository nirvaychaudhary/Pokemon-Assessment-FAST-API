from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings

DATABASE_URL = settings.DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine,
    class_=AsyncSession
)

Base = declarative_base()

'''
This function likely provides a database session to other parts of the application. 
It's used to manage database connections within an asynchronous context.
get_db defines asynchronous function to create database session
'''

async def get_db():
    async with SessionLocal() as session:
        try:
            yield session

        finally:
            await session.close()