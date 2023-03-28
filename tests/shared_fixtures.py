import pytest
import json

@pytest.fixture
def author_bobby_data():
    return {'first_name': 'Bobby', 'last_name': 'Johns'}

@pytest.fixture
def author_bobby(client, author_bobby_data):
    response = client.post('/api/author/', data=author_bobby_data)
    return json.loads(response.data)

@pytest.fixture
def author_stephen_data():
    return {'first_name': 'Bobby', 'last_name': 'Johns'}

@pytest.fixture
def author_stephen(client, author_stephen_data):
    response = client.post('/api/author/', data=author_stephen_data)
    return json.loads(response.data)