
import pytest
from Lesson4.Figure import Triangle


@pytest.mark.parametrize(
    "input_side1, "
    "input_side2, "
    "input_side3",
    [(1, 4, 1), (2, 8, 1)]
)
def test_init_positive_triangle(input_side1, input_side2, input_side3):
    triangle = Triangle(input_side1, input_side2, input_side3)
    assert triangle.name == Triangle.name
    assert triangle.angles == Triangle.angles
    assert triangle.side1 == input_side1
    assert triangle.side2 == input_side2
    assert triangle.side3 == input_side3


@pytest.mark.parametrize(
    "input_side1, "
    "input_side2, "
    "input_side3",
    [(-1, 4, 1), (2, -8, 1), (2, 8, -1)]
)
def test_init_negative_triangle_side(input_side1, input_side2, input_side3):
    with pytest.raises(AssertionError):
        Triangle(input_side1, input_side2, input_side3)


@pytest.mark.parametrize(
    "input_side1, "
    "input_side2, "
    "input_side3, "
    "expected_area",
    [(3, 4, 5, 6)]
)
def test_get_area_triangle(
        input_side1,
        input_side2,
        input_side3,
        expected_area):
    assert Triangle(
        input_side1,
        input_side2,
        input_side3
    ).area == expected_area


@pytest.mark.parametrize(
    "input_side1, "
    "input_side2, "
    "input_side3, "
    "expected_perimeter",
    [(1, 1, 4, 6), (2, 4, 12, 18)]
)
def test_get_perimeter_triangle(
        input_side1,
        input_side2,
        input_side3,
        expected_perimeter):
    assert Triangle(
        input_side1,
        input_side2,
        input_side3
    ).perimeter == expected_perimeter
