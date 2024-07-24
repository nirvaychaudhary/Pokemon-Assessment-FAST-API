#this file stores secret keys, environment variables and other necessary settings

from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()

# Debug prints
print(f"Current working directory: {os.getcwd()}")
print(f"Contents of .env file:")
with open(".env") as f:
    print(f.read())
print(f"DATABASE_URL: {settings.DATABASE_URL}")  # This will print the DATABASE_URL to verify it's loaded correctly
