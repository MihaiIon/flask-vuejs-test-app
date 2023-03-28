import pytest

def test_api(client):
    resp = client.get('/api/')
    assert resp.status_code == 200
