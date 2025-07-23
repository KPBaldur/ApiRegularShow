from fastapi import APIRouter, HTTPException, Query
from app.models import Capitulo
from typing import List, Optional
from app.data.data_manager import DataManager

router = APIRouter(
    prefix="/capitulos",
    tags=["Capitulos"]
)

data_manager = DataManager()

@router.get("/", response_model=List[Capitulo])
def obtener_capitulos(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    titulo: Optional[str] = None,
    temporada: Optional[int] = None,
    numero: Optional[int] = None
):
    data = data_manager.get_data("capitulos")

    if titulo:
        data = [c for c in data if titulo.lower() in c["titulo"].lower()]
    if temporada:
        data = [c for c in data if c["temporada"] == temporada]
    if numero:
        data = [c for c in data if c["numero"] == numero]

    return data[skip:skip + limit]

@router.get("/{id}", response_model=Capitulo)
def obtener_capitulo_por_id(id: str):
    data = data_manager.get_data("capitulos")
    for capitulo in data:
        if capitulo["id"] == id:
            return capitulo
    raise HTTPException(status_code=404, detail="Capítulo no encontrado")

@router.get("/top", response_model=List[Capitulo])
def obtener_top_capitulos(limit: int = 10):
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
    data.sort(key=lambda c: c.get("IMDb_score", 0), reverse=True)
    return data[:limit]