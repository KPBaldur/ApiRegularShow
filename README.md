
# Regular Show Mini Wiki API

API pública para consultar información sobre la serie animada Regular Show: personajes, capítulos, temporadas y cómics.

---

## 🚀 **Prueba la API en Producción**
[https://tu-url-en-render.com/docs](https://tu-url-en-render.com/docs)

Usa la documentación interactiva de Swagger para explorar todos los endpoints fácilmente.

| Recurso    | Endpoint                  |
|------------|----------------------------|
| Personajes | `/personajes/`             |
| Capítulos  | `/capitulos/`              |
| Temporadas | `/temporadas/`             |
| Cómics     | `/comics/`                 |

---

## 🖥️ **Instalación local (modo desarrollador)**

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
```

📍 **Documentación local:**
http://localhost:8000/docs

---

## 📂 **Estructura del proyecto**
```
app/
├── routers/           # Endpoints (personajes, capitulos, etc.)
├── data/              # Datos JSON
├── models.py          # Modelos de datos (Pydantic)
├── main.py            # Configuración principal de la API
├── config.py          # Variables de entorno y configuración
├── errors.py          # Manejo de errores personalizados
```

---

## 🔧 **Endpoints principales**

### 📑 Personajes
- `GET /personajes`
- `GET /personajes/{id}`
- `GET /personajes/aleatorio/5`
- `GET /personajes/aleatorio/10`

### 📑 Capítulos
- `GET /capitulos`
- `GET /capitulos/{id}`

### 📑 Temporadas
- `GET /temporadas`
- `GET /temporadas/{id}`

### 📑 Cómics
- `GET /comics`
- `GET /comics/{id}`

---

## 💡 **Ejemplos de uso (producción o local)**

Obtener primeros 5 personajes:
```
GET /personajes?skip=0&limit=5
```

Buscar personajes por raza:
```
GET /personajes?raza=mapache
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