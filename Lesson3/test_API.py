import pytest


TODOS_MAX = 200
USER_ID_MAX = 10


@pytest.mark.parametrize('todos_id', [1, TODOS_MAX])
def test_positive_getting_a_resource(session, base_url, todos_id):
    res = session.get(f'{base_url}/{todos_id}')
    assert res.status_code == 200
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
    payload = {
        "userId": user_id,
        "id": todos_id,
        "title": title,
        "completed": completed
    }
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
    payload = {
        "userId": user_id,
        "id": todos_id,
        "title": title,
        "completed": completed
    }
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


@pytest.mark.parametrize(
    'field, value',
    [('userId', USER_ID_MAX),
     ('id', TODOS_MAX),
     ('title', 'delectus aut autem'),
     ('completed', True)]
)
def test_positive_filtering_resources(session, base_url, field, value):
    str_val = str(value).lower() if isinstance(value, bool) else str(value)
    res = session.get(base_url, params={field: str_val})
    assert res.status_code == 200
    assert len(res.json()) != 0
    for i in res.json():
        assert i[field] == value


def test_positive_filtering_resources_all_params(session, base_url):
    user_id = 1
    id = 1
    title = "delectus aut autem"
    completed = False
    res = session.get(
        f'{base_url}?'
        f'userId={user_id}'
        f'&id={id}'
        f'&title={title}'
        f'&completed={str(completed).lower()}')
    assert res.status_code == 200
    assert len(res.json()) != 0
    for i in res.json():
        assert i['id'] == id
        assert i['userId'] == user_id
        assert i['title'] == title
        assert i['completed'] == completed


@pytest.mark.parametrize(
    'field, value',
    [('id', TODOS_MAX + 1),
     ('userId', USER_ID_MAX + 1),
     ('title', 'test'),
     ('completed', 'test')]
)
def test_negative_filtering_resources_id(session, base_url, field, value):
    res = session.get(base_url, params={field: value})
    assert res.status_code == 200
    assert not res.json()
