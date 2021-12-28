from http import HTTPStatus


def test_main(test_app):
    response = test_app.get("/items/3")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"item_id": 3}
