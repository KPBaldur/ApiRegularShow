# app/data/data_manager.py
from pathlib import Path
import json

class DataManager:
    _instance = None
    _data = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataManager, cls).__new__(cls)
            cls._load_data()
        return cls._instance

    @classmethod
    def _load_data(cls):
        # Aquí corregimos la ruta para que apunte a /data correctamente
        data_path = Path(__file__).resolve().parent
        
        cls._data["personajes"] = json.load(open(data_path / "personajes.json", "r", encoding="utf-8"))
        cls._data["capitulos"] = json.load(open(data_path / "capitulos.json", "r", encoding="utf-8"))
        cls._data["temporadas"] = json.load(open(data_path / "temporadas.json", "r", encoding="utf-8"))
        cls._data["comics"] = json.load(open(data_path / "comics.json", "r", encoding="utf-8"))

    def get_data(self, collection):
        return self._data.get(collection, [])