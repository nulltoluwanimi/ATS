from datetime import date

class_list = [{"first_name": "Awwal", "last_name": "Adeleke", "date": {"day": 20, "month": 4}, "attendance": 11, "height": 190, "weight": 70, "age": 23},
              {"first_name": "Abraham", "last_name": "Adekunle", "date": {
                  "day": 25, "month": 1}, "attendance": 11, "height": 183, "weight": 65, "age": 23},
              {"first_name": "Abdulwali", "last_name": "Tajudeen", "date": {
                  "day": 16, "month": 9}, "attendance": 11, "height": 193, "weight": 75, "age": 20},
              {"first_name": "Adebusola", "last_name": "Adeyeye", "date": {
                  "day": 10, "month": 7}, "attendance": 10, "height": 178, "weight": 55, "age": 21},
              {"first_name": "Yusuff", "last_name": "Oyedele", "date": {
                  "day": 14, "month": 3}, "attendance": 9, "height": 180, "weight": 63, "age": 26},
              {"first_name": "Basheer", "last_name": "Balogun", "date": {
                  "day": 16, "month": 11}, "attendance": 10, "height": 180, "weight": 60, "age": 25},
              {"first_name": "Abdullahi", "last_name": "Salaam", "date": {
                  "day": 2, "month": 7}, "attendance": 11, "height": 172, "weight": 68, "age": 25},
              {"first_name": "Faith", "last_name": "Adeosun", "date": {
                  "day": 5, "month": 3}, "attendance": 7, "height": 168, "weight": 61, "age": 23},
              {"first_name": "Ahmad", "last_name": "Sharafudeen", "date": {
                  "day": 12, "month": 12}, "attendance": 11, "height": 178, "weight": 61, "age": 24},
              {"first_name": "Lukman", "last_name": "Abisoye", "date": {
                  "day": 15, "month": 11}, "attendance": 10, "height": 175, "weight": 62, "age": 23},
              {"first_name": "Toluwanimi", "last_name": "Ogunbiyi", "date": {"day": 9, "month": 3}, "attendance": 9, "height": 188, "weight": 81, "age": 24}]

month = ["January", "February", "March", "April", "May", "June", "July",
         "August", "September", "October", "November", "December"]


def increment_attendance(first_name: str, last_name: str):
    user_profile = {}
    for keys in class_list:
        if keys['first_name'].lower() == first_name.lower() and keys['last_name'].lower() == last_name.lower:
            user_profile = keys
    user_profile['attendance'] = user_profile['attendance'] + 1
    return user_profile['attendance']
    # if((type() == float)):
    #     return 'Error: value must be a number'
    # else:
    #     return (value + 1)


def update_first_name(first_name: str, last_name: str):
    user_profile = {}
    for keys in class_list:
        if keys['first_name'].lower() == first_name.lower() and keys['last_name'].lower() == last_name.lower:
            user_profile = keys
    user_profile['first_name'] = first_name
    user_profile['last_name'] = last_name
    return user_profile


def all_full_name(list: list):
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
        if keys['first_name'].lower() == first_name.lower() and keys['last_name'].lower() == last_name.lower:
            class_list.remove(keys)
            return keys


def get_dob(first_name: str, last_name: str):
    user_profile = {}
    for keys in class_list:
        if keys['first_name'].lower() == first_name.lower() and keys['last_name'].lower() == last_name.lower:
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
        if keys['first_name'].lower() == first_name.lower() and keys['last_name'].lower() == last_name.lower:
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
    return sum_list[len(class_list)-1]


def youngest_in_class(class_list: list):
    new_list = []
    for people in class_list:
        new_list.append(people['age'])
    sum_list = new_list.sort()
    return sum_list[0]


def birth_year(first_name: str, last_name: str):
    for keys in class_list:
        if keys['first_name'].lower() == first_name.lower() and keys['last_name'].lower() == last_name.lower:
            user_profile = keys
        today = date.today().year - user_profile['age']
        return today


# the class contain has different attributes


print(increment_attendance(class_list))
