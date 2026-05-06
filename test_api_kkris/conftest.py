import pytest
from endpoints.create_object import CreateObject
from endpoints.update_object import UpdateObject
from endpoints.delete_object import DeleteObject
from endpoints.get_object import GetObject


@pytest.fixture()
def create_get_endpoint():
    return GetObject()


@pytest.fixture()
def create_post_endpoint():
    return CreateObject()


@pytest.fixture()
def create_put_patch_endpoint():
    return UpdateObject()


@pytest.fixture()
def create_delete_endpoint():
    return DeleteObject()


@pytest.fixture()
def created_object(create_post_endpoint, create_delete_endpoint):
    payload = {
        "name": "temp object",
        "data": {
            "color": "red",
            "size": "medium"
        }
    }
    headers = {'Content-Type': 'application/json'}

    response = create_post_endpoint.create_new_object(payload=payload, headers=headers)
    object_id = response.json()['id']
    yield object_id
    create_delete_endpoint.delete_existing_object(object_id)
