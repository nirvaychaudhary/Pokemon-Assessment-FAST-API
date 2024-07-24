# Pokemon FASTAPI Project Assessment
This is a RESTAPI developed in FastAPI that serves a list of Pokemons. 
reference API: https://pokeapi.co/api/v2/pokemon?limit=100

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone `https://github.com/nirvaychaudhary/Pokemon-Assessment-FAST-API.git`
    cd pokemon_api
    ```

2. Create a virtual environment and activate it:
    ```bash
    Virtualenv pokemon_env
    source pokemon_env/bin/activate #for linux  
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:
    - Create a `.env` file and add your database URL:
      ```
      DATABASE_URL=postgresql+asyncpg://user:password@localhost/pokemon_db
      ```
    - Run the database migrations:
      ```bash
      alembic upgrade head
      ```

5. Run the FastAPI application:
    ```bash
    uvicorn main:app --reload
    ```

6. The API will be available at `http://127.0.0.1:8000`.

## API Endpoints
- `http://127.0.0.1:8000/docs#/` swagger docs
- `GET /api/v1/pokemons`: Retrieve a list of Pokemons.
- `GET /api/v1/pokemons/search`: Search for Pokemons by name or type.
- `POST /api/v1/pokemons`: Create a new Pokemon.
- `PUT /api/v1/{pokemon_id}`: Update a exisiting Pokemon.
- `DELETE /api/v1/{pokemon_id}`: Delete a Pokemon.

