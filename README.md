# 📺 Regular Show Mini Wiki API
![API Deploy](https://img.shields.io/badge/Deployed-Render-2ea44f?logo=render&logoColor=white)

Una API RESTful desarrollada con **FastAPI** para consultar informacion completa sobre
la serie **"Regular Show"** (Un Show Mas), incluyendo personajes, capitulos,
temporadas y comics.

> ⚡ Esta API está pensada como recurso educativo y de referencia para desarrolladores y fans.

---

## 🚀 **Prueba la API en Producción y documentacion Swagger**
- [📘 Documentación Swagger](http://localhost:8000/docs)
- [🌐 Web Wiki Frontend](https://kpbaldur.github.io/RegularShowWiki/index.html) — Página que consume esta API y entrega más contexto visual.

Usa la documentación interactiva de Swagger para explorar todos los endpoints fácilmente.

| Recurso    | Endpoint                  |
|------------|----------------------------|
| Personajes | `/personajes/`             |
| Capítulos  | `/capitulos/`              |
| Temporadas | `/temporadas/`             |
| Cómics     | `/comics/`                 |

---

## 📦 Estructura del Proyecto

```
app/
├── main.py               # Punto de entrada de la API
├── config.py             # Configuración general
├── errors.py             # Manejo centralizado de errores
├── models.py             # Esquemas Pydantic para validación
├── data/
│   ├── personajes.json
│   ├── capitulos.json
│   ├── temporadas.json
│   └── comics.json
├── routers/
│   ├── personajes.py
│   ├── capitulos.py
│   ├── temporadas.py
│   └── comics.py
└── data_manager.py       # Singleton para acceder a los datos

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

📍 **Documentación local:**
http://localhost:8000/docs

---

## 📚 Endpoints por recurso

---

### 👤 /personajes

#### `GET /personajes`
Consulta personajes con paginación y filtros opcionales.

Parámetros opcionales:
- `skip`: desde qué índice comenzar (por defecto 0)
- `limit`: cuántos personajes devolver (por defecto 10)
- `nombre`, `raza`, `tipo_personaje`, `profesion`: filtros parciales

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

Obtener primeros 5 personajes:
```
GET /personajes?skip=0&limit=5
```

Filtrar capítulos por temporada:
```
GET /capitulos?temporada=1
```

Obtener cómics de 2014:
```
GET /comics?publicacion=2014
```

---

## 📌 Consideraciones

- La API no usa una base de datos tradicional. Todos los datos están alojados en archivos `.json` para facilitar su lectura y modificación.
- Es posible integrar bases de datos reales como PostgreSQL o MongoDB en el futuro.

---

## 🔔 **Preguntas frecuentes (FAQ)**

### ❓ ¿Por qué me devuelve 404 en `/`?
La API está pensada para usarse vía `/docs` o directamente por los endpoints.

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