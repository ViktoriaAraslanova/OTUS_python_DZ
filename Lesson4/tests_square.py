import pytest
from Lesson4.Figure import Square


@pytest.mark.parametrize("input_side", range(0, 5))
def test_init_positive_square(input_side):
    square = Square(input_side)
    assert square.name == Square.name
    assert square.angles == Square.angles
    assert square.side == input_side


@pytest.mark.parametrize("negative_input_side", [-1, -5])
def test_init_negative_square(negative_input_side):
    with pytest.raises(AssertionError):
        Square(negative_input_side)


@pytest.mark.parametrize(
    "input_side, "
    "expected_area",
    [(1, 1), (2, 4), (3, 9), (4, 16)]
)
def test_get_area_square(input_side, expected_area):
    assert Square(input_side).area == expected_area


@pytest.mark.parametrize(
    "input_side, "
    "expected_perimeter",
    [(1, 4), (2, 8), (3, 12), (4, 16)]
)
def test_get_perimeter_square(input_side, expected_perimeter):
    assert Square(input_side).perimeter == expected_perimeter
