# tests/test_routes.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_analyze_route_status():
    response = client.get("/analyze/testsub")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_analyze_route_structure():
    response = client.get("/analyze/testsub")
    if response.json():
        comment = response.json()[0]
        assert "id" in comment
        assert "text" in comment
        assert "polarity_score" in comment
        assert "classification" in comment
