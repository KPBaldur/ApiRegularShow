from fastapi import APIRouter
import json
from pathlib import Path

router = APIRouter(
    prefix="/comics",
    tags=["Comics"]
)

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "comics.json"

@router.get("/")
def obtener_comics():
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

@router.get("/{id}")
def obtener_comic_por_id(id: str):
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
    for comic in data:
        if comic["id"] == id:
            return comic
    return {"error": "Cómic no encontrado"}