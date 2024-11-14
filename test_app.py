import pytest
from app import app 

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_add_user(client):
    res = client.post('/users', query_string={'user':'Ram'})
    assert res.status == 200
    res = res.get_json()
    assert res['msg'] == "User Inserted Successfully!"