from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import personajes, capitulos, temporadas, comics
from app.errors import configure_error_handlers
from app.config import settings

app = FastAPI(
    title=settings.app_name,
    description="API pública para obtener información de la serie Regular Show, incluyendo personajes, capítulos, temporadas y cómics.",
    version="1.0.0",
    contact={
        "name": "Kevin P.",
        "url": "https://github.com/KPBaldur/ApiRegularShow",
        "email": settings.admin_email
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT"
    },
    terms_of_service="https://github.com/KPBaldur/ApiRegularShow#terms"
)

# Routers
app.include_router(personajes.router)
app.include_router(capitulos.router)
app.include_router(temporadas.router)
app.include_router(comics.router)


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "Regular Show API is running. Visit /docs for documentation.",
        "documentation": "/docs"
    }

# Global Errors
configure_error_handlers(app)
