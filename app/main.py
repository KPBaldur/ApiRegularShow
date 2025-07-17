from fastapi import FastAPI
from app.routers import personajes, capitulos, temporadas, comics

app = FastAPI(
    title="Regular Show API",
    description="API pública para obtener información de la serie Regular Show, incluyendo personajes, capítulos, temporadas y cómics.",
    version="1.0.0",
    contact={
        "name": "Kevin P.",
        "url": "https://github.com/KevinP-Antartica/ApiRegularShow",
        "email": "kevinp@example.com"
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT"
    },
    terms_of_service="https://github.com/KevinP-Antartica/ApiRegularShow#terms"
)

app.include_router(personajes.router)
app.include_router(capitulos.router)
app.include_router(temporadas.router)
app.include_router(comics.router)