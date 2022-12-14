from decimal import Decimal
from fractions import Fraction


class Rational:
    def __init__(self, args) -> None:
        """Instantiate with (numerator, numerator, denominator , denominator) """
        if len(args) > 4:
            raise ValueError('Variables can not be more than FOur (4)')
        self.first_num = args[0]
        self.second_num = args[1]
        self.first_denum = args[2]
        self.second_denum = args[3]

    def __str__(self):
        return f'({self.first_num} / {self.first_denum}), ({self.second_num} / {self.second_denum})'

    @staticmethod
    def get_common_factor(numer, denumer):
        common_factor = []
        for num in range(1, abs(denumer)):
            if (numer % num == 0) and (denumer % num == 0):
                common_factor.append(num)
        return max(common_factor)

    def add(self):
        result = (self.first_num / self.first_denum) + \
                 (self.second_num / self.second_denum)
        return {"reduced": str(Fraction(result).limit_denominator()), "actual result": str(Fraction(result))}

    def another_add(self):
        numerator = self.first_num + self.second_num
        denumerator = self.first_denum + self.second_denum
        result = f'{numerator // self.get_common_factor(numerator, denumerator)} / {denumerator // self.get_common_factor(numerator, denumerator)}'
        return result

    def subtract(self):
        result = (self.first_num / self.first_denum) - \
                 (self.second_num / self.second_denum)
        return {"reduced": str(Fraction(result).limit_denominator()), "actual result": str(Fraction(result))}

    @staticmethod
    def check_zero_error(value):
        if value <= 0:
            raise ValueError("Zero Variable on operation")

    def another_subract(self):
        try:
            numerator = self.first_num - self.second_num
            denumerator = self.first_denum - self.second_denum
            print(denumerator, numerator)
            print(f'{numerator // self.get_common_factor(numerator, denumerator)} / {denumerator // self.get_common_factor(numerator, denumerator)}')
            return 0 if numerator or denumerator == 0 else f'{numerator // self.get_common_factor(numerator, denumerator)} / {denumerator // self.get_common_factor(numerator, denumerator)}'
        except Exception as e:
            return e

    def multiply(self):
        result = (self.first_num / self.first_denum) * \
                 (self.second_num / self.second_denum)
        return {"reduced": str(Fraction(result).limit_denominator()), "actual result": str(Fraction(result))}

    def divide(self):
        result = (self.first_num / self.first_denum) / \
                 (self.second_num / self.second_denum)
        return {"reduced": str(Fraction(result).limit_denominator()), "actual result": str(Fraction(result))}


rational_number = Rational((1, -2, 2, 3))
print(rational_number)
print(rational_number.add())
print(rational_number.another_subract())
print(rational_number.get_common_factor(2, 100))
