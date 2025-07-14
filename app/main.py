from fastapi import FastAPI
from app.routers import personajes, capitulos, temporadas, comics

app = FastAPI(
    tittle="Regular Show API",
    description= "API publica para obtener informacion de la serie Regular Show.",
    version="1.0.0"
)

app.include_router(personajes.router)
app.include_router(capitulos.router)
app.include_router(temporadas.router)
app.include_router(comics.router)