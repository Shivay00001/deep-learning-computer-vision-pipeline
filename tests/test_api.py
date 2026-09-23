import pytest
import httpx
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_health():
    transport = httpx.ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
