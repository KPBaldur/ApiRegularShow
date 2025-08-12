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


# --- Utilidades ----------------------------------------------

def _ensure_score(x) -> Optional[float]:
    """Normaliza imdb_score a float o None."""
    try:
        if x in (None, "", "null"):
            return None
        return float(x)
    except (ValueError, TypeError):
        return None


def _capitulos_de_temporada(num_temporada: int) -> List[Dict[str, Any]]:
    """Filtra y normaliza capítulos por número de temporada."""
    caps = data_manager.get_data("capitulos")
    filtrados = [c for c in caps if c.get("temporada") == num_temporada]
    # normalizar imdb_score y asegurar campos clave
    for c in filtrados:
        c["imdb_score"] = _ensure_score(c.get("imdb_score"))
        c.setdefault("imagen_url", None)
    return filtrados


# --- Endpoints -----------------------------------------------

@router.get("/capitulos-por-temporada", response_model=List[dict])
def capitulos_por_temporada():
    """
    Para cada temporada devuelve: numero_temporada, total_capitulos y una lista con
    {id, numero, titulo, imdb_score}.
    """
    temporadas = data_manager.get_data("temporadas")
    resultado = []

    for temp in temporadas:
        num_temp = temp.get("numero_temporada")
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
                }
                for c in sorted(caps, key=lambda x: x.get("numero", 0))
            ]
        })

    return resultado


@router.get("/mejor-capitulo-por-temporada", response_model=List[Capitulo])
def mejor_capitulo_por_temporada():
    """
    Devuelve el mejor capítulo (mayor imdb_score) por cada temporada.
    Ignora capítulos sin puntaje.
    """
    caps = data_manager.get_data("capitulos")
    mejores_por_temp: Dict[int, Dict[str, Any]] = {}

    for c in caps:
        num_temp = c.get("temporada")
        score = _ensure_score(c.get("imdb_score"))
        if num_temp is None or score is None:
            continue

        # Guardar con score normalizado
        if (num_temp not in mejores_por_temp) or (score > mejores_por_temp[num_temp]["imdb_score"]):
            c_norm = dict(c)
            c_norm["imdb_score"] = score
            c_norm.setdefault("imagen_url", None)
            mejores_por_temp[num_temp] = c_norm

    return [mejores_por_temp[t] for t in sorted(mejores_por_temp.keys())]


@router.get("/resumen", response_model=List[dict])
def resumen_temporadas():
    """
    Resumen por temporada con:
    - id
    - numero_temporada
    - cantidad_capitulos
    - anio_estreno
    - promedio_imdb_score (2 decimales, None si no hay puntajes)
    """
    temporadas = data_manager.get_data("temporadas")
    resumen = []

    for temp in temporadas:
        num_temp = temp.get("numero_temporada")
        caps = _capitulos_de_temporada(num_temp)
        scores = [c["imdb_score"] for c in caps if c.get("imdb_score") is not None]

        promedio = round(sum(scores) / len(scores), 2) if scores else None

        resumen.append({
            "id": temp.get("id"),
            "numero_temporada": num_temp,
            "cantidad_capitulos": len(caps),
            "anio_estreno": temp.get("anio_estreno"),
            "promedio_imdb_score": promedio
        })

    # Ordenar por numero_temporada asc
    return sorted(resumen, key=lambda x: x["numero_temporada"])


@router.get("/", response_model=List[Temporada])
def obtener_temporadas(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    anio_estreno: Optional[int] = None,
    numero_temporada: Optional[int] = None
):
    temporadas_raw = data_manager.get_data("temporadas")
    capitulos = data_manager.get_data("capitulos")

    normalizadas = []
    for t in temporadas_raw:
        # Copia para no mutar el array compartido en memoria
        temp = dict(t)

        # 1) Mapear numero -> numero_temporada (lo que exige el modelo)
        if "numero_temporada" not in temp:
            temp["numero_temporada"] = temp.get("numero")

        # 2) Asegurar lista de capitulos
        temp.setdefault("capitulos", temp.get("capitulos", []))

        # 3) Calcular numero_capitulos desde capitulos.json (si tu lista está vacía)
        num_temp = temp.get("numero_temporada")
        count_por_cruce = len([c for c in capitulos if c.get("temporada") == num_temp])
        temp["numero_capitulos"] = count_por_cruce if count_por_cruce else len(temp["capitulos"])

        normalizadas.append(temp)

    # Filtros sobre la lista normalizada (coinciden con los query params)
    if anio_estreno is not None:
        normalizadas = [t for t in normalizadas if t.get("anio_estreno") == anio_estreno]
    if numero_temporada is not None:
        normalizadas = [t for t in normalizadas if t.get("numero_temporada") == numero_temporada]

    # Paginación
    return normalizadas[skip: skip + limit]


@router.get("/{id}", response_model=Temporada)
def obtener_temporada_por_id(id: str):
    data = data_manager.get_data("temporadas")
    for temporada in data:
        if temporada.get("id") == id:
            # completar numero_capitulos también aquí
            num_temp = temporada.get("numero_temporada")
            temporada = dict(temporada)
            temporada["numero_capitulos"] = len(_capitulos_de_temporada(num_temp))
            temporada.setdefault("capitulos", temporada.get("capitulos", []))
            return temporada
    raise HTTPException(status_code=404, detail="Temporada no encontrada")