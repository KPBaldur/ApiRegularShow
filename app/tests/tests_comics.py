from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_obtener_comics_status_200():
    response = client.get("/comics")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_obtener_comics_filtros_titulo():
    response = client.get("/comics?titulo=Manic")
    assert response.status_code == 200
    data = response.json()
    assert all("manic" in comic["titulo"].lower() for comic in data)


def test_obtener_comics_filtros_tipo():
    response = client.get("/comics?tipo=principal")
    assert response.status_code == 200
    data = response.json()
    assert all("principal" in comic["tipo"].lower() for comic in data)


def test_obtener_comics_filtros_autor():
    response = client.get("/comics?autor=KC Green")
    assert response.status_code == 200
    data = response.json()
    assert any("KC Green" in autor for comic in data for autor in comic["autores"])


def test_obtener_comics_skip_limit():
    response = client.get("/comics?skip=0&limit=3")
    assert response.status_code == 200
    assert len(response.json()) <= 3


def test_obtener_comic_por_id_existente():
    response = client.get("/comics/COMC001")
    assert response.status_code == 200
    assert response.json()["id"] == "COMC001"


def test_obtener_comic_por_id_inexistente():
    response = client.get("/comics/INVENTADO999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Cómic no encontrado"
