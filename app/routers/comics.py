from fastapi import APIRouter, HTTPException, Query
import json
from pathlib import Path
from app.models import Comic
from typing import List, Optional

router = APIRouter(
    prefix="/comics",
    tags=["Comics"]
)

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "comics.json"

@router.get("/", response_model=List[Comic])
def obtener_comics(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    titulo: Optional[str] = None,
    tipo: Optional[str] = None,
    autor: Optional[str] = None,
    publicacion: Optional[str] = None
):
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
    if titulo:
        data = [c for c in data if titulo.lower() in c["titulo"].lower()]
    if tipo:
        data = [c for c in data if tipo.lower() in c["tipo"].lower()]
    if autor:
        data = [c for c in data if any(autor.lower() in a.lower() for a in c["autores"])]
    if publicacion:
        data = [c for c in data if publicacion in c["publicacion"]]
    return data[skip:skip+limit]

@router.get("/{id}", response_model=Comic)
def obtener_comic_por_id(id: str):
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
    for comic in data:
        if comic["id"] == id:
            return comic
    raise HTTPException(status_code=404, detail="Cómic no encontrado")