# 📺 Regular Show Mini Wiki API
![API Deploy](https://img.shields.io/badge/Deployed-Render-2ea44f?logo=render&logoColor=white)

Una API RESTful desarrollada con **FastAPI** para consultar información completa sobre
la serie **"Regular Show"** (Un Show Más): personajes, capítulos, temporadas y cómics.

> ⚡ Recurso educativo y de referencia para desarrolladores y fans.

---

## 🚀 **Producción y Documentación**
- 📘 **Documentación oficial (Wiki)**: https://kpbaldur.github.io/RegularShowWiki
- 🔎 **Esquema OpenAPI (machine-readable)**: `GET /openapi.json` (desde tu servidor)
- 🧭 **Redirecciones**:
  - `GET /` → redirige a la Wiki
  - `GET /docs` → redirige a la Wiki (`/docs`)
  - `GET /redoc` → redirige a la Wiki (`/docs`)

> Nota: El Swagger/Redoc **interno** de FastAPI está deshabilitado. Usa la Wiki para navegar la documentación. La Wiki puede consumir `/openapi.json` si lo necesita.

---

## 📦 Estructura del Proyecto

app/
├── main.py # Punto de entrada de la API (con redirecciones a la Wiki)
├── config.py # Configuración (.env: DEBUG, ALLOWED_ORIGINS, etc.)
├── errors.py # Manejo centralizado de errores
├── models.py # Esquemas Pydantic
├── data/
│ ├── personajes.json
│ ├── capitulos.json
│ ├── temporadas.json
│ └── comics.json
├── data_manager.py # Singleton de datos con normalización ligera
└── routers/
├── personajes.py
├── capitulos.py
├── temporadas.py
└── comics.py

---

## Instalacion y ejecucion local

### 1️⃣ Clona el repositorio:
```bash
git clone https://github.com/KPBaldur/ApiRegularShow.git
cd ApiRegularShow
```

### 2️⃣ Crea y activa un entorno virtual:
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
```

### 3️⃣ Instala las dependencias:
```bash
pip install -r requirements.txt
```

### 4️⃣ Ejecuta el servidor local:
```bash
uvicorn app.main:app --reload
### O tambien con este:
python -m uvicorn app.main:app --reload
```

## Documentación local: redirigirá a la Wiki

Esquema: http://localhost:8000/openapi.json

---

## 📚 Endpoints por recurso
Parametros comunes:  skip, limit (paginación).
as respuestas estan validadas por Pydantic

---

### 👤 /personajes

#### `GET /personajes`

Parámetros opcionales:
-`filtros`: `nombre`, `raza`, `tipo_personaje`, `estado`, `capitulo_aparicion`

#### `GET /personajes/todos`
Retorna todos los personajes sin paginación ni filtros.

#### `GET /personajes/aleatorio/6`
Devuelve 6 personajes aleatorios.

#### `GET /personajes/aleatorio/10`
Devuelve 10 personajes aleatorios.

#### `GET /personajes/{id}`
Busca un personaje por su ID (e.g., `CHARCT001`).

---

### 📚 /capitulos

#### `GET /capitulos`
Permite listar capítulos con filtros:

Parámetros:
- `skip`, `limit`
- `titulo`, `temporada`, `anio_emision`, `rating_min`, `rating_max`

#### `GET /capitulos/{id}`
Consulta un capítulo por su ID (e.g., `CAP001TEMP01`).

---

### 📖 /temporadas

#### `GET /temporadas`
Listado de temporadas con filtros por:
- `anio_estreno`
- `numero_temporada`

#### `GET /temporadas/{id}`
Consulta una temporada por su ID (e.g., `TEMP03`).

--

### 📘 /comics

#### `GET /comics`
Listado de cómics con filtros:

Parámetros:
- `titulo`, `tipo`, `autor`, `publicacion`

#### `GET /comics/{id}` 
Consulta un cómic por su ID (e.g., `COMC001`).

---

## 💡 **Ejemplos de uso (producción o local)**

Obtener 5 personajes:
-`GET /personajes?skip=0&limit=5`

Filtrar capítulos por temporada:
-`GET /capitulos?temporada=8`

Top 10 capítulos por puntaje descendente:
-`GET /capitulos/top?limit=10&sort_by=imdb_score&order=desc`

Resumen de temporadas:
-`GET /temporadas/resumen`

---

## 📌 Consideraciones

- La API no usa una base de datos tradicional. Todos los datos están alojados en archivos `.json` para facilitar su lectura y modificación.
- Es posible integrar bases de datos reales como PostgreSQL o MongoDB en el futuro.

---

## 🔔 **Preguntas frecuentes (FAQ)**

### ❓ ¿Por qué /docs no muestra Swagger local?
Redirigimos la documentación a la Wiki. El esquema sigue disponible en /openapi.json.

### ❓ ¿Cómo reporto un problema?
Abre un issue en este repositorio o contáctame.

---

## 📃 **Licencia**
MIT License

---

## 👨‍💻 **Contacto**
Kevin Pizarro  
[Repositorio GitHub: ApiRegularShow](https://github.com/KPBaldur/ApiRegularShow)

---

## 📝 **Términos de Servicio**
- Puedes usar esta API con fines educativos, personales o no comerciales.
- Si la usas en público, otorga créditos al creador.
- No garantizo disponibilidad continua ni soporte.
- No puedes revender la API como propia.

---

### 🚩 **Nota final para usuarios:**
Esta API es un proyecto fan, no oficial. Es solo para fines de práctica, educación y compartir el amor por Regular Show. 🎮✨