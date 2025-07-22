from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_obtener_temporadas_status_200():
    response = client.get("/temporadas")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_obtener_temporadas_filtros_anio():
    response = client.get("/temporadas?anio_estreno=2010")
    assert response.status_code == 200
    data = response.json()
    assert all(temporada["anio_estreno"] == 2010 for temporada in data)


def test_obtener_temporadas_filtros_numero():
    response = client.get("/temporadas?numero_temporada=1")
    assert response.status_code == 200
    data = response.json()
    assert all(temporada["numero_temporada"] == 1 for temporada in data)


def test_obtener_temporadas_skip_limit():
    response = client.get("/temporadas?skip=0&limit=3")
    assert response.status_code == 200
    assert len(response.json()) <= 3


def test_obtener_temporada_por_id_existente():
    response = client.get("/temporadas/TEMP01")
    assert response.status_code == 200
    assert response.json()["id"] == "TEMP01"


def test_obtener_temporada_por_id_inexistente():
    response = client.get("/temporadas/INVENTADA999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Temporada no encontrada"
