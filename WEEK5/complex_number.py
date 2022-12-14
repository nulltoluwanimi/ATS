from math import sqrt
from decimal import Decimal
from typing import Tuple

TYPES = (0, 0, 0, 0)


class Complex:

    # i = sqrt(-1)

    def __init__(self, kwargs: Tuple = TYPES) -> None:
        """Instantiate with (real, real, imaginary , imaginary) """
        if len(kwargs) > 4:
            raise ValueError('Variables can not be more than FOur (4)')
        self.first_real = Decimal(kwargs[0])
        self.second_real = Decimal(kwargs[1])
        self.first_imaginary = Decimal(kwargs[2])
        self.second_imaginary = Decimal(kwargs[3])

    def __str__(self):
        return f'({self.first_real} , {self.first_imaginary}i), ({self.second_real} , {self.second_imaginary}i)'

    def add(self):
        return f'{self.first_real + self.second_real} + {self.first_imaginary + self.second_imaginary}i'

    def subtract(self):
        return f'{self.first_real - self.second_real} + {self.first_imaginary - self.second_imaginary}i'


complex_number = Complex((6, 3, -4, 7))
print(complex_number)
