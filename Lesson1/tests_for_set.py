import pytest


# тест на проверку добавления элемента во множенство
@pytest.mark.parametrize("set_input", [set(), {i for i in range(10)}, {'one', 'two', 'three'}])
@pytest.mark.parametrize("el_add", [1, "str", False])
def test_set_add(set_input, el_add):
    set_input.add(el_add)
    print("\n set_input_with_el_add: " + str(set_input))
    assert el_add in set_input


# тест на проверку удаления элемента из множества (эл-т во множестве есть)
@pytest.mark.parametrize("set_input", [set(), {i for i in range(10)}, {'one', 'two', 'three'}])
@pytest.mark.parametrize("elem", [1, "str", False])
def test_set_remove(set_input, elem):
    set_input.add(elem)
    set_input.remove(elem)
    print("\n set_input_with_del_elem: " + str(set_input))
    assert elem not in set_input


# тест на проверку очищения множества
@pytest.mark.parametrize("set_input", [set(), {i for i in range(10)}, {'one', 'two', 'three'}])
def test_set_clear(set_input):
    set_input.clear()
    print("\n set_input_clear: " + str(set_input))
    assert len(set_input) == 0


# тест на проверку копирования множества
@pytest.mark.parametrize("test_input", [set(), {i for i in range(10)}, {'one', 'two', 'three'}])
def test_set_copy(test_input):
    copy_test_input = test_input.copy()
    assert copy_test_input == test_input


# множество всех элементов 1-го множества, не принадлежащие ни одному из 2-го множества
@pytest.mark.parametrize("test_input", [set(), {i for i in range(10)}, {'one', 'two', 'three'}])
@pytest.mark.parametrize("test_input_two", [{i for i in range(20)}])
def test_set_difference(test_input, test_input_two):
    test_out = {i for i in test_input if i not in test_input_two}
    assert test_out == test_input.difference(test_input_two)


# тест на проверку объединения 2-х множеств
@pytest.mark.parametrize("test_input", [set(), {i for i in range(10)}, {'one', 'two', 'three'}])
@pytest.mark.parametrize("test_input_two", [{i for i in range(20)}])
def test_set_union(test_input, test_input_two):
    test_out = test_input.copy()
    for i in test_input_two:
        test_out.add(i)
    assert test_out == test_input.union(test_input_two)


# тест на пересечение элементов 2-х множеств
@pytest.mark.parametrize("test_input", [set(), {i for i in range(10)}, {'one', 'two', 'three'}])
@pytest.mark.parametrize("test_input_two", [{i for i in range(20)}])
def test_set_intersection(test_input, test_input_two):
    test_out = {i for i in test_input for j in test_input_two if i == j}
    print("\n test_input: " + str(test_input))
    print("\n test_input_two " + str(test_input_two))
    print("\n test_out " + str(test_out))
    assert test_out == test_input.intersection(test_input_two)

