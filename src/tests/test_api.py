from http import HTTPStatus

from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_main():
    response = client.get("/items/3")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"item_id": 3}
