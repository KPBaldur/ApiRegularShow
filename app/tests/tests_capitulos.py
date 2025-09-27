from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_obtener_capitulos_status_200():
    response = client.get("/capitulos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_obtener_capitulos_filtro_titulo():
    response = client.get("/capitulos?titulo=The Power")
    assert response.status_code == 200
    data = response.json()
    assert all("the power" in cap["titulo_eng"].lower() or "the power" in cap.get("titulo_es", "").lower() for cap in data)


def test_obtener_capitulos_filtro_temporada():
    response = client.get("/capitulos?temporada=1")
    assert response.status_code == 200
    data = response.json()
    assert all(cap["temporada"] == 1 for cap in data)


def test_obtener_capitulos_filtro_numero():
    response = client.get("/capitulos?numero=1")
    assert response.status_code == 200
    data = response.json()
    assert all(cap["numero"] == 1 for cap in data)


def test_obtener_capitulos_skip_limit():
    response = client.get("/capitulos?skip=0&limit=5")
    assert response.status_code == 200
    assert len(response.json()) <= 5


def test_obtener_capitulo_por_id_existente():
    response = client.get("/capitulos/CAP001TEMP01")
    assert response.status_code == 200
    assert response.json()["id"] == "CAP001TEMP01"


def test_obtener_capitulo_por_id_inexistente():
    response = client.get("/capitulos/INVENTADO999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Capítulo no encontrado"


def test_buscar_capitulo_por_titulo_ingles():
    response = client.get("/capitulos/nombre/The Power")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0


def test_buscar_capitulo_por_titulo_espanol():
    response = client.get("/capitulos/nombre/El Poder")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
