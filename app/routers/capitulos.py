from fastapi import APIRouter, HTTPException, Query
from app.models import Capitulo
from typing import List, Optional
from app.data.data_manager import DataManager

router = APIRouter(
    prefix="/capitulos",
    tags=["Capitulos"]
)

data_manager = DataManager()

def ensure_complete_capitulo(cap_data):
    """Asegura que el capítulo tenga todos los campos necesarios"""
    # Crear una copia para no modificar el original
    complete_cap = cap_data.copy()
    
    # Asegurar que imagen_url existe, aunque sea None
    if 'imagen_url' not in complete_cap:
        complete_cap['imagen_url'] = None
    
    return complete_cap

@router.get("/", response_model=List[Capitulo])
def obtener_capitulos(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    titulo: Optional[str] = None,
    temporada: Optional[int] = None,
    numero: Optional[int] = None,
    imdb_score: Optional[float] = None
):
    data = data_manager.get_data("capitulos")

    if titulo:
        data = [c for c in data if titulo.lower() in c["titulo"].lower()]
    if temporada:
        data = [c for c in data if c["temporada"] == temporada]
    if numero:
        data = [c for c in data if c["numero"] == numero]
    if imdb_score is not None:
        data = [c for c in data if isinstance(c.get("imdb_score"), (int, float)) and c["imdb_score"] >= imdb_score]

    result = [ensure_complete_capitulo(c) for c in data[skip:skip + limit]]
    return result

@router.get("/top", response_model=List[Capitulo])
def obtener_top_capitulos(limit: int = 10, temporada: Optional[int] = None):
    data = data_manager.get_data("capitulos")
    data = [c for c in data if isinstance(c.get("imdb_score"), (int, float))]
    
    # Filtrar por temporada si se especifica
    if temporada:
        data = [c for c in data if c.get("temporada") == temporada]

    data.sort(key=lambda c: c["imdb_score"], reverse=True)
    
    # Asegurar campos completos antes de devolver
    result = [ensure_complete_capitulo(c) for c in data[:limit]]
    return result

@router.get("/{id}", response_model=Capitulo)
def obtener_capitulo_por_id(id: str):
    data = data_manager.get_data("capitulos")
    for capitulo in data:
        if capitulo["id"] == id:
            return capitulo
    raise HTTPException(status_code=404, detail="Capítulo no encontrado")