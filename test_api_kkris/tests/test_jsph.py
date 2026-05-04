def test_get_all_objects(create_get_endpoint):
    create_get_endpoint.get_all_objects()
    create_get_endpoint.check_object_len()


def test_get_one_object(create_get_endpoint):
    object_id = 1
    create_get_endpoint.get_object_by_id(object_id)
    create_get_endpoint.check_object_id_is_correct(object_id)


def test_post_object(create_post_endpoint):
    payload = {
        "name": 'My object',
        "data": {
            "color": "red",
            "size": "medium"
        }
    }
    headers = {'Content-Type': 'application/json'}
    create_post_endpoint.create_new_object(payload=payload, headers=headers)
    create_post_endpoint.check_response_title(payload["name"])
    create_post_endpoint.check_response_code()


def test_put_object(create_put_patch_endpoint, created_object):
    payload = {
        "name": "My object-UPD",
        "data": {
            "color": "red-UPD",
            "size": "medium-UPD"
        }
    }
    headers = {'Content-Type': 'application/json'}
    create_put_patch_endpoint.put_existing_object(created_object, payload=payload, headers=headers)
    create_put_patch_endpoint.check_response_title(payload["name"])
    create_put_patch_endpoint.check_response_code()


def test_patch_object(create_put_patch_endpoint, created_object):
    payload = {
        "name": "My object-UPDUPD",
    }
    headers = {'Content-Type': 'application/json'}
    create_put_patch_endpoint.patch_existing_object(created_object, payload=payload, headers=headers)
    create_put_patch_endpoint.check_response_title(payload["name"])
    create_put_patch_endpoint.check_response_code()


def test_delete_object(create_delete_endpoint, created_object):
    create_delete_endpoint.delete_existing_object(created_object)
    create_delete_endpoint.check_response_code()
