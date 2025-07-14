from fastapi import APIRouter
import json
from pathlib import Path

router = APIRouter(
    prefix="/capitulos",
    tags=["Capitulos"]
)

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "capitulos.json"

@router.get("/")
def obtener_capitulos():
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

@router.get("/{id}")
def obtener_capitulo_por_id(id: str):
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
    for capitulo in data:
        if capitulo["id"] == id:
            return capitulo
    return {"error": "Capítulo no encontrado"}