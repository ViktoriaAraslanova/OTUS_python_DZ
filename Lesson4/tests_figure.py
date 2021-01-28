import pytest
from Lesson4.Figure import Square, Rectangle, Triangle, Circle


@pytest.mark.parametrize(
    "is_figure1, "
    "is_figure2",
    [(Square(1), Rectangle(1, 2)), (Triangle(1, 2, 3), Circle(5))]
)
def test_positive_add_area(is_figure1, is_figure2):
    assert is_figure1.add_area(is_figure2) == is_figure1.area + is_figure2.area


@pytest.mark.parametrize(
    "is_figure1, "
    "not_figure",
    [(Square(1), "test"), (Triangle(1, 2, 3), 1)]
)
def test_negative_add_area(is_figure1, not_figure):
    with pytest.raises(AssertionError):
        is_figure1.add_area(not_figure)
