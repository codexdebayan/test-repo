import pytest
from app import app 

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_fetch_user(client):
    res = client.get('/users')
    assert res.status_code == 200
    res_json = res.get_json()
    expected_users = ["Gyan", "Prince", "Shyam", "John"]
    assert res_json == expected_users