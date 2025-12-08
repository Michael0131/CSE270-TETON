import requests

BASE_URL = "https://michael0131.github.io/CSE270-TETON/"

def test_users_valid_credentials():
    response = requests.get(f"{BASE_URL}/users/", params={
        "username": "admin",
        "password": "qwerty"
    })
    assert response.status_code == 200
    assert response.text == ""

def test_users_invalid_credentials():
    response = requests.get(f"{BASE_URL}/users/", params={
        "username": "admin",
        "password": "admin"
    })
    assert response.status_code == 401
    assert response.text == ""
