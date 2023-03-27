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
def author_stephen_data():
    return {'first_name': 'Bobby', 'last_name': 'Johns'}

@pytest.fixture
def author_stephen(client, author_stephen_data):
    response = client.post('/api/author/', data=author_stephen_data)
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

def test_note_creation__note_with_an_author(author_bobby, bobby_note):
    expected_author_full_name = f"{author_bobby['first_name']} {author_bobby['last_name']}"

    assert bobby_note['author_id'] == author_bobby['id']
    assert bobby_note['author_full_name'] == expected_author_full_name

def test_note_creation__error_when_attempting_to_create_a_note_without_a_title(client):
    data = { 'content': 'abc' }
    response = client.post('/api/note/', data=data)
    response_data = json.loads(response.data)

    error_message = response_data.get('errors', {}).get('title', '')
    assert 'A note must have a title' in error_message
    assert response.status_code == 400

def test_note_creation__error_when_attempting_to_create_a_note_without_a_content(client):
    data = { 'title': 'abc' }
    response = client.post('/api/note/', data=data)
    response_data = json.loads(response.data)

    error_message = response_data.get('errors', {}).get('content', '')
    assert 'A note must have a content' in error_message
    assert response.status_code == 400

""" Update """

def test_note_update(client, anonymous_note):
    expected_updated_title = "This title was updated"
    expected_updated_content = "This content was updated"

    data = { 'id': anonymous_note['id'], 'title': expected_updated_title, 'content': expected_updated_content }
    response = client.put('/api/note/', data=data)
    updated_note = json.loads(response.data)

    assert response.status_code == 200
    assert updated_note['id'] == anonymous_note['id']
    assert updated_note['title'] == expected_updated_title
    assert updated_note['content'] == expected_updated_content
    assert updated_note['author_full_name'] == anonymous_note['author_full_name']

def test_note_update__error_when_attempting_to_remove_the_title(client, anonymous_note):
    data = { 'id': anonymous_note['id'], 'title': '' }
    response = client.put('/api/note/', data=data)
    response_data = json.loads(response.data)

    error_message = response_data.get('errors', {}).get('title', '')
    assert 'A note must have a title' in error_message
    assert response.status_code == 400

def test_note_update__error_when_attempting_to_remove_the_content(client, anonymous_note):
    data = { 'id': anonymous_note['id'], 'content': '' }
    response = client.put('/api/note/', data=data)
    response_data = json.loads(response.data)

    error_message = response_data.get('errors', {}).get('content', '')
    assert 'A note must have a content' in error_message
    assert response.status_code == 400

def test_note_update__add_author_to_an_anonymous_note(client, author_bobby, anonymous_note):
    expected_author_full_name = f"{author_bobby['first_name']} {author_bobby['last_name']}"

    data = { 'id': anonymous_note['id'], 'author_id': author_bobby['id'] }
    response = client.put('/api/note/', data=data)
    updated_note = json.loads(response.data)

    assert updated_note['author_id'] == author_bobby['id']
    assert updated_note['author_full_name'] == expected_author_full_name

def test_note_update__remove_author(client, bobby_note):
    data = { 'id': bobby_note['id'], 'author_id': None }
    response = client.put('/api/note/', data=data)
    updated_note = json.loads(response.data)

    assert updated_note['author_id'] == None
    assert updated_note['author_full_name'] == 'Anonymous'

def test_note_update__change_author(client, bobby_note, author_stephen):
    expected_author_full_name = f"{author_stephen['first_name']} {author_stephen['last_name']}"

    data = { 'id': bobby_note['id'], 'author_id': author_stephen['id'] }
    response = client.put('/api/note/', data=data)
    updated_note = json.loads(response.data)

    assert updated_note['author_id'] == author_stephen['id']
    assert updated_note['author_full_name'] == expected_author_full_name
