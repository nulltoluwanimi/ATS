from typing import Tuple


class Rectangle:

    def __init__(self, upper_coordinates: Tuple=(), lower_coordinates: Tuple=()) -> None:
        self.upper_coordinates = upper_coordinates
        self.lower_coordinates = lower_coordinates

    @property
    def upper_coordinates(self):
        return self.upper_coordinates

    @upper_coordinates.setter
    def upper_coordinates(self, value):
        print(value)
        if value[0] or value[1] > 20:
            raise ValueError(f"coordinates can not be greater than 20")
        self.upper_coordinates = value

    @property
    def lower_coordinates(self):
        return self.lower_coordinates

    @lower_coordinates.setter
    def lower_coordinates(self, value):
        if value[0] or value[1] > 20:
            raise ValueError(f"coordinates can not be greater than 20")
        self.lower_coordinates = value

    def __str__(self) -> str:
        return f'{self.upper_coordinates}, {self.lower_coordinates}'

    def get_sides(self):
        side1 = self.upper_coordinates[1] - self.lower_coordinates[1]
        side2 = self.lower_coordinates[0] - self.upper_coordinates[0]
        return side1, side2

    def get_length(self):
        length = max(self.get_sides())
        return length

    def get_width(self):
        width = min(self.get_sides())
        return width

    def get_perimeter(self):
        return 2 * (self.get_length() + self.get_width())

    def get_area(self):
        return self.get_length() * self.get_width()

    def is_square(self):
        return True if min(self.get_sides()) == max(self.get_sides()) else False

    def is_rectangle(self):
        return True if min(self.get_sides()) != max(self.get_sides()) else False


rec1 = Rectangle((5, 6), (7, 1))
# rec2 = Rectangle((2, 3), (3, 2))
#
# print(rec1.get_perimeter())
#
# print(rec2.get_area())
#
# print(rec2.is_square())
