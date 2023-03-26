import pytest
import json

""" Creation """

def test_note_creation(client):
    expected_title = 'This is a test title for the note'
    expected_content = 'This is a test content for the note'

    data = { 'title': expected_title, 'content': expected_content }
    response = client.post('/api/note/', data=data)

    created_note = json.loads(response.data)
    assert response.status_code == 200
    assert isinstance(created_note['id'], int)
    assert created_note['title'] == expected_title
    assert created_note['content'] == expected_content

def test_note_creation__anonymous_author_when_creating_a_note_without_an_author(client):
    expected_author_full_name = 'Anonymous'

    data = { 'title': 'abc', 'content': 'xyz' }
    response = client.post('/api/note/', data=data)

    created_note = json.loads(response.data)
    assert created_note['author_full_name'] == expected_author_full_name

def test_note_creation__error_when_attempting_to_create_a_note_without_a_title(client):
    data = { 'content': 'xyz' }
    response = client.post('/api/note/', data=data)

    data = json.loads(response.data)
    error_message = data.get('message', '')
    assert error_message == 'A note must have a title'
    assert response.status_code == 400

def test_note_creation__error_when_attempting_to_create_a_note_without_a_content(client):
    data = { 'title': 'abc' }
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
