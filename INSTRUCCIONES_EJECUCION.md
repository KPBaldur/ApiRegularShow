# 🚀 Instrucciones para Ejecutar la API Regular Show

## 📋 Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## 🔧 Instalación y Configuración

### 1. Clonar el repositorio (si no lo has hecho)
```bash
git clone https://github.com/KPBaldur/ApiRegularShow.git
cd ApiRegularShow
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

## 🎯 Métodos de Ejecución

### Método 1: Usando el script de inicio (Recomendado)
```bash
python start_server.py
```

### Método 2: Usando el archivo batch (Windows)
```cmd
start_server.bat
```

### Método 3: Usando uvicorn directamente
```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

### Método 4: Usando cmd (Windows)
```cmd
cmd
cd C:\Users\Casa\Documents\GitHub\ApiRegularShow
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

## 🌐 Acceso a la API

Una vez que el servidor esté ejecutándose:

- **API Base**: http://127.0.0.1:8000
- **Documentación Swagger**: http://127.0.0.1:8000/docs
- **Documentación ReDoc**: http://127.0.0.1:8000/redoc

## 📊 Endpoints Disponibles

### Personajes
- `GET /personajes` - Listar personajes
- `GET /personajes/{id}` - Obtener personaje por ID
- `GET /personajes/aleatorio/6` - 6 personajes aleatorios
- `GET /personajes/aleatorio/10` - 10 personajes aleatorios

### Capítulos
- `GET /capitulos` - Listar capítulos
- `GET /capitulos/{id}` - Obtener capítulo por ID
- `GET /capitulos/top` - Top capítulos por puntuación

### Temporadas
- `GET /temporadas` - Listar temporadas
- `GET /temporadas/{id}` - Obtener temporada por ID

### Cómics
- `GET /comics` - Listar cómics
- `GET /comics/{id}` - Obtener cómic por ID

## 🔍 Filtros Disponibles

### Personajes
- `?nombre=texto` - Filtrar por nombre
- `?raza=texto` - Filtrar por raza
- `?tipo_personaje=Principal|Secundario|Antagonista` - Filtrar por tipo
- `?profesion=texto` - Filtrar por profesión
- `?skip=0&limit=10` - Paginación

### Capítulos
- `?titulo=texto` - Filtrar por título
- `?temporada=1` - Filtrar por temporada
- `?numero=1` - Filtrar por número de capítulo

### Temporadas
- `?anio_estreno=2010` - Filtrar por año
- `?numero_temporada=1` - Filtrar por número

### Cómics
- `?titulo=texto` - Filtrar por título
- `?tipo=principal` - Filtrar por tipo
- `?autor=nombre` - Filtrar por autor
- `?publicacion=2013` - Filtrar por año

## 🧪 Ejecutar Pruebas

```bash
# Instalar pytest si no está instalado
pip install pytest

# Ejecutar todas las pruebas
python -m pytest app/tests/ -v

# Ejecutar pruebas específicas
python -m pytest app/tests/tests_personajes.py -v
```

## 🐛 Solución de Problemas

### Error: "No module named 'fastapi'"
```bash
pip install fastapi uvicorn
```

### Error: "No module named 'httpx'"
```bash
pip install httpx
```

### Error: "Port already in use"
Cambia el puerto en el comando:
```bash
uvicorn app.main:app --reload --port 8001
```

### Error: "Permission denied"
Ejecuta como administrador o cambia el puerto.

### PowerShell da problemas
Usa cmd en lugar de PowerShell:
```cmd
cmd
python start_server.py
```

## 📝 Notas Importantes

- La API incluye **60 personajes** con información completa
- Todos los personajes tienen el campo `tipo_personaje` (Principal, Secundario, Antagonista)
- Se eliminó el campo `estado` como se solicitó
- La API está configurada con CORS para permitir acceso desde cualquier origen
- La documentación interactiva está disponible en `/docs`

## 🆘 Contacto

Si tienes problemas, revisa:
1. Que estés en el directorio correcto
2. Que todas las dependencias estén instaladas
3. Que no haya otro proceso usando el puerto 8000
4. Los logs de error en la consola 