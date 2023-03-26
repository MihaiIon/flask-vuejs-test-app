import pytest
import json

from app.utils import Database
from flask_sqlalchemy import SQLAlchemy

# db = Database.instance

def test_note_creation_response_code(client):
    data = { 'title': 'abc', 'content': 'xyz' }
    response = client.post('/api/note/', data=data)

    assert response.status_code == 200

def test_note_creation_error_when_the_title_is_missing(client):
    data = { 'content': 'abc' }
    response = client.post('/api/note/', data=data)

    data = json.loads(response.data)
    error_message = data.get('message', '')
    assert error_message == 'A note must have a title'
    assert response.status_code == 400

def test_note_creation_error_when_the_content_is_missing(client):
    data = { 'title': 'xyz' }
    response = client.post('/api/note/', data=data)

    data = json.loads(response.data)
    error_message = data.get('message', '')
    assert error_message == 'A note must have a content'
    assert response.status_code == 400


def test_note_creation_without_an_author(client):
    expected_title = 'This is a test title for the note'
    expected_content = 'This is a test content for the note'
    expected_author_full_name = 'Anonymous'

    data = { 'title': expected_title, 'content': expected_content }
    response = client.post('/api/note/', data=data)

    created_note = json.loads(response.data)
    assert created_note['title'] == expected_title
    assert created_note['content'] == expected_content
    assert created_note['author_full_name'] == expected_author_full_name
