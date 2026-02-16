import requests
import pytest

url = "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="module")
def created_user():
    payload = {
        "name": "Jayanta",
        "email": "jayanta@email.com",
        "balance": 5000
    }

    response = requests.post(f"{url}/users", json=payload)

    assert response.status_code == 201
    return response.json()["id"]
# GET Test
def test_get_customer():
    response = requests.get(f"{url}/users/1")

    assert response.status_code == 200
# PUT Test
def test_update_customer():
    payload = {"email": "updated@email.com"}

    response = requests.put(f"{url}/users/1", json=payload)

    assert response.status_code == 200
    assert response.json()["email"] == payload["email"]
# DELETE Test
def test_delete_customer():
    response = requests.delete(f"{url}/users/1")

    assert response.status_code == 200