import pytest
import requests
from jsonschema import validate
import json


TODOS_MAX = 200
USER_ID_MAX = 10


def assert_valid_schema(data, schema_file):
    with open(schema_file) as f:
        schema = json.load(f)
    return validate(instance=data, schema=schema)

@pytest.fixture()
def base_url():
    return "https://jsonplaceholder.typicode.com/todos"


@pytest.fixture()
def session():
    return requests.Session()


@pytest.mark.parametrize('todos_id', [1, TODOS_MAX])
def test_positive_getting_a_resource(session, base_url, todos_id):
    res = session.get(f'{base_url}/{todos_id}')
    assert res.status_code == 200
    assert_valid_schema(res.json(), 'schemas/getting_a_resource_schema.json')
    assert res.json()['id'] == todos_id


@pytest.mark.parametrize('todos_id', [0, TODOS_MAX + 1])
def test_negative_getting_a_resource(session, base_url, todos_id):
    res = session.get(f'{base_url}/{todos_id}')
    assert res.status_code == 404
    assert not res.json()


def test_positive_listing_all_resources(session, base_url):
    res = session.get(f'{base_url}')
    json = res.json()
    assert res.status_code == 200
    assert_valid_schema(res.json(), 'schemas/listing_all_resources_schema.json')
    assert len(json) == TODOS_MAX


def test_positive_creating_a_resource(session, base_url):
    user_id = 1
    title = "test title"
    completed = True
    payload = {"userId": user_id, "title": title, "completed": completed}
    res = session.post(url=base_url, json=payload)
    assert res.status_code == 201
    json = res.json()
    assert json['id'] == TODOS_MAX + 1
    assert json['userId'] == user_id
    assert json['title'] == title
    assert json['completed'] == completed


@pytest.mark.parametrize('todos_id', [1, TODOS_MAX])
def test_positive_updating_a_resource_with_put(session, base_url, todos_id):
    user_id = 1
    title = "test title"
    completed = True
    payload = {"userId": user_id, "id": todos_id, "title": title, "completed": completed}
    res = session.put(url=f'{base_url}/{todos_id}', json=payload)
    assert res.status_code == 200
    json = res.json()
    assert json['id'] == todos_id
    assert json['userId'] == user_id
    assert json['title'] == title
    assert json['completed'] == completed


@pytest.mark.parametrize('todos_id', [0, TODOS_MAX + 1])
def test_negative_updating_a_resource(session, base_url, todos_id):
    user_id = 1
    title = "test title"
    completed = True
    payload = {"userId": user_id, "id": todos_id, "title": title, "completed": completed}
    res = session.put(url=f'{base_url}/{todos_id}', json=payload)
    assert res.status_code == 500


@pytest.mark.parametrize('todos_id', [1, TODOS_MAX])
def test_positive_updating_a_resource_with_patch(session, base_url, todos_id):
    url_with_todos_id = (f'{base_url}/{todos_id}')
    res_json = session.get(url_with_todos_id).json()
    title = res_json['title'] + '_updated'
    res = session.patch(url=url_with_todos_id, json={'title': title})
    assert res.status_code == 200
    json = res.json()
    assert json['id'] == todos_id
    assert json['userId'] == res_json['userId']
    assert json['title'] == title
    assert json['completed'] == res_json['completed']


@pytest.mark.parametrize('todos_id', [1, TODOS_MAX])
def test_positive_deleting_a_resource(session, base_url, todos_id):
    res = session.delete(f'{base_url}/{todos_id}')
    assert res.status_code == 200
    assert not res.json()


@pytest.mark.parametrize('user_id', [1, USER_ID_MAX])
def test_positive_filtering_resources_userId(session, base_url, user_id):
    res = session.get(f'{base_url}?userId={user_id}')
    assert res.status_code == 200
    for i in res.json():
        assert i['userId'] == user_id


@pytest.mark.parametrize('id', [1, TODOS_MAX])
def test_positive_filtering_resources_id(session, base_url, id):
    res = session.get(f'{base_url}?id={id}')
    assert res.status_code == 200
    for i in res.json():
        assert i['id'] == id


@pytest.mark.parametrize('title', ["delectus aut autem", "quis ut nam facilis et officia qui"])
def test_positive_filtering_resources_title(session, base_url, title):
    res = session.get(f'{base_url}?title={title}')
    assert res.status_code == 200
    for i in res.json():
        assert i['title'] == title


@pytest.mark.parametrize('completed', [True, False])
def test_positive_filtering_resources_completed(session, base_url, completed):
    res = session.get(f'{base_url}?completed={completed}')
    assert res.status_code == 200
    for i in res.json():
        assert i['completed'] == completed


def test_positive_filtering_resources_all_params(session, base_url):
    title = "delectus aut autem"
    res = session.get(f'{base_url}?userId={1}&id={1}&title={title}&completed={True}')
    assert res.status_code == 200
    for i in res.json():
        assert i['id'] == 1
        assert i['userId'] == 1
        assert i['title'] == title
        assert i['completed'] == True


@pytest.mark.parametrize('id', [0, TODOS_MAX + 1])
def test_negative_filtering_resources_id(session, base_url, id):
    res = session.get(f'{base_url}?id={id}')
    assert res.status_code == 200
    assert not res.json()


@pytest.mark.parametrize('user_id', [0, USER_ID_MAX + 1])
def test_negative_filtering_resources_userId(session, base_url, user_id):
    res = session.get(f'{base_url}?userId={user_id}')
    assert res.status_code == 200
    assert not res.json()


def test_negative_filtering_resources_title(session, base_url):
    res = session.get(f'{base_url}?title={"test"}')
    assert res.status_code == 200
    assert not res.json()


def test_negative_filtering_resources_completed(session, base_url):
    res = session.get(f'{base_url}?completed={"test"}')
    assert res.status_code == 200
    assert not res.json()


