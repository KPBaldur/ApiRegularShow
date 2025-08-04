from fastapi import APIRouter, HTTPException, Query
from app.models import Capitulo, Temporada
from typing import List, Optional
from app.data.data_manager import DataManager
from app.data import data_manager

router = APIRouter(
    prefix="/temporadas",
    tags=["Temporadas"]
)

data_manager = DataManager()

@router.get("/capitulos-por-temporada", response_model=List[dict])
def capitulos_por_temporada():
    temporadas = data_manager.get_data("temporadas")
    capitulos = data_manager.get_data("capitulos")
    resultado = []
    for temporada in temporadas:
        numero_temporada = temporada["numero_temporada"]
        capitulos_temp = [c for c in capitulos if c["numero_temporada"] == numero_temporada]
        resultado.append({
            "temporada": numero_temporada,
            "total_capitulos": len(capitulos_temp),
            "nombres_capitulos": [c["nombre"] for c in capitulos_temp]
        })
    return resultado

@router.get("/top-imdb", response_model=List[Capitulo])
def top_10_capitulos_imdb():
    capitulos = data_manager.get_data("capitulos")
    capitulos_ordenados = sorted(
        capitulos, key=lambda c: c.get("imbdb_score", 0), reverse=True
    )
    return capitulos_ordenados[:10]

@router.get("/", response_model=List[Temporada])
def obtener_temporadas(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    anio_estreno: Optional[int] = None,
    numero_temporada: Optional[int] = None
):
    data = data_manager.get_data("temporadas")

    if anio_estreno:
        data = [t for t in data if t["anio_estreno"] == anio_estreno]
    if numero_temporada:
        data = [t for t in data if t["numero_temporada"] == numero_temporada]

    return data[skip:skip + limit]


@router.get("/{id}", response_model=Temporada)
def obtener_temporada_por_id(id: str):
    data = data_manager.get_data("temporadas")
    for temporada in data:
        if temporada["id"] == id:
            return temporada
    raise HTTPException(status_code=404, detail="Temporada no encontrada")
