import pytest
import json

""" Fixtures """

from .shared_fixtures import *

""" Read """

def test_author_read__list(client, author_bobby, author_stephen):
    response = client.get('/api/author/')
    authors = json.loads(response.data)

    author_ids = sorted([author['id'] for author in authors])
    expected_authors_ids = sorted([author_bobby['id'], author_stephen['id']])

    assert response.status_code == 200
    assert author_ids == expected_authors_ids

""" Creation """

def test_author_creation(client):
    expected_first_name = 'Bobby'
    expected_last_name = 'Johns'
    expected_full_name = f"{expected_first_name} {expected_last_name}"

    data = { 'first_name': expected_first_name, 'last_name': expected_last_name }
    response = client.post('/api/author/', data=data)
    created_author = json.loads(response.data)

    assert response.status_code == 200
    assert isinstance(created_author['id'], int)
    assert created_author['first_name'] == expected_first_name
    assert created_author['last_name'] == expected_last_name
    assert created_author['full_name'] == expected_full_name

def test_author_creation__error_when_attempting_to_create_a_author_without_a_first_name(client):
    data = { 'last_name': 'LastName' }
    response = client.post('/api/author/', data=data)

    data = json.loads(response.data)
    error_message = data.get('errors', {}).get('first_name', '')
    assert 'An author must have first name' in error_message
    assert response.status_code == 400

def test_author_creation__error_when_attempting_to_create_a_author_without_a_last_name(client):
    data = { 'first_name': 'FirstName' }
    response = client.post('/api/author/', data=data)

    data = json.loads(response.data)
    error_message = data.get('errors', {}).get('last_name', '')
    assert 'An author must have last name' in error_message
    assert response.status_code == 400
