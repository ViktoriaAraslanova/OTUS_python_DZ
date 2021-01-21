import math


class Figure:
    name = "Figure"
    angles = 0
    __area = 0
    __perimeter = 0

    def __init__(self, name, angles):
        self.name = name
        self.angles = angles

    @property
    def area(self):
        return self.__area

    @property
    def perimeter(self):
        return self.__perimeter

    def add_area(self, other_figure):
        if isinstance(other_figure, Figure):
            return self.area + other_figure.area
        raise AssertionError('wrong condition')


class Square(Figure):
    name = "Square"
    angles = 4

    def __init__(self, side):
        super().__init__(Square.name, Square.angles)
        if side < 0:
            raise AssertionError('side must be positive number or zero')
        self.side = side

    @property
    def area(self):
        return self.side ** 2

    @property
    def perimeter(self):
        return self.side*4


class Rectangle(Figure):
    name = "Rectangle"
    angles = 4

    def __init__(self, side1, side2):
        super().__init__(Rectangle.name, Rectangle.angles)
        if side1 < 0 or side2 < 0:
            raise AssertionError('side must be positive number or zero')
        self.side1 = side1
        self.side2 = side2

    @property
    def area(self):
        return self.side1 * self.side2

    @property
    def perimeter(self):
        return (self.side1 + self.side2)*2


class Triangle(Figure):
    name = "Triangle"
    angles = 3

    def __init__(self, side1, side2, side3):
        super().__init__(Triangle.name, Triangle.angles)
        if side1 < 0 or side2 < 0 or side3 < 0:
            raise AssertionError('side must be positive number or zero')
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    @property
    def area(self):
        pp = self.perimeter / 2
        return math.sqrt(pp * ((pp - self.side1) * (pp - self.side2) * (pp - self.side3)))

    @property
    def perimeter(self):
        return self.side1 + self.side2 + self.side3


class Circle(Figure):
    name = "Circle"
    angles = 0

    def __init__(self, radius):
        super().__init__(Circle.name, Circle.angles)
        if radius < 0:
            raise AssertionError('side must be positive number or zero')
        self.radius = radius

    @property
    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    @property
    def perimeter(self):
        return round(self.radius*2*math.pi, 2)



