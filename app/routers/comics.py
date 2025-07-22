from fastapi import APIRouter, HTTPException, Query
from app.models import Comic
from typing import List, Optional
from app.data.data_manager import DataManager

router = APIRouter(
    prefix="/comics",
    tags=["Comics"]
)

data_manager = DataManager()


@router.get("/", response_model=List[Comic])
def obtener_comics(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    titulo: Optional[str] = None,
    tipo: Optional[str] = None,
    autor: Optional[str] = None,
    publicacion: Optional[str] = None
):
    data = data_manager.get_data("comics")

    if titulo:
        data = [c for c in data if titulo.lower() in c["titulo"].lower()]
    if tipo:
        data = [c for c in data if tipo.lower() in c["tipo"].lower()]
    if autor:
        data = [c for c in data if any(autor.lower() in a.lower() for a in c["autores"])]
    if publicacion:
        data = [c for c in data if publicacion in c["publicacion"]]

    return data[skip:skip + limit]


@router.get("/{id}", response_model=Comic)
def obtener_comic_por_id(id: str):
    data = data_manager.get_data("comics")
    for comic in data:
        if comic["id"] == id:
            return comic
    raise HTTPException(status_code=404, detail="Cómic no encontrado")