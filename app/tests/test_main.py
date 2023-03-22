from fastapi.testclient import TestClient

from flask import Flask, request, jsonify

from app.main import app

client = TestClient(app)


# def test_read_main():
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"Hello": "World1"}

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World1"}

def test_callname():
    name = "pajjaree1"
    response = client.get(f"/callname/{name}")
    assert response.status_code == 200
    assert response.json() == {"hello": name}

# def test_callname():
#     name = "pajjaree"
#     response = client.post("/callname", json={"name": name})
#     assert response.status_code == 200
#     assert response.json() == {"hello": name}

def test_callname():
    data = request.json
    name = data['pajjaree']
    response = {"hello": name}
    return jsonify(response)
