from pydantic import BaseModel, Field
from typing import List, Optional

class Personaje(BaseModel):
    id: str = Field(..., description="ID único del personaje", example="CHARCT001")
    nombre: str = Field(..., description="Nombre completo del personaje", example="Mordecai (Mordecai)")
    nombre_ingles: str = Field(..., description="Nombre en inglés", example="Mordecai")
    nombre_latino: str = Field(..., description="Nombre en español latino", example="Mordecai")
    raza: str = Field(..., description="Raza o especie del personaje", example="Arrendajo azul")
    profesion: str = Field(..., description="Profesión u ocupación", example="Guardabosques del parque, artista")
    capitulo_aparicion: str = Field(..., description="Primer capítulo de aparición", example="The Power (S01E01)")
    comic_aparicion: str = Field(..., description="Primer cómic de aparición o información relevante", example="Aparece en todos los cómics de Regular Show")
    tipo_personaje: str = Field(..., description="Relevancia del personaje", example="Principal")
    imagen_url: str = Field(..., description="URL de la imagen del personaje", example="https://i.imgur.com/abcd123.png")

class Capitulo(BaseModel):
    id: str = Field(..., description="ID único del capítulo", example="CAP001")
    titulo_eng: str = Field(..., description="Título del capítulo en inglés", example="The Power")
    titulo_es: str = Field(..., description="Título del capítulo en español", example="El poder")
    temporada: int = Field(..., description="Número de temporada", example=1)
    numero: int = Field(..., description="Número de capítulo en la temporada", example=1)
    fecha_estreno: str = Field(..., description="Fecha de estreno (YYYY-MM-DD)", example="2010-09-06")
    sinopsis: str = Field(..., description="Resumen del capítulo", example="Mordecai y Rigby encuentran un teclado mágico...")
    imdb_score: float = Field(..., description="Puntaje IMDb del capítulo", example=8.6)
    imagen_url: Optional[str] = Field(..., description="URL de la imagen del capítulo", example="https://cdn.regularshow.com/capitulos/thepower.jpg")


class Temporada(BaseModel):
    id: str = Field(..., description="ID único de la temporada", example="TEMP01")
    numero_temporada: int = Field(..., description="Número de la temporada", example=1)
    numero_capitulos: int = Field(..., description="Cantidad de capítulos en la temporada", example=12)
    anio_estreno: int = Field(..., description="Año de estreno", example=2010)
    resumen: str = Field(..., description="Resumen de la temporada", example="Mordecai y Rigby, dos amigos flojos...")
    capitulos: Optional[List[str]] = Field(default_factory=list, description="ID's de capitulos de la temporada", example=["CAP001", "CAP002"])


class Comic(BaseModel):
    id: str = Field(..., description="ID único del cómic", example="COMC001")
    titulo: str = Field(..., description="Título del cómic", example="Manic Moshers")
    tipo: str = Field(..., description="Tipo de cómic (principal, especial, etc.)", example="principal")
    numero_issues: str = Field(..., description="Números de issues incluidos", example="1-2")
    autores: List[str] = Field(..., description="Lista de autores", example=["KC Green"])
    ilustradores: List[str] = Field(..., description="Lista de ilustradores", example=["Al Strejlau"])
    publicacion: str = Field(..., description="Año de publicación", example="2013")