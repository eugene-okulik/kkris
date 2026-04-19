import requests


def all_objects():
    response = requests.get('http://objapi.course.qa-practice.com/object').json()
    assert len(response) == 1, 'Not all objects returned'


all_objects()


def one_object():
    object_id = 1
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{object_id}').json()
    assert response['id'] == object_id, 'Wrong object id returned'


one_object()


def post_object():
    body = {
        "name": "My object",
        "data": {
            "color": "red",
            "size": "medium"
        }
    }
    header = {'Content-Type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=header)
    assert response.status_code == 201, 'Wrong status code returned'
    assert response.json()['name'] == 'My object', 'Wrong body name returned'


post_object()


def put_object():
    body = {
        "name": "My object-UPD",
        "data": {
            "color": "red-UPD",
            "size": "medium-UPD"
        }
    }
    header = {'Content-Type': 'application/json'}
    response = requests.put('http://objapi.course.qa-practice.com/object/1', json=body, headers=header)
    assert response.json()['name'] == 'My object-UPD', 'Wrong body name returned'


put_object()


def patch_object():
    body = {
        "name": "My object-UPDUPD",
    }
    header = {'Content-Type': 'application/json'}
    response = requests.patch('http://objapi.course.qa-practice.com/object/1', json=body, headers=header)
    assert response.json()['name'] == 'My object-UPDUPD', 'Wrong body name returned'


patch_object()


def delete_object():
    response = requests.delete('http://objapi.course.qa-practice.com/object/1')
    assert response.status_code == 200, 'Wrong status code returned'


delete_object()
