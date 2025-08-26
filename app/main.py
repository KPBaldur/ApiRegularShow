from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import personajes, capitulos, temporadas, comics
from app.errors import configure_error_handlers
from app.config import settings
from fastapi.responses import RedirectResponse

app = FastAPI(
    title=settings.app_name,
    description="API pública para obtener información de la serie *Regular Show*.",
    version="1.0.0",
    docs_url=None,
    redoc_url=None,
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

app.include_router(personajes.router)
app.include_router(capitulos.router)
app.include_router(temporadas.router)
app.include_router(comics.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Redirecciones a la Wiki ---
@app.get("/", include_in_schema=False)
def redirect_root():
    return RedirectResponse("https://kpbaldur.github.io/RegularShowWiki", status_code=307)

@app.get("/docs", include_in_schema=False)
async def redirect_docs():
    return RedirectResponse("https://kpbaldur.github.io/RegularShowWiki/docs", status_code=307)

@app.get("/redoc", include_in_schema=False)
async def redirect_redoc():
    return RedirectResponse("https://kpbaldur.github.io/RegularShowWiki/docs", status_code=307)

configure_error_handlers(app)
