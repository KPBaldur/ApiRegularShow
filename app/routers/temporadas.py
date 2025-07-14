from fastapi import APIRouter
import json
from pathlib import Path

router = APIRouter(
    prefix="/temporadas",
    tags=["Temporadas"]
)

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "temporadas.json"

@router.get("/")
def obtener_temporadas():
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

@router.get("/{id}")
def obtener_temporada_por_id(id: str):
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
    for temporada in data:
        if temporada["id"] == id:
            return temporada
    return {"error": "Temporada no encontrada"}