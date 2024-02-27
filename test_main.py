import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def assert_almost_equal(actual, expected, tolerance=0.001):
    assert abs(actual - expected) < tolerance

def test_convert_currency():
    response = client.get("/convert/?from_currency=USD&to_currency=BRL&amount=100")
    assert response.status_code == 200
    assert_almost_equal(response.json()["result"], 530.0)

    response = client.get("/convert/?from_currency=BRL&to_currency=USD&amount=100")
    assert response.status_code == 200
    assert_almost_equal(response.json()["result"], 18.867924528301888)

    response = client.get("/convert/?from_currency=EUR&to_currency=BRL&amount=50")
    assert response.status_code == 200    

    response = client.get("/convert/?from_currency=BTC&to_currency=USD&amount=1")
    assert response.status_code == 200    

def test_invalid_currency():
    response = client.get("/convert/?from_currency=XYZ&to_currency=BRL&amount=100")
    assert response.status_code == 200
    assert response.json() == {"error": "Moeda não suportada"}

    response = client.get("/convert/?from_currency=USD&to_currency=XYZ&amount=100")
    assert response.status_code == 200
    assert response.json() == {"error": "Moeda não suportada"}

def test_negative_amount():
    response = client.get("/convert/?from_currency=USD&to_currency=BRL&amount=-100")
    assert response.status_code == 200
    assert response.json() == {"error": "O valor a ser convertido deve ser positivo"}

def test_missing_parameters():
    response = client.get("/convert/?to_currency=BRL&amount=100")
    assert response.status_code == 422

    response = client.get("/convert/?from_currency=USD&amount=100")
    assert response.status_code == 422

    response = client.get("/convert/?from_currency=USD&to_currency=BRL")
    assert response.status_code == 422
