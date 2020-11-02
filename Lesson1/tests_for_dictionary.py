import pytest


# тест на проверку обновления словаря
@pytest.mark.parametrize("dict_input", [dict(), {a: a ** 2 for a in range(10)}])
def test_update_dict(dict_input: dict):
    dict_input.update({'new_key': 1})
    assert dict_input['new_key'] == 1


# тест на проверку получение элемента словаря по ключу ф-ей get
@pytest.mark.parametrize("dict_input", [dict(), {a: a ** 2 for a in range(10)}])
def test_dict_get(dict_input):
    dict_input.update({'new_key': 1})
    assert dict_input.get('new_key') == dict_input['new_key']


# тест на провреку удаления ключа и возвращение значения
@pytest.mark.parametrize("dict_input", [dict(), {a: a ** 2 for a in range(10)}])
def test_dict_pop(dict_input):
    dict_input.update({'new_key': 1})
    value = dict_input.pop('new_key')
    assert value == 1 and 'new_key' not in dict_input


# тест на провреку является ли словарь пустым
@pytest.mark.parametrize("dict_input", [dict(), {a: a ** 2 for a in range(10)}])
def test_dict_is_empty(dict_input):
    assert dict_input.clear() is None

# тест на проверку метода, создающего копию словаря
@pytest.mark.parametrize("dict_input", [dict(), {a: a ** 2 for a in range(10)}])
def test_dict_copy(dict_input):
    assert dict_input.copy() == dict_input
