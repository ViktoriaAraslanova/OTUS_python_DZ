import pytest
from Lesson4.test_Figure import *


# Figure
@pytest.mark.parametrize("is_figure1, is_figure2", [(Square(1), Rectangle(1, 2)), (Triangle(1, 2, 3), Circle(5))])
def test_positive_add_area(is_figure1, is_figure2):
    assert is_figure1.add_area(is_figure2) == is_figure1.area + is_figure2.area


@pytest.mark.parametrize("is_figure1, not_figure", [(Square(1), "test"), (Triangle(1, 2, 3), 1)])
def test_negative_add_area(is_figure1, not_figure):
    with pytest.raises(AssertionError):
        is_figure1.add_area(not_figure)


# Square
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


@pytest.mark.parametrize("input_side, expected_area", [(1, 1), (2, 4), (3, 9), (4, 16)])
def test_get_area_square(input_side, expected_area):
    assert Square(input_side).area == expected_area


@pytest.mark.parametrize("input_side, expected_perimeter", [(1, 4), (2, 8), (3, 12), (4, 16)])
def test_get_perimeter_square(input_side, expected_perimeter):
    assert Square(input_side).perimeter == expected_perimeter


# Rectangle
@pytest.mark.parametrize("input_side1, input_side2", [(1, 4), (2, 8), (3, 12), (4, 16)])
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


@pytest.mark.parametrize("input_side1, input_side2, expected_area", [(1, 2, 2), (2, 4, 8), (3, 9, 27), (4, 16, 64)])
def test_get_area_rectangle(input_side1, input_side2, expected_area):
    assert Rectangle(input_side1, input_side2).area == expected_area


@pytest.mark.parametrize("input_side1, input_side2, expected_perimeter", [(1, 1, 4), (2, 4, 12), (3, 9, 24), (4, 16, 40)])
def test_get_perimeter_rectangle(input_side1, input_side2, expected_perimeter):
    assert Rectangle(input_side1, input_side2).perimeter == expected_perimeter


# Triangle
@pytest.mark.parametrize("input_side1, input_side2, input_side3", [(1, 4, 1), (2, 8, 1)])
def test_init_positive_triangle(input_side1, input_side2, input_side3):
    triangle = Triangle(input_side1, input_side2, input_side3)
    assert triangle.name == Triangle.name
    assert triangle.angles == Triangle.angles
    assert triangle.side1 == input_side1
    assert triangle.side2 == input_side2
    assert triangle.side3 == input_side3


@pytest.mark.parametrize("input_side1, input_side2, input_side3", [(-1, 4, 1), (2, -8, 1), (2, 8, -1)])
def test_init_negative_triangle_side(input_side1, input_side2, input_side3):
    with pytest.raises(AssertionError):
        Triangle(input_side1, input_side2, input_side3)


@pytest.mark.parametrize("input_side1, input_side2, input_side3, expected_area", [(3, 4, 5, 6)])
def test_get_area_triangle(input_side1, input_side2, input_side3, expected_area):
    assert Triangle(input_side1, input_side2, input_side3).area == expected_area


@pytest.mark.parametrize("input_side1, input_side2, input_side3, expected_perimeter", [(1, 1, 4, 6), (2, 4, 12, 18)])
def test_get_perimeter_triangle(input_side1, input_side2, input_side3, expected_perimeter):
    assert Triangle(input_side1, input_side2, input_side3).perimeter == expected_perimeter


# Circle
@pytest.mark.parametrize("input_radius", range(1,3))
def test_init_positive_circle(input_radius):
    circle = Circle(input_radius)
    assert circle.name == Circle.name
    assert circle.angles == Circle.angles
    assert circle.radius == input_radius


@pytest.mark.parametrize("negative_input_radius", [-1, -5])
def test_init_negative_circle_radius(negative_input_radius):
    with pytest.raises(AssertionError):
        Circle(negative_input_radius)


@pytest.mark.parametrize("input_radius, expected_area", [(5, 78.54)])
def test_get_area_circle(input_radius, expected_area):
    assert Circle(input_radius).area == expected_area


@pytest.mark.parametrize("input_radius, expected_perimeter", [(5, 31.42)])
def test_get_perimeter_circle(input_radius, expected_perimeter):
    assert Circle(input_radius).perimeter == expected_perimeter