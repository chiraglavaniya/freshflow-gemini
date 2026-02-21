from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"


def test_dashboard_endpoint_shape():
    response = client.get("/api/v1/dashboard?limit=60")
    assert response.status_code == 200
    payload = response.json()

    assert "average_price" in payload
    assert "forecast_price" in payload
    assert "agents" in payload
    assert len(payload["series"]) == 60
