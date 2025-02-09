import json
import pytest
from src.core.api.app import app
from httpx import ASGITransport, AsyncClient

pytestmark = pytest.mark.test_login


@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.post(
            "/api/v1/register", json={"phone_number": "1234567890"}
        )
    assert response.status_code == 200
