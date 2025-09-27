from fastapi import APIRouter, HTTPException, Query
from app.models import Capitulo
from typing import List, Optional
from app.data.data_manager import DataManager
from rapidfuzz import fuzz, process

router = APIRouter(
    prefix="/capitulos",
    tags=["Capitulos"]
)

data_manager = DataManager()

def ensure_complete_capitulo(cap_data):
    complete_cap = cap_data.copy()

    if 'imagen_url' not in complete_cap:
        complete_cap['imagen_url'] = None

    try:
        if "imdb_score" in complete_cap and complete_cap["imdb_score"] not in (None, "", "null"):
            complete_cap["imdb_score"] = float(complete_cap["imdb_score"])
        else:
            complete_cap["imdb_score"] = None
    except (ValueError, TypeError):
        complete_cap["imdb_score"] = None

    return complete_cap

@router.get("/", response_model=List[Capitulo])
def obtener_capitulos(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    titulo: Optional[str] = None,
    temporada: Optional[int] = None,
    numero: Optional[int] = None,
    imdb_score: Optional[float] = None
):
    data = data_manager.get_data("capitulos")
    data = [ensure_complete_capitulo(c) for c in data]

    if titulo:
        data = [c for c in data if 
                titulo.lower() in c.get("titulo_eng", "").lower() or 
                titulo.lower() in c.get("titulo_es", "").lower()]
    if temporada:
        data = [c for c in data if c.get("temporada") == temporada]
    if numero:
        data = [c for c in data if c.get("numero") == numero]
    if imdb_score is not None:
        data = [c for c in data if c.get("imdb_score") is not None and c["imdb_score"] >= imdb_score]

    return data[skip:skip + limit]

@router.get("/nombre/{nombre}", response_model=List[Capitulo])
def buscar_capitulo_nombre(nombre: str):
    data = data_manager.get_data("capitulos")
    titulos_map = {}
    for c in data:
        if c.get("titulo_eng"):
            titulos_map[c["titulo_eng"]] = c
        if c.get("titulo_es"):
            titulos_map[c["titulo_es"]] = c

    matches = process.extract(nombre, titulos_map.keys(), scorer=fuzz.WRatio, limit=5)
    resultado = [ensure_complete_capitulo(titulos_map[m[0]]) for m in matches if m[1] >= 60]

    if not resultado:
        resultado = [
            ensure_complete_capitulo(c) for c in data
            if nombre.lower() in c.get("titulo_eng", "").lower()
            or nombre.lower() in c.get("titulo_es", "").lower()
        ]

    if not resultado:
        raise HTTPException(status_code=404, detail="No se encontraron capítulos similares al nombre entregado.")
    
    return resultado

@router.get("/temporada/{temporada}", response_model=dict)
def obtener_capitulos_por_temporada(temporada: int):
    data = data_manager.get_data("capitulos")
    capitulos_temporada = [ensure_complete_capitulo(c) for c in data if c.get("temporada") == temporada]

    if not capitulos_temporada:
        raise HTTPException(status_code=404, detail="No se encontraron capítulos para esta temporada.")

    return {
        "temporada": temporada,
        "total_capitulos": len(capitulos_temporada),
        "capitulos": capitulos_temporada
    }

@router.get("/top", response_model=List[Capitulo])
def obtener_top_capitulos(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    temporada: Optional[int] = None,
    sort_by: str = Query("imdb_score", description="Campo por el que ordenar"),
    order: str = Query("desc", regex="^(asc|desc)$", description="Orden: asc o desc")
):
    data = data_manager.get_data("capitulos")
    data = [ensure_complete_capitulo(c) for c in data]

    if temporada:
        data = [c for c in data if c.get("temporada") == temporada]

    data = [c for c in data if c.get(sort_by) is not None]

    reverse = True if order == "desc" else False
    try:
        data.sort(key=lambda c: c.get(sort_by), reverse=reverse)
    except TypeError:
        raise HTTPException(status_code=400, detail=f"No se puede ordenar por '{sort_by}'")

    return data[skip:skip + limit]

@router.get("/{id}", response_model=Capitulo)
def obtener_capitulo_por_id(id: str):
    data = data_manager.get_data("capitulos")
    for capitulo in data:
        if capitulo.get("id") == id:
            return ensure_complete_capitulo(capitulo)
    raise HTTPException(status_code=404, detail="Capítulo no encontrado")
