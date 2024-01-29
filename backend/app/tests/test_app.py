from starlette.testclient import TestClient

from main import app

client = TestClient(app)


def test_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert response.json() == {"producte1": "asdfasdfsadfdsaf"}