import random
import string


class password_gen:
    def __init__(self):
        self.alpha_case = list(string.ascii_uppercase)
        self.lower_case = list(string.ascii_lowercase)
        self.numerics = list(string.digits)
        self.special = list(string.punctuation)

    def generate_password(self):
        group = self.alpha_case + self.lower_case + self.numerics + self.special
        return ''.join(random.sample(group, 20))

    # @staticmethod
    def username_suggestion(self):
        first_name = str(input('provide your username: '))
        last_name = str(input('provide your lastname: '))
        suggest = []
        for i in range(5):
            slice_number = int(random.randint(0, len(first_name)))
            slice_last = int(random.randint(0, len(last_name)))
            suggestions = first_name[0:slice_number] + last_name[0:slice_last] + str(random.randint(99, 999))
            suggest.append(suggestions)

        return suggest


if __name__ == '__main__':
    print()
    pass_gen = password_gen()
    print(pass_gen.username_suggestion())
