import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def api_client():
    with sync_playwright() as p:
        request_context = p.request.new_context()
        yield request_context
        request_context.dispose()

class UserAPI:
    def __init__(self):
        self.url = "http://localhost:5001/api/create_user"
        self.headers = {
            "Content-Type": "application/json",
            "X-API-KEY": "my-secret-key-123"
        }

def test_create_user(api_client):
    user_api = UserAPI()
    payload = {
        "user_id": "5209",
        "user_name": "Saad Malik",
        "current_balance": 398000,
        "city": "123"
    }

    response = api_client.post(user_api.url, data=payload, headers=user_api.headers)
    print("Response:", response.json())
    assert response.status == 201
