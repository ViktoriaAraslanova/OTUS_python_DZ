import pytest


# проверка является ли строка пустой
def test_string_is_empty():
    assert len('') == 0

# длина строки при контактенации 2-х строк = длине двух этих строк
@pytest.mark.parametrize("string_one", ['', 'test1', 'test2'])
@pytest.mark.parametrize("string_two", ['', 'test2', 'test1'])
def test_sting_concat(string_one, string_two):
    assert len(string_one + string_two) == len(string_one) + len(string_two)


# длина строки при повторении = длине строки * кол-во повторений
@pytest.mark.parametrize("string_one", ['', 'test1', 'test2'])
def test_string_repeat(string_one):
    assert len(string_one * 3) == len(string_one) * 3


# проверка метода replace
@pytest.mark.parametrize("string_one", ["Kyzkin", "Kiselev", "Shishkin"])
@pytest.mark.parametrize("add_str", ["Ivan", "Mihail", "Alexei"])
@pytest.mark.parametrize("replace", ["Petya", "Grisha", "Sergey"])
def test_string_replace(string_one, add_str, replace):
    print((string_one + add_str).replace(add_str, replace))
    print("Result", string_one + replace)
    assert string_one + replace == (string_one + add_str).replace(add_str, replace)


# проверка извлечения среза из строки
@pytest.mark.parametrize("string_one", ["Kyzkin", "Kiselev", "Shishkin"])
@pytest.mark.parametrize("sub_str", ["Ivan", "Mihail", "Alexei"])
def test_string_find(string_one, sub_str):
    string_one = string_one + sub_str
    number = (string_one + sub_str).find(sub_str)
    print("\n" + sub_str)
    print(string_one[number:len(string_one)])
    assert sub_str == string_one[number:len(string_one)]



