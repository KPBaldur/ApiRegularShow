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

    if not data:
        raise HTTPException(status_code=404, detail="No se encontraron personajes que coincidan con los filtros proporcionados")

    return data[skip:skip + limit]

@router.get("/todos", response_model=List[Personaje])
def obtener_todos_los_personajes():
    data = data_manager.get_data("personajes")
    if not data:
        raise HTTPException(status_code=404, detail="No hay personajes disponibles")
    return data

@router.get("/principales", response_model=List[Personaje])
def obtener_personajes_principales():
    data = data_manager.get_data("personajes")
    principales = [p for p in data if p.get("tipo_personaje", "").lower() == "principal"]
    
    if not principales:
        raise HTTPException(status_code=404, detail="No se encontraron personajes principales")
    
    return principales


@router.get("/aleatorio/6", response_model=List[Personaje])
def obtener_6_personajes_aleatorios():
    data = data_manager.get_data("personajes")
    if not data:
        raise HTTPException(status_code=404, detail="No hay personajes disponibles")
    return random.sample(data, min(6, len(data)))

@router.get("/aleatorio/10", response_model=List[Personaje])
def obtener_10_personajes_aleatorios():
    data = data_manager.get_data("personajes")
    if not data:
        raise HTTPException(status_code=404, detail="No hay personajes disponibles")
    return random.sample(data, min(10, len(data)))

@router.get("/aleatorio/20", response_model=List[Personaje])
def obtener_20_personajes_aleatorios():
    data = data_manager.get_data("personajes")
    if not data:
        raise HTTPException(status_code=404, detail="No hay personajes disponibles")
    return random.sample(data, min(20, len(data)))

@router.get("/nombre/{nombre}", response_model=List[Personaje])
def obtener_personajes_por_nombre(nombre: str):
    data = data_manager.get_data("personajes")
    resultado = [p for p in data if nombre.lower() in p["nombre"].lower()]
    if not resultado:
        raise HTTPException(status_code=404, detail="No se encontraron personajes con ese nombre")
    return resultado

@router.get("/tipo/{tipo_personaje}", response_model=List[Personaje])
def obtener_personajes_por_tipo(tipo_personaje: str):
    data = data_manager.get_data("personajes")
    resultado = [p for p in data if tipo_personaje.lower() in p["tipo_personaje"].lower()]
    if not resultado:
        raise HTTPException(status_code=404, detail="No se encontraron personajes de ese tipo")
    return resultado

@router.get("/{id}", response_model=Personaje)
def obtener_personaje_por_id(id: str):
    data = data_manager.get_data("personajes")
    for personaje in data:
        if personaje["id"] == id:
            return personaje
    raise HTTPException(status_code=404, detail="Personaje no encontrado")
