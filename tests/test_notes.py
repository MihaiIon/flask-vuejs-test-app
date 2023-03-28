import pytest
import json

""" Fixtures """

from .shared_fixtures import *

@pytest.fixture
def note_data():
    return {'title': 'Note Title', 'content': 'Note Content'}

@pytest.fixture
def bobby_note_data(note_data, author_bobby):
    return {'title': f"{author_bobby['first_name']} {note_data['title']}", 'content': note_data['title'], 'author_id': author_bobby['id']}

@pytest.fixture
def stephen_note_data(note_data, author_stephen):
    return {'title': f"{author_stephen['first_name']} {note_data['title']}", 'content': note_data['title'], 'author_id': author_stephen['id']}

@pytest.fixture
def anonymous_note(client, note_data):
    response = client.post('/api/note/', data=note_data)
    return json.loads(response.data)

@pytest.fixture
def bobby_note(client, bobby_note_data):
    response = client.post('/api/note/', data=bobby_note_data)
    return json.loads(response.data)

@pytest.fixture
def stephen_note(client, stephen_note_data):
    response = client.post('/api/note/', data=stephen_note_data)
    return json.loads(response.data)

""" Read """

def test_note_read__list(client, anonymous_note, bobby_note, stephen_note):
    response = client.get('/api/note/')
    notes = json.loads(response.data)

    note_ids = sorted([note['id'] for note in notes])
    expected_note_ids = sorted([anonymous_note['id'], bobby_note['id'], stephen_note['id']])

    assert response.status_code == 200
    assert note_ids == expected_note_ids

def test_note_read(client, bobby_note):
    response = client.get(f"/api/note/{bobby_note['id']}")
    note = json.loads(response.data)

    assert response.status_code == 200
    assert note['id'] == bobby_note['id']
    assert note['title'] == bobby_note['title']
    assert note['content'] == bobby_note['content']
    assert note['author_id'] == bobby_note['author_id']
    assert note['author_full_name'] == bobby_note['author_full_name']

def test_note_read__error_when_request_a_note_that_does_not_exist(client, bobby_note):
    none_existing_note_id = 1234567890

    response = client.get(f"/api/note/{none_existing_note_id}")
    data = json.loads(response.data)

    assert response.status_code == 404
    assert f"Note {none_existing_note_id} not found" in data['message'] 

""" Creation """

def test_note_creation(note_data, anonymous_note):
    expected_title = note_data['title']
    expected_content = note_data['content']

    assert isinstance(anonymous_note['id'], int)
    assert anonymous_note['title'] == expected_title
    assert anonymous_note['content'] == expected_content

def test_note_creation__error_when_attempting_to_create_a_note_without_a_title(client):
    response = client.post('/api/note/', data={'content': 'abc'})
    response_data = json.loads(response.data)

    error_message = response_data.get('errors', {}).get('title', '')
    assert 'A note must have a title' in error_message
    assert response.status_code == 400

def test_note_creation__error_when_attempting_to_create_a_note_without_a_content(client):
    response = client.post('/api/note/', data={'title': 'abc'})
    response_data = json.loads(response.data)

    error_message = response_data.get('errors', {}).get('content', '')
    assert 'A note must have a content' in error_message
    assert response.status_code == 400

# def test_note_creation__error_when_attempting_to_associate_the_note_with_an_author_that_does_not_exist(client):
#     assert False

def test_note_creation__anonymous_author_when_creating_a_note_without_an_author(anonymous_note):
    assert anonymous_note['author_full_name'] == 'Anonymous'

def test_note_creation__note_with_an_author(author_bobby, bobby_note):
    expected_author_full_name = f"{author_bobby['first_name']} {author_bobby['last_name']}"

    assert bobby_note['author_id'] == author_bobby['id']
    assert bobby_note['author_full_name'] == expected_author_full_name

""" Update """

def test_note_update(client, anonymous_note):
    expected_updated_title = "This title was updated"
    expected_updated_content = "This content was updated"

    route = f"/api/note/{anonymous_note['id']}"
    data = {'title': expected_updated_title, 'content': expected_updated_content}

    response = client.put(route, data=data)
    updated_note = json.loads(response.data)

    assert response.status_code == 200
    assert updated_note['id'] == anonymous_note['id']
    assert updated_note['title'] == expected_updated_title
    assert updated_note['content'] == expected_updated_content
    assert updated_note['author_full_name'] == anonymous_note['author_full_name']

def test_note_update__error_when_attempting_to_remove_the_title(client, anonymous_note):
    route = f"/api/note/{anonymous_note['id']}"
    data = {'title': ''}

    response = client.put(route, data=data)
    response_data = json.loads(response.data)

    error_message = response_data.get('errors', {}).get('title', '')
    assert 'A note must have a title' in error_message
    assert response.status_code == 400

def test_note_update__error_when_attempting_to_remove_the_content(client, anonymous_note):
    route = f"/api/note/{anonymous_note['id']}"
    data = {'content': ''}

    response = client.put(route, data=data)
    response_data = json.loads(response.data)

    error_message = response_data.get('errors', {}).get('content', '')
    assert 'A note must have a content' in error_message
    assert response.status_code == 400

# def test_note_update__error_when_attempting_to_associate_the_note_with_an_author_that_does_not_exist(client):
#     assert False

def test_note_update__add_author_to_an_anonymous_note(client, author_bobby, anonymous_note):
    expected_author_full_name = f"{author_bobby['first_name']} {author_bobby['last_name']}"

    route = f"/api/note/{anonymous_note['id']}"
    data = {'author_id': author_bobby['id']}

    response = client.put(route, data=data)
    updated_note = json.loads(response.data)

    assert updated_note['author_id'] == author_bobby['id']
    assert updated_note['author_full_name'] == expected_author_full_name

def test_note_update__remove_author(client, bobby_note):
    route = f"/api/note/{bobby_note['id']}"
    data = {'author_id': None}

    response = client.put(route, data=data)
    updated_note = json.loads(response.data)

    assert updated_note['author_id'] == None
    assert updated_note['author_full_name'] == 'Anonymous'

def test_note_update__change_author(client, bobby_note, author_stephen):
    expected_author_full_name = f"{author_stephen['first_name']} {author_stephen['last_name']}"

    route = f"/api/note/{bobby_note['id']}"
    data = {'author_id': author_stephen['id']}

    response = client.put(route, data=data)
    updated_note = json.loads(response.data)

    assert updated_note['author_id'] == author_stephen['id']
    assert updated_note['author_full_name'] == expected_author_full_name

""" Delete """

def test_note_delete(client, anonymous_note):
    response = client.delete(f"/api/note/{anonymous_note['id']}")
    assert response.status_code == 200

    response = client.get(f"/api/note/{anonymous_note['id']}")
    assert response.status_code == 404
