from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import personajes, capitulos, temporadas, comics
from app.errors import configure_error_handlers
from app.config import settings


app = FastAPI(
    title=settings.app_name,
    description="API pública para obtener información de la serie *Regular Show*.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    contact={
        "name": "Kevin P.",
        "url": "https://kpbaldur.github.io/RegularShowWiki/index.html",
        "email": "kevin.pizarrosanz@gmail.com"
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
def redirect_to_wiki():
    return {
        "message": "API pública para obtener información de la serie Regular Show. " \
                   "Esta API permite consultar personajes, capitulos, comics y temporadas. " \
                   "Está pensada para ser consumida por otros desarrolladores y por la web oficial del proyecto.",
        "documentation": "Ir a la Wiki del Proyecto (https://kpbaldur.github.io/RegularShowWiki)"
    }

# Global Errors
configure_error_handlers(app)
