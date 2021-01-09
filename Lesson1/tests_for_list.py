import pytest


# тест на проверку длины пустого списка
def test_list_is_empty():
    assert len([]) == 0


# тест на проверку добавления элемента в конец списка
@pytest.mark.parametrize("list_input", [[], [i for i in range(10)], [i for i in range(5, 10)]])
@pytest.mark.parametrize("el_add", [1, "str", True])
def test_list_append(list_input, el_add):
    list_input.append(el_add)
    print("\n list_input_with_el_add: " + str(list_input))
    assert list_input[len(list_input)-1] == el_add


# тест на проверку вставки в i-ый элемент значения x
@pytest.mark.parametrize("list_input", [[], [i for i in range(10)], [i for i in range(5, 10)]])
@pytest.mark.parametrize("el_insert", [1, "str", True])
def test_list_insert(list_input, el_insert):
    i = 0
    list_input.insert(i, el_insert)
    print("\n list_input_with_el_insert: " + str(list_input))
    assert list_input[i] == el_insert


# тест на проверку копирования списка
@pytest.mark.parametrize("list_input", [[], [i for i in range(10)], [i for i in range(5, 10)]])
def test_list_copy(list_input):
    print("\n list_input: " + str(list_input))
    assert list_input == list_input.copy()


# тест на проверку очищения списка
@pytest.mark.parametrize("list_input", [[], [i for i in range(10)], [i for i in range(5, 10)]])
def test_list_clear(list_input):
    print("\n list_input: " + str(list_input))
    assert list_input.clear() is None




