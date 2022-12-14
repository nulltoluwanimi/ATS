class Computation:
    @classmethod
    def factorial(cls, number):
        if number == 1 or number == 0:
            return 1
        return number * cls.factorial(number - 1)

    @staticmethod
    def sum(numbers):
        """sum of a given list"""
        validate_number = isinstance(numbers, list)
        for number in numbers:
            if type(number) != int: raise ValueError('Invalid data type')
        if not validate_number: raise ValueError('Invalid data type')
        result = 0
        for number in numbers:
            number += number
            result = number
        return result

    @staticmethod
    def is_prime(number):
        """check if a number is prime"""
        validate_number = isinstance(number, int)
        if not validate_number: raise ValueError('Invalid data type')
        if number <= 1: return False
        for i in range(2, number):
            if number % i == 0:
                return False

        return True

    @staticmethod
    def get_mult_table(number):
        """returns multiplication table of a given number"""
        result = []
        div = list(range(1, 11))
        for num in range(1, 11):
            result.append(number * num)
        return f"""
            mult table of {number}
            (divisor, mult):{list(zip(div, result))}
        """

    @staticmethod
    def get_all_mult():
        """returns all multiplication table"""
        for i in range(1, 11):
            for j in range(1, 11):
                print(f'{i * j}', end=' ')
            print('\n')


print(Computation.get_all_mult())
