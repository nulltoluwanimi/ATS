from datetime import date
from class_list import class_list,month

class backend:
    def __init__(self, email):
        self.class_list = class_list
        self.month = month
        self.email = class_list[email]

    def increment_attendance(self,email):
            user_profile = {}
            for keys in class_list:
                if keys['first_name'].lower() == email.lower():
                    user_profile = keys
            user_profile['attendance'] = user_profile['attendance'] + 1
            return user_profile['attendance']

    def update_first_name(self, first_name: str, last_name: str, new_first_name: str, new_last_name: str):
            user_profile = {}
            for keys in class_list:
                if keys['first_name'].lower() == first_name.lower() and keys['last_name'].lower() == last_name.lower():
                    user_profile = keys
            user_profile['first_name'] = new_first_name
            user_profile['last_name'] = new_last_name
            return user_profile

    def all_full_name(self,list: list):
            new_list = []
            for list in class_list:
                new_list.append(list['first_name'].title())
            return new_list

    def add_new_profile(user_profile: dict):
            class_list.extend(user_profile)
            return class_list

    def number_of_users(class_list: list):
            return len(class_list)

    def remove_profile(first_name: str, last_name: str):
            for keys in class_list:
                if keys['first_name'].lower() == first_name.lower() and keys['last_name'].lower() == last_name.lower():
                    class_list.remove(keys)
                    return keys

    def get_dob(first_name: str, last_name: str):
            user_profile = {}
            for keys in class_list:
                if keys['first_name'].lower() == first_name.lower() and keys['last_name'].lower() == last_name.lower():
                    user_profile = keys
            return month[user_profile.date.month]

    def get_initial(class_list: list):
            new_list = []
            for people in class_list:
                print(people)
                append_data = "{a},{b}".format(
                    a=people['first_name'][0], b=people['last_name'][0])
                new_list.append(append_data)
            return new_list

    def BMI(first_name: str, last_name: str):
            for keys in class_list:
                if keys['first_name'].lower() == first_name.lower() and keys['last_name'].lower() == last_name.lower():
                    user_profile = keys
            bmi = user_profile['weight'] / user_profile['height'] ** 2
            return bmi

    def average_age_of_the_class(class_list: list):
            new_list = []
            for people in class_list:
                new_list.append(people['age'])
            sum_list = sum(new_list) / len(new_list)
            return sum_list

    def old_in_class(class_list: list):
            new_list = []
            for people in class_list:
                new_list.append(people['age'])
            sum_list = new_list.sort()
            return sum_list[len(class_list) - 1]

    def youngest_in_class(class_list: list):
            new_list = []
            for people in class_list:
                new_list.append(people['age'])
            sum_list = new_list.sort()
            return sum_list[0]

    def birth_year(first_name: str, last_name: str):
            for keys in class_list:
                if keys['first_name'].lower() == first_name.lower() and keys['last_name'].lower() == last_name.lower():
                    user_profile = keys
                today = date.today().year - user_profile['age']
                return today

    def describe(self, class_list: dict):
            return f"""
            The class has {self.number_of_users(class_list)} students, 
            the oldest students in the class is of {self.old_in_class(class_list)} age.
            and the  youngest student in the class is of {self.youngest_in_class(class_list)}
            and the average age is {self.average_age_of_the_class(class_list)}
            """

        # the class contain has different attributes

        print(increment_attendance('toluwanimi', 'ogunbiyi'))


