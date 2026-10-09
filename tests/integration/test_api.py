import httpx
import pytest

from app.main import app


@pytest.fixture
async def client():
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as c:
        yield c


async def test_health_returns_200(client):
    response = await client.get("/health")
    assert response.status_code == 200


async def test_chat_valid_question_returns_200(client):
    response = await client.post("/api/v1/chat", json={"question": "¿Qué es FastAPI?"})
    assert response.status_code == 200
    body = response.json()
    assert body["provider"] == "bootstrap-local"
    assert body["answer"]


async def test_chat_too_short_question_returns_422(client):
    response = await client.post("/api/v1/chat", json={"question": "ab"})
    assert response.status_code == 422


async def test_info_returns_200_and_llm_disabled(client):
    response = await client.get("/api/v1/info")
    assert response.status_code == 200
    assert response.json()["llm_enabled"] is False
