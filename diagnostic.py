import sys
import os

print("=== DIAGNÓSTICO DE LA API REGULAR SHOW ===\n")

# Verificar Python y dependencias
print("1. Versión de Python:")
print(f"   Python {sys.version}")
print()

# Verificar estructura de directorios
print("2. Estructura de directorios:")
current_dir = os.getcwd()
print(f"   Directorio actual: {current_dir}")

required_dirs = ['app', 'app/routers', 'app/data', 'app/tests']
for dir_path in required_dirs:
    if os.path.exists(dir_path):
        print(f"   ✓ {dir_path}/ existe")
    else:
        print(f"   ✗ {dir_path}/ NO existe")

required_files = [
    'app/main.py',
    'app/config.py',
    'app/models.py',
    'app/errors.py',
    'app/data/data_manager.py',
    'app/data/personajes.json',
    'app/data/capitulos.json',
    'app/data/temporadas.json',
    'app/data/comics.json',
    'app/routers/personajes.py',
    'app/routers/capitulos.py',
    'app/routers/temporadas.py',
    'app/routers/comics.py'
]

print("\n3. Archivos requeridos:")
for file_path in required_files:
    if os.path.exists(file_path):
        print(f"   ✓ {file_path} existe")
    else:
        print(f"   ✗ {file_path} NO existe")

print("\n4. Verificando importaciones:")

try:
    print("   Probando importación de FastAPI...")
    import fastapi
    print(f"   ✓ FastAPI {fastapi.__version__} importado correctamente")
except ImportError as e:
    print(f"   ✗ Error importando FastAPI: {e}")

try:
    print("   Probando importación de uvicorn...")
    import uvicorn
    print(f"   ✓ Uvicorn importado correctamente")
except ImportError as e:
    print(f"   ✗ Error importando uvicorn: {e}")

try:
    print("   Probando importación de pydantic...")
    import pydantic
    print(f"   ✓ Pydantic {pydantic.__version__} importado correctamente")
except ImportError as e:
    print(f"   ✗ Error importando pydantic: {e}")

print("\n5. Verificando módulos de la aplicación:")

try:
    print("   Probando importación de app.config...")
    from app.config import settings
    print(f"   ✓ app.config importado correctamente")
    print(f"   ✓ app_name: {settings.app_name}")
except ImportError as e:
    print(f"   ✗ Error importando app.config: {e}")

try:
    print("   Probando importación de app.models...")
    from app.models import Personaje, Capitulo, Temporada, Comic
    print(f"   ✓ app.models importado correctamente")
except ImportError as e:
    print(f"   ✗ Error importando app.models: {e}")

try:
    print("   Probando importación de app.data.data_manager...")
    from app.data.data_manager import DataManager
    print(f"   ✓ app.data.data_manager importado correctamente")
except ImportError as e:
    print(f"   ✗ Error importando app.data.data_manager: {e}")

try:
    print("   Probando importación de app.errors...")
    from app.errors import configure_error_handlers
    print(f"   ✓ app.errors importado correctamente")
except ImportError as e:
    print(f"   ✗ Error importando app.errors: {e}")

print("\n6. Verificando routers:")

routers = ['personajes', 'capitulos', 'temporadas', 'comics']
for router_name in routers:
    try:
        print(f"   Probando importación de app.routers.{router_name}...")
        module = __import__(f'app.routers.{router_name}', fromlist=['router'])
        print(f"   ✓ app.routers.{router_name} importado correctamente")
    except ImportError as e:
        print(f"   ✗ Error importando app.routers.{router_name}: {e}")

print("\n7. Verificando datos JSON:")

json_files = ['personajes', 'capitulos', 'temporadas', 'comics']
for json_name in json_files:
    try:
        import json
        with open(f'app/data/{json_name}.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"   ✓ {json_name}.json cargado correctamente ({len(data)} elementos)")
    except Exception as e:
        print(f"   ✗ Error cargando {json_name}.json: {e}")

print("\n=== FIN DEL DIAGNÓSTICO ===") 