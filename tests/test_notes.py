import pytest
import json

""" Fixtures """

@pytest.fixture
def author_bobby_data():
    return {'first_name': 'Bobby', 'last_name': 'Johns'}

@pytest.fixture
def author_bobby(client, author_bobby_data):
    response = client.post('/api/author/', data=author_bobby_data)
    return json.loads(response.data)

@pytest.fixture
def note_data():
    return {'title': 'Note Title', 'content': 'Note Content'}

@pytest.fixture
def bobby_note_data(note_data, author_bobby):
    return {'title': note_data['title'], 'content': note_data['title'], 'author_id': author_bobby['id']}

@pytest.fixture
def anonymous_note(client, note_data):
    response = client.post('/api/note/', data=note_data)
    return json.loads(response.data)

@pytest.fixture
def bobby_note(client, bobby_note_data):
    response = client.post('/api/note/', data=bobby_note_data)
    return json.loads(response.data)

""" Creation """

def test_note_creation(note_data, anonymous_note):
    expected_title = note_data['title']
    expected_content = note_data['content']

    assert isinstance(anonymous_note['id'], int)
    assert anonymous_note['title'] == expected_title
    assert anonymous_note['content'] == expected_content

def test_note_creation__anonymous_author_when_creating_a_note_without_an_author(anonymous_note):
    assert anonymous_note['author_full_name'] == 'Anonymous'

def test_note_creation__author_full_name_returned_when_note_has_an_author(author_bobby_data, bobby_note):
    author_first_name = author_bobby_data['first_name']
    author_last_name = author_bobby_data['last_name']
    expected_author_full_name = f"{author_first_name} {author_last_name}"

    assert bobby_note['author_full_name'] == expected_author_full_name

def test_note_creation__error_when_attempting_to_create_a_note_without_a_title(client):
    data = { 'content': 'abc' }
    response = client.post('/api/note/', data=data)

    data = json.loads(response.data)
    error_message = data.get('errors', {}).get('title', '')
    assert 'A note must have a title' in error_message
    assert response.status_code == 400

def test_note_creation__error_when_attempting_to_create_a_note_without_a_content(client):
    data = { 'title': 'abc' }
    response = client.post('/api/note/', data=data)

    data = json.loads(response.data)
    error_message = data.get('errors', {}).get('content', '')
    assert 'A note must have a content' in error_message
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
