# Regular Show Mini Wiki API

API pública para consultar información sobre la serie animada Regular Show: personajes, capítulos, temporadas y cómics.

## Características
- Consulta de personajes, capítulos, temporadas y cómics
- Filtros y paginación en todos los endpoints
- Respuestas en formato JSON
- Documentación automática con Swagger y Redoc

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/KevinP-Antartica/ApiRegularShow.git
   cd ApiRegularShow
   ```
2. Crea y activa un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   venv\Scripts\activate  # En Windows
   source venv/bin/activate  # En Linux/Mac
   ```
3. Instala las dependencias:
   ```bash
   pip install fastapi uvicorn
   ```

## Ejecución

Lanza el servidor de desarrollo con:
```bash
uvicorn app.main:app --reload
```

La API estará disponible en: [http://localhost:8000](http://localhost:8000)

- Documentación Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)
- Documentación Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## ¿Cómo funciona la API?

La API lee datos desde archivos JSON ubicados en la carpeta `app/data/`. Cada endpoint accede a su archivo correspondiente y permite filtrar, buscar y paginar los resultados.  
La documentación interactiva está disponible en `/docs` y describe todos los modelos y parámetros.

**Estructura del proyecto:**
- `app/routers/`: Endpoints de la API.
- `app/data/`: Archivos de datos en formato JSON.
- `app/models.py`: Modelos de datos (Pydantic).
- `app/main.py`: Configuración principal de la API.

**Ejemplo de respuesta para `/personajes/CHARCT001`:**
```json
{
  "id": "CHARCT001",
  "nombre": "Mordecai (Mordecai)",
  "nombre_ingles": "Mordecai",
  "nombre_latino": "Mordecai",
  "raza": "Arrendajo azul",
  "profesion": "Guardabosques del parque, artista",
  "capitulo_aparicion": "The Power (S01E01)",
  "comic_aparicion": "Aparece en todos los cómics de Regular Show",
  "estado": "Vivo"
}
```

---

## Endpoints principales

### Personajes
- `GET /personajes` — Lista de personajes (filtros: nombre, raza, estado, profesión; paginación: skip, limit)
- `GET /personajes/{id}` — Detalle de personaje por ID
- `GET /personajes/aleatorio/5` — 5 personajes aleatorios
- `GET /personajes/aleatorio/10` — 10 personajes aleatorios

### Capítulos
- `GET /capitulos` — Lista de capítulos (filtros: título, temporada, número; paginación)
- `GET /capitulos/{id}` — Detalle de capítulo por ID

### Temporadas
- `GET /temporadas` — Lista de temporadas (filtros: año de estreno, número de temporada; paginación)
- `GET /temporadas/{id}` — Detalle de temporada por ID

### Cómics
- `GET /comics` — Lista de cómics (filtros: título, tipo, autor, año de publicación; paginación)
- `GET /comics/{id}` — Detalle de cómic por ID

---

## Ejemplos de uso

- Obtener los primeros 5 personajes:
  ```http
  GET /personajes?skip=0&limit=5
  ```
- Buscar personajes por raza:
  ```http
  GET /personajes?raza=mapache
  ```
- Filtrar capítulos por temporada:
  ```http
  GET /capitulos?temporada=1
  ```
- Obtener cómics publicados en 2014:
  ```http
  GET /comics?publicacion=2014
  ```

---

## Preguntas frecuentes (FAQ)

- **¿Qué hago si un endpoint devuelve una lista vacía?**
  - Significa que no hay datos que coincidan con los filtros aplicados. Prueba con otros parámetros o revisa la ortografía.
- **¿Cómo reporto un error o sugerencia?**
  - Puedes abrir un issue en el repositorio de GitHub o contactar al mantenedor vía email.

---

## Ejercicios prácticos

### Básicos
- Listar todos los personajes:  
  `GET /personajes`
- Buscar personajes por nombre:  
  `GET /personajes?nombre=rigby`
- Listar capítulos de la temporada 1:  
  `GET /capitulos?temporada=1`
- Listar cómics publicados en 2013:  
  `GET /comics?publicacion=2013`

### Intermedios
- Filtrar personajes vivos de raza “mapache”:  
  `GET /personajes?raza=mapache&estado=vivo`
- Listar títulos de capítulos de la temporada 2:  
  `GET /capitulos?temporada=2`
- Buscar cómics de tipo “principal” por autor “KC Green”:  
  `GET /comics?tipo=principal&autor=KC Green`
- Recorrer personajes de 5 en 5:  
  `GET /personajes?skip=0&limit=5`, luego `skip=5`, etc.

### Avanzados
- Script para mostrar un personaje aleatorio cada día usando `/personajes/aleatorio/5` y seleccionando uno.
- Obtener todos los personajes que aparecen en capítulos de la temporada 2 (requiere combinar datos de `/capitulos` y `/personajes`).
- Crear un dashboard con estadísticas usando los endpoints de la API.
- Integrar la API con un frontend para mostrar información dinámica y filtrada.

---

## Licencia
MIT 