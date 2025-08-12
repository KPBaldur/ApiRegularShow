from fastapi import APIRouter, HTTPException, Query
from app.models import Comic
from typing import List, Optional, Dict, Any
from app.data.data_manager import DataManager

router = APIRouter(
    prefix="/comics",
    tags=["Comics"]
)

data_manager = DataManager()


def _normalize_comic(c: Dict[str, Any]) -> Dict[str, Any]:
    """Devuelve una copia del comic con tipos y campos normalizados."""
    cc = dict(c)

    # numero_issues como string limpio
    cc["numero_issues"] = str(cc.get("numero_issues", "")).strip()

    # listas seguras
    autores = cc.get("autores", [])
    ilustradores = cc.get("ilustradores", [])
    cc["autores"] = autores if isinstance(autores, list) else ([autores] if autores else [])
    cc["ilustradores"] = ilustradores if isinstance(ilustradores, list) else ([ilustradores] if ilustradores else [])

    # publicacion como string limpio
    cc["publicacion"] = str(cc.get("publicacion", "")).strip()

    # titulo / tipo como strings limpios por si acaso
    cc["titulo"] = str(cc.get("titulo", "")).strip()
    cc["tipo"] = str(cc.get("tipo", "")).strip()

    # id como string limpio (no cambiamos el valor, solo strip)
    cc["id"] = str(cc.get("id", "")).strip()

    return cc

# --- Endpoints --------------------------------------------------

@router.get("/", response_model=List[Comic])
def obtener_comics(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    titulo: Optional[str] = None,
    tipo: Optional[str] = None,
    autor: Optional[str] = None,
    publicacion: Optional[str] = None
):
    data = [ _normalize_comic(c) for c in data_manager.get_data("comics") ]

    if titulo:
        t = titulo.lower().strip()
        data = [c for c in data if t in c.get("titulo", "").lower()]
    if tipo:
        tp = tipo.lower().strip()
        data = [c for c in data if tp in c.get("tipo", "").lower()]
    if autor:
        a = autor.lower().strip()
        data = [c for c in data if any(a in (x or "").lower() for x in c.get("autores", []))]
    if publicacion:
        p = publicacion.strip()
        data = [c for c in data if p in c.get("publicacion", "")]

    return data[skip: skip + limit]


@router.get("/{id}", response_model=Comic)
def obtener_comic_por_id(id: str):
    id_norm = str(id).strip().upper()
    for comic in data_manager.get_data("comics"):
        c = _normalize_comic(comic)
        if c.get("id", "").upper() == id_norm:
            return c
    raise HTTPException(status_code=404, detail="Cómic no encontrado")