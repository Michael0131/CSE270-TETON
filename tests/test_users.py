import requests

BASE_URL = "https://michael0131.github.io/CSE270-TETON/"

def test_users_valid_credentials():
    response = requests.get(f"{BASE_URL}/data/users.json")
    assert response.status_code == 200

    users = response.json()

    assert "admin" in users
    assert users["admin"]["password"] == "qwerty"


def test_users_invalid_credentials():
    response = requests.get(f"{BASE_URL}/data/users.json")
    assert response.status_code == 200

    users = response.json()

    assert "not_a_real_user" not in users
