from fastapi import APIRouter, HTTPException, Query
import json
from pathlib import Path
from app.models import Personaje
from typing import List, Optional
import random

router = APIRouter(
    prefix="/personajes",
    tags=["Personajes"]
)

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "personajes.json"

@router.get("/", response_model=List[Personaje])
def obtener_personajes(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    nombre: Optional[str] = None,
    raza: Optional[str] = None,
    estado: Optional[str] = None,
    profesion: Optional[str] = None
):
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
    # Filtros
    if nombre:
        data = [p for p in data if nombre.lower() in p["nombre"].lower()]
    if raza:
        data = [p for p in data if raza.lower() in p["raza"].lower()]
    if estado:
        data = [p for p in data if estado.lower() in p["estado"].lower()]
    if profesion:
        data = [p for p in data if profesion.lower() in p["profesion"].lower()]
    return data[skip:skip+limit]

@router.get("/aleatorio/5", response_model=List[Personaje])
def obtener_5_personajes_aleatorios():
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
    return random.sample(data, min(5, len(data)))

@router.get("/aleatorio/10", response_model=List[Personaje])
def obtener_10_personajes_aleatorios():
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
    return random.sample(data, min(10, len(data)))

@router.get("/{id}", response_model=Personaje)
def obtener_personaje_por_id(id: str):
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
    for personaje in data:
        if personaje["id"] == id:
            return personaje
    raise HTTPException(status_code=404, detail="Personaje no encontrado")