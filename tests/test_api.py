from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_create_and_get_task():
    payload = {"title": "Estudar DevOps", "description": "Terminar o roteiro", "completed": False}
    create_response = client.post("/tasks", json=payload)
    assert create_response.status_code == 201
    task_id = create_response.json()["id"]

    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 200
    assert get_response.json()["title"] == "Estudar DevOps"


def test_get_task_not_found():
    response = client.get("/tasks/9999")
    assert response.status_code == 404


def test_update_task():
    payload = {"title": "Nova tarefa", "description": "desc", "completed": False}
    created = client.post("/tasks", json=payload).json()

    update_payload = {"title": "Nova tarefa", "description": "desc atualizada", "completed": True}
    response = client.put(f"/tasks/{created['id']}", json=update_payload)
    assert response.status_code == 200
    assert response.json()["completed"] is True


def test_delete_task():
    payload = {"title": "Tarefa temporária", "description": "desc", "completed": False}
    created = client.post("/tasks", json=payload).json()

    response = client.delete(f"/tasks/{created['id']}")
    assert response.status_code == 200