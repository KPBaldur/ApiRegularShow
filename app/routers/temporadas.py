from fastapi import APIRouter, HTTPException, Query
import json
from pathlib import Path
from app.models import Temporada
from typing import List, Optional

router = APIRouter(
    prefix="/temporadas",
    tags=["Temporadas"]
)

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "temporadas.json"

@router.get("/", response_model=List[Temporada])
def obtener_temporadas(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    anio_estreno: Optional[int] = None,
    numero_temporada: Optional[int] = None
):
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
    if anio_estreno:
        data = [t for t in data if t["anio_estreno"] == anio_estreno]
    if numero_temporada:
        data = [t for t in data if t["numero_temporada"] == numero_temporada]
    return data[skip:skip+limit]

@router.get("/{id}", response_model=Temporada)
def obtener_temporada_por_id(id: str):
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
    for temporada in data:
        if temporada["id"] == id:
            return temporada
    raise HTTPException(status_code=404, detail="Temporada no encontrada")