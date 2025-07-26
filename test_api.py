from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

# Probar endpoint principal
response = client.get('/personajes')
print(f'Status: {response.status_code}')
print(f'Total personajes (primeros 10): {len(response.json())}')

# Probar filtro por tipo de personaje
response = client.get('/personajes?tipo_personaje=Principal')
print(f'Status: {response.status_code}')
print(f'Personajes principales: {len(response.json())}')

# Probar filtro por raza
response = client.get('/personajes?raza=mapache')
print(f'Status: {response.status_code}')
print(f'Personajes mapache: {len(response.json())}')

# Probar endpoint aleatorio
response = client.get('/personajes/aleatorio/6')
print(f'Status: {response.status_code}')
print(f'Personajes aleatorios: {len(response.json())}')

# Probar personaje específico
response = client.get('/personajes/CHARCT001')
print(f'Status: {response.status_code}')
if response.status_code == 200:
    personaje = response.json()
    print(f'Personaje: {personaje["nombre"]} - {personaje["tipo_personaje"]}') 