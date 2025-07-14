from fastapi import APIRouter
import json
from pathlib import Path

router = APIRouter(
    prefix="/personajes",
    tags=["Personajes"]
)

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "personajes.json"

@router.get("/")
def obtener_personajes():
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

@router.get("/{id}")
def obtener_personaje_por_id(id: str):
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
    for personaje in data:
        if personaje["id"] == id:
            return personaje
    return {"error": "Personaje no encontrado"}