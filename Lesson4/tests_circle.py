import pytest
from Lesson4.Figure import Circle


@pytest.mark.parametrize("input_radius", range(1, 3))
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
