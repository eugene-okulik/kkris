import requests
import pytest


@pytest.fixture()
def new_object_id():
    body = {
        "name": "My object",
        "data": {
            "color": "red",
            "size": "medium"
        }
    }
    header = {'Content-Type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=header)
    object_id = response.json()['id']
    yield object_id
    requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')


@pytest.fixture(scope='session', autouse=True)
def auxfunc_session():
    print('\nStart testing')
    yield
    print('\nTesting completed')


@pytest.fixture(autouse=True)
def auxfunc_tests():
    print('\nbefore test')
    yield
    print('\nafter test')


def test_all_objects():
    response = requests.get('http://objapi.course.qa-practice.com/object').json()
    assert len(response) == 1, 'Not all objects returned'


def test_one_object(new_object_id):
    object_id = 1
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{object_id}').json()
    assert response['id'] == object_id, 'Wrong object id returned'


@pytest.mark.critical
@pytest.mark.parametrize('name', [1, 'My object', '$&^$'])
def test_post_object(name):
    body = {
        "name": name,
        "data": {
            "color": "red",
            "size": "medium"
        }
    }
    header = {'Content-Type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=header)
    assert response.status_code == 200, 'Wrong status code returned'
    assert response.json()['name'] == 'My object', 'Wrong body name returned'


def test_put_object(new_object_id):
    body = {
        "name": "My object-UPD",
        "data": {
            "color": "red-UPD",
            "size": "medium-UPD"
        }
    }
    header = {'Content-Type': 'application/json'}
    response = requests.put(f'http://objapi.course.qa-practice.com/object/{new_object_id}', json=body, headers=header)
    assert response.json()['name'] == 'My object-UPD', 'Wrong body name returned'


@pytest.mark.medium
def test_patch_object(new_object_id):
    body = {
        "name": "My object-UPDUPD",
    }
    header = {'Content-Type': 'application/json'}
    response = requests.patch(f'http://objapi.course.qa-practice.com/object/{new_object_id}', json=body, headers=header)
    assert response.json()['name'] == 'My object-UPDUPD', 'Wrong body name returned'


def test_delete_object(new_object_id):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{new_object_id}')
    assert response.status_code == 200, 'Wrong status code returned'
