import pytest
from httpx import AsyncClient, ASGITransport

from app.main import app

TESTUSER_LOGIN_DATA = {
    'username': 'test@test.com',
    'password': 'test_password'
}

AUTHENTICATED_RESPONSE = {
    "salary": "777.00",
    "next_promotion": "2027-05-14"
}
UNAUTHENTICATED_RESPONSE = {'detail': 'Unauthorized'}


@pytest.fixture
def anyio_backend():
    return 'asyncio'


@pytest.fixture
async def client():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://127.0.0.1:8000/"
    ) as client:
        yield client


@pytest.mark.anyio
async def test_authenticated_request(client):
    login_response = await client.post(
        "/auth/jwt/login",
        data=TESTUSER_LOGIN_DATA
    )
    assert login_response.status_code == 200
    response_data = login_response.json()
    assert 'access_token' in response_data
    token = response_data['access_token']
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = await client.get("/api/v1/salary", headers=headers)
    assert response.status_code == 200
    assert response.json() == AUTHENTICATED_RESPONSE


@pytest.mark.anyio
async def test_unauthenticated_request(client):
    response = await client.get("/api/v1/salary")
    assert response.status_code == 401
    assert response.json() == UNAUTHENTICATED_RESPONSE
