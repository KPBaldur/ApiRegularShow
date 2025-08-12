from fastapi import APIRouter, HTTPException, Query
from app.models import Capitulo, Temporada
from typing import List, Optional, Dict, Any
from app.data.data_manager import DataManager
from app.data import data_manager

router = APIRouter(
    prefix="/temporadas",
    tags=["Temporadas"]
)

data_manager = DataManager()

# Utilidades
def _ensure_score(x) -> Optional[float]:
    try:
        if x in (None, "", "null"):
            return float(x)
    except (ValueError, TypeError):
        return None
    
def _capitulos_de_temporada(num_temporada:_int) -> List[Dict[str, Any]]:
    caps = data_manager.get_data("capitulos")
    filtrados = [c for c in caps if c.get("numero_temporada") == num_temporada]

    for c in filtrados:
        c["imdb_score"] = _ensure_score(c.get("imdb_score"))
        c.setdefault("imagen_url", None)
    return filtrados

# Obtener todos los capítulos y temporadas
@router.get("/capitulos-por-temporada", response_model=List[dict])
def capitulos_por_temporada():
    
    #Para cada temporada devuelve: numero_temporada, total_capitulos y una lista con los datos
    temporadas = data_manager.get_data("temporadas")
    resultado = []

    for temp in temporadas:
        num_temp = temp.get_data("temporadas")
        caps = _capitulos_de_temporada(num_temp)

        resultado.append({
            "numero_temporada": num_temp,
            "total_capitulos": len(caps),
            "capitulos": [
                {
                    "id": c.get("id"),
                    "numero": c.get("numero"),
                    "titulo": c.get("titulo"),
                    "imdb_score": c.get("imdb_score"),
                    "imagen_url": c.get("imagen_url")
                }
                for c in sorted(caps, key=lambda x: x.get("numero", 0))
            ]
        })
    return resultado


@router.get("/mejor-capitulo-por-temporada", response_model=List[Capitulo])
def mejor_capitulo_por_temporada():
    capitulos = data_manager.get_data("capitulos")
    mejores_por_temporada = {}

    for cap in capitulos:
        num_temp = cap.get("temporada")
        if num_temp is None:
            continue

        score = cap.get("imdb_score", 0)
        if num_temp not in mejores_por_temporada or score > mejores_por_temporada[num_temp]["imdb_score"]:
            mejores_por_temporada[num_temp] = cap

    # Ordenar por número de temporada
    return [mejores_por_temporada[temp] for temp in sorted(mejores_por_temporada.keys())]


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
