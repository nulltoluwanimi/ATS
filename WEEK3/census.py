import re
import os
import csv

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def validate_input(value):
    if value:
        return value
    else:
        print('empty input, field is required!')
        return


def validate_gender(value):
    if value.lower() not in ['male', 'female']:
        print('Invalid, gender type')
    else:
        return value


def validate_email(value):
    if re.fullmatch(regex, value):
        return value
    else:
        print('email type is wrong')
        return


def validate_marital(value):
    if value.lower() not in ['married', 'single']:
        print('Invalid marital type')
    else:
        return value


def create_dict(*args):
    dict_data = {
        'first_name': args[0],
        'last_name': args[1],
        'middle_name': args[2],
        'age': args[3],
        'occupation': args[4],
        'dob': args[5],
        'gender': args[6],
        'marital_status': args[7],
        'email': args[8]

    }
    print(dict_data)
    return dict_data


def get_data():
    first_name = validate_input(str(input('Input your first name: ')))
    last_name = validate_input(str(input('Input your last name: ')))
    middle_name = validate_input(str(input('Input your middle name: ')))
    age = validate_input(str(input('please provide your age: ')))
    occupation = validate_input(str(input('provide your occupation: ')))
    dob = validate_input(str(input('provide date of birth: ')))
    gender = validate_gender(str(input('male / female: ')))
    marital_status = validate_marital(validate_input(str(input('marital status: '))))
    email = validate_email(validate_input(str(input('provide a valid email:'))))
    user_data = create_dict(first_name, last_name, middle_name, age, occupation, dob, gender, marital_status, email)
    print(user_data)
    user_list:list = [].append(user_data)
    print(user_list)
    rr = str(input('do you wish to input data again (y for yes)/ (n for no): '))
    if 'y' == rr:
        get_data()
    elif 'n' == rr:
        print()
        save_data(user_list)
    else:
        print('wrong input')


def actions():
    act = str(input('''what will you like to do: '
                    1 - check data
                    2 - save data
                    '''''))
    if act not in ['1', '2']:
        print('wrong input , try again')
        actions()
    else:
        action_dict = {
            '1': provide_data,
            '2': get_data
        }
        return action_dict.get(act, None)()


def save_data(user_list: list):
    print(user_list)
    with open('hours-worked-per-week-in-other-jobs-2018-census-csv.csv', 'w') as user_file:
        handler = csv.DictWriter(user_file,
                                 fieldnames=['first_name', 'last_name', 'middle_name', 'age', 'occupation', 'dob',
                                             'gender', 'marital_status', 'email'])
        handler.writeheader()
        for list_data in user_list:
            handler.writerow(list_data)

    return 'Operation successfully'


def provide_data():
    type_data = input("""what will you like to check with
    1. email
    2. names
    """)
    if '2' == type_data:
        first = input('provide first name')
        last = input('provide last name')
        middle = input('provide middle name')
        return read_data(first, last, middle, email=None)
    if '1' == type_data:
        email = validate_email(input('provide a valid email'))
        return read_data(email)


def read_data(*args, email=None):
    with open('hours-worked-per-week-in-other-jobs-2018-census-csv.csv', 'w') as user_file:
        handler = csv.DictReader(user_file)
    if args:
        for rows in handler:
            if rows['first_name'] == args[0] or rows['last_name'] == args[1] or rows['middle_name'] == args[2]:
                return rows
    elif email:
        for rows in handler:
            if rows['email'] == email:
                return rows


# print(first_name)

if __name__ == '__main__':
    actions()
