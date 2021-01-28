import pytest
from Lesson4.Figure import Rectangle


@pytest.mark.parametrize(
    "input_side1, "
    "input_side2",
    [(1, 4), (2, 8), (3, 12), (4, 16)]
)
def test_init_positive_rectangle(input_side1, input_side2):
    rect = Rectangle(input_side1, input_side2)
    assert rect.name == Rectangle.name
    assert rect.angles == Rectangle.angles
    assert rect.side1 == input_side1
    assert rect.side2 == input_side2


@pytest.mark.parametrize("input_side1, input_side2", [(-1, 4), (2, -8)])
def test_init_negative_rectangle_side(input_side1, input_side2):
    with pytest.raises(AssertionError):
        Rectangle(input_side1, input_side2)


@pytest.mark.parametrize(
    "input_side1, "
    "input_side2, "
    "expected_area",
    [(1, 2, 2), (2, 4, 8), (3, 9, 27), (4, 16, 64)]
)
def test_get_area_rectangle(input_side1, input_side2, expected_area):
    assert Rectangle(input_side1, input_side2).area == expected_area


@pytest.mark.parametrize(
    "input_side1, "
    "input_side2, "
    "expected_perimeter",
    [(1, 1, 4), (2, 4, 12), (3, 9, 24), (4, 16, 40)]
)
def test_get_perimeter_rectangle(input_side1, input_side2, expected_perimeter):
    assert Rectangle(input_side1, input_side2).perimeter == expected_perimeter
