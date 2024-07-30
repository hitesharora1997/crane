from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_update_state_endpoint():
    response = client.post(
        "/update_state",
        json={
            "swing": 45,
            "lift": 100,
            "elbow": 30,
            "wrist": 60,
            "gripper": 20})
    assert response.status_code == 200
    assert response.json() == {"message": "State updated"}


def test_solve_ik_endpoint():
    response = client.post("/solve_ik", json=[100, 100, 50])
    assert response.status_code == 200
    assert response.json() == {"message": "IK solved"}


def test_update_origin_endpoint():
    response = client.post(
        "/update_origin",
        json={
            "x": 10,
            "y": 20,
            "z": 30,
            "rotation": 45})
    assert response.status_code == 200
    assert response.json() == {"message": "Origin updated"}
