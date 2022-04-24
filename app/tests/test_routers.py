from ..main import app
from ..database.schemas.flights import Flight

from fastapi.testclient import TestClient
from typing import List

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_get_single_flight():
    response = client.get("/flights")
    assert response.status_code == 200
