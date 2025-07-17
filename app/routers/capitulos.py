from fastapi import APIRouter, HTTPException, Query
import json
from pathlib import Path
from app.models import Capitulo
from typing import List, Optional

router = APIRouter(
    prefix="/capitulos",
    tags=["Capitulos"]
)

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "capitulos.json"

@router.get("/", response_model=List[Capitulo])
def obtener_capitulos(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    titulo: Optional[str] = None,
    temporada: Optional[int] = None,
    numero: Optional[int] = None
):
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
    if titulo:
        data = [c for c in data if titulo.lower() in c["titulo"].lower()]
    if temporada:
        data = [c for c in data if c["temporada"] == temporada]
    if numero:
        data = [c for c in data if c["numero"] == numero]
    return data[skip:skip+limit]

@router.get("/{id}", response_model=Capitulo)
def obtener_capitulo_por_id(id: str):
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
    for capitulo in data:
        if capitulo["id"] == id:
            return capitulo
    raise HTTPException(status_code=404, detail="Capítulo no encontrado")