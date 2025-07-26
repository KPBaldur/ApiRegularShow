from app.data import data_manager
from fastapi import APIRouter, HTTPException, Query
from app.models import Personaje
from typing import List, Optional
from app.data.data_manager import DataManager
import random

router = APIRouter(
    prefix="/personajes",
    tags=["Personajes"]
)

data_manager = DataManager()

@router.get("/", response_model=List[Personaje])
def obtener_personajes(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    nombre: Optional[str] = None,
    raza: Optional[str] = None,
    tipo_personaje: Optional[str] = None,
    profesion: Optional[str] = None
):
    data = data_manager.get_data("personajes")

    if nombre:
        data = [p for p in data if nombre.lower() in p["nombre"].lower()]
    if raza:
        data = [p for p in data if raza.lower() in p["raza"].lower()]
    if tipo_personaje:
        data = [p for p in data if tipo_personaje.lower() in p["tipo_personaje"].lower()]
    if profesion:
        data = [p for p in data if profesion.lower() in p["profesion"].lower()]

    return data[skip:skip + limit]


@router.get("/aleatorio/6", response_model=List[Personaje])
def obtener_6_personajes_aleatorios():
    data = data_manager.get_data("personajes")
    return random.sample(data, min(6, len(data)))


@router.get("/aleatorio/10", response_model=List[Personaje])
def obtener_10_personajes_aleatorios():
    data = data_manager.get_data("personajes")
    return random.sample(data, min(10, len(data)))


@router.get("/{id}", response_model=Personaje)
def obtener_personaje_por_id(id: str):
    data = data_manager.get_data("personajes")
    for personaje in data:
        if personaje["id"] == id:
            return personaje
    raise HTTPException(status_code=404, detail="Personaje no encontrado")