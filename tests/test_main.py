from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_execute_task():
    response = client.post("/execute", json={
        "task_type": "execute_code",
        "code": "print('Hello, World!')",
        "resources": {
            "cpu": "2",
            "gpu": "0",
            "ram": "512MB",
            "storage": "1GB"
        }
    })
    assert response.status_code == 200
    assert "Hello, World!" in response.json()["result"]

def test_execute_task_with_loop():
    response = client.post("/execute", json={
        "task_type": "execute_code",
        "code": "for i in range(5): print(f'Count {i}')",
        "resources": {
            "cpu": "1",
            "gpu": "0",
            "ram": "256MB",
            "storage": "500MB"
        }
    })
    assert response.status_code == 200
    assert "Count 0" in response.json()["result"]
    assert "Count 4" in response.json()["result"]
