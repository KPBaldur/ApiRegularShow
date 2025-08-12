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

#==============================================================
# 1. Endpoint principal con filtros y paginacion
#==============================================================
@router.get("/", response_model=List[Personaje])
def obtener_personajes(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    nombre: Optional[str] = None,
    raza: Optional[str] = None,
    tipo_personaje: Optional[str] = None,
    estado: Optional[str] = None,
    capitulo_aparicion: Optional[str] = None
):
    data = data_manager.get_data("personajes")

    if nombre:
        data = [p for p in data if nombre.lower() in p.get("nombre", "").lower()]
    if raza:
        data = [p for p in data if raza.lower() in p.get("raza", "").lower()]
    if tipo_personaje:
        data = [p for p in data if p.get("tipo_personaje", "").lower() == tipo_personaje.lower()]
    if estado:
        data = [p for p in data if p.get("estado", "").lower() == estado.lower()]
    if capitulo_aparicion:
        data = [p for p in data if p.get("capitulo_aparicion", "").lower() == capitulo_aparicion.lower()]

    if not data:
        raise HTTPException(status_code=404, detail="No se encontraron personajes que coincidan con los filtros proporcionados")

    return data[skip:skip + limit]

#==============================================================
# 2. Endpoint fijos
#==============================================================
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

@router.get("/secundarios", response_model=List[Personaje])
def obtener_personajes_secundarios():
    data = data_manager.get_data("personajes")
    secundarios = [p for p in data if p.get("tipo_personaje", "").lower() == "secundario"]
    if not secundarios:
        raise HTTPException(status_code=404, detail="No se encontraron personajes secundarios")
    return secundarios

#==============================================================
# 3. Endpoint unificado para personajes aleatorios
#==============================================================
@router.get("/aleatorio/{cantidad}", response_model=List[Personaje])
def obtener_personajes_aleatorios(cantidad: int):
    data = data_manager.get_data("personajes")
    if not data:
        raise HTTPException(status_code=404, detail="No hay personajes disponibles")
    return random.sample(data, min(cantidad, len(data)))

#==============================================================
# 4. Endpoints de busqueda por campos especificos
#==============================================================
@router.get("/nombre/{nombre}", response_model=List[Personaje])
def obtener_personajes_por_nombre(nombre: str):
    data = data_manager.get_data("personajes")
    resultado = [p for p in data if nombre.lower() in p.get("nombre", "").lower()]
    if not resultado:
        raise HTTPException(status_code=404, detail="No se encontraron personajes con ese nombre")
    return resultado

@router.get("/tipo/{tipo_personaje}", response_model=List[Personaje])
def obtener_personajes_por_tipo(tipo_personaje: str):
    data = data_manager.get_data("personajes")
    resultado = [p for p in data if tipo_personaje.lower() in p.get("tipo_personaje", "").lower()]
    if not resultado:
        raise HTTPException(status_code=404, detail="No se encontraron personajes de ese tipo")
    return resultado

#==============================================================
# 5. Endpoint de busqueda por ID
#==============================================================
@router.get("/{id}", response_model=Personaje)
def obtener_personaje_por_id(id: str):
    data = data_manager.get_data("personajes")
    for personaje in data:
        if personaje.get("id", "").lower() == id.lower():
            return personaje
    raise HTTPException(status_code=404, detail="Personaje no encontrado")
