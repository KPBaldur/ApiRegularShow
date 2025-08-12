from pathlib import Path
import json
from copy import deepcopy
from typing import Any, Dict, List


class DataManager:
    """
    Carga y sirve colecciones JSON en memoria.
    - Carga segura con manejo de errores.
    - get_data -> devuelve COPIA para evitar mutaciones accidentales.
    - reload() -> recarga los JSON (útil en desarrollo).
    - Normalización ligera en 'personajes' (trim) y en 'temporadas' (capitulos como lista).
    """
    _instance = None
    _data: Dict[str, List[Dict[str, Any]]] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._load_data()
        return cls._instance

    # -------------------------
    # Normalizadores (ligeros)
    # -------------------------

    @staticmethod
    def _trim_str(value: Any) -> Any:
        return value.strip() if isinstance(value, str) else value

    @classmethod
    def _normalize_personaje(cls, p: Dict[str, Any]) -> Dict[str, Any]:
        # Solo recorte de espacios en campos de texto conocidos (evita "CJ ").
        fields_to_trim = [
            "id", "nombre", "nombre_ingles", "nombre_latino",
            "raza", "profesion", "capitulo_aparicion",
            "comic_aparicion", "tipo_personaje", "imagen_url"
        ]
        out = dict(p)
        for k in fields_to_trim:
            if k in out:
                out[k] = cls._trim_str(out[k])
        return out

    @classmethod
    def _normalize_temporada(cls, t: Dict[str, Any]) -> Dict[str, Any]:
        out = dict(t)
        # Asegurar lista de capitulos si faltara (defensivo a futuro)
        if "capitulos" not in out or out["capitulos"] is None:
            out["capitulos"] = []
        elif not isinstance(out["capitulos"], list):
            out["capitulos"] = [out["capitulos"]]
        return out

    # -------------------------
    # Carga de datos
    # -------------------------

    @classmethod
    def _load_data(cls):
        data_path = Path(__file__).resolve().parent

        try:
            with open(data_path / "personajes.json", "r", encoding="utf-8") as f:
                personajes = json.load(f)
                # Normalización ligera
                cls._data["personajes"] = [cls._normalize_personaje(p) for p in personajes]

            with open(data_path / "capitulos.json", "r", encoding="utf-8") as f:
                cls._data["capitulos"] = json.load(f)

            with open(data_path / "temporadas.json", "r", encoding="utf-8") as f:
                temporadas = json.load(f)
                cls._data["temporadas"] = [cls._normalize_temporada(t) for t in temporadas]

            with open(data_path / "comics.json", "r", encoding="utf-8") as f:
                cls._data["comics"] = json.load(f)

        except FileNotFoundError as e:
            # Error claro si falta algún archivo
            raise RuntimeError(f"Archivo de datos faltante: {e.filename}") from e
        except json.JSONDecodeError as e:
            # Error claro si un JSON está mal formado
            raise RuntimeError(f"JSON inválido (línea {e.lineno}, columna {e.colno}).") from e

    @classmethod
    def reload(cls):
        """Recarga las colecciones desde disco (útil en desarrollo)."""
        cls._load_data()

    # -------------------------
    # Acceso de solo lectura
    # -------------------------

    def get_data(self, collection: str) -> List[Dict[str, Any]]:
        """
        Devuelve una COPIA de la colección solicitada para evitar mutaciones accidentales.
        Colecciones disponibles: 'personajes', 'capitulos', 'temporadas', 'comics'.
        """
        return deepcopy(self._data.get(collection, []))
