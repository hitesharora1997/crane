import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


@pytest.mark.asyncio
async def test_websocket():
    with client.websocket_connect("/ws") as websocket:
        data = websocket.receive_json()
        assert "state" in data
        assert "origin" in data
