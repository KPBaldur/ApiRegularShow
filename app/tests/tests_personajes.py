from fastapi.testclient import TestClient
from app.main import app  # Ajusta esta ruta si tu main está en otro lugar.

client = TestClient(app)


def test_obtener_personajes_status_200():
    response = client.get("/personajes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_obtener_personajes_filtros():
    response = client.get("/personajes?nombre=Mordecai")
    assert response.status_code == 200
    data = response.json()
    assert all("Mordecai" in personaje["nombre"] for personaje in data)

def test_obtener_personajes_filtro_tipo():
    response = client.get("/personajes?tipo_personaje=Principal")
    assert response.status_code == 200
    data = response.json()
    assert all("Principal" in personaje["tipo_personaje"] for personaje in data)


def test_obtener_personajes_skip_limit():
    response = client.get("/personajes?skip=0&limit=5")
    assert response.status_code == 200
    assert len(response.json()) <= 5


def test_personajes_aleatorio_5():
    response = client.get("/personajes/aleatorio/5")
    assert response.status_code == 200
    assert len(response.json()) <= 5


def test_personajes_aleatorio_10():
    response = client.get("/personajes/aleatorio/10")
    assert response.status_code == 200
    assert len(response.json()) <= 10


def test_obtener_personaje_por_id_existente():
    response = client.get("/personajes/CHARCT001")
    assert response.status_code == 200
    assert response.json()["id"] == "CHARCT001"


def test_obtener_personaje_por_id_inexistente():
    response = client.get("/personajes/INVENTADO999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Personaje no encontrado"