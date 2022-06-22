import csv
import sys

headers = ['first_name', 'last_name', 'username', 'password', 'dob', 'phone_number', 'gender', 'address']


def validate_input(value):
    if value:
        return value
    else:
        print('empty input, field is required!')
        return input('Input value again: ')


def validate_phone(value):
    if value.isnumeric():
        return value
    else:
        print('phone number can only contain numbers: ')
        return input('Input value again: ')


def compulsory_input(i):
    value = str(input(f'Enter {i}: '))
    if value:
        return value
    else:
        print('compulsory input')
        return compulsory_input(i)


def check_password(password, c_password):
    if password != c_password:
        print('Password does not match!')
        return
    if len(str(password)) < 8:
        print('At least 8 characters required')
        return False
    elif password == c_password:
        return True


def check_username(name):
    if len(str(name)) < 6:
        return 'Username can not be less than 6'
    with open('new_file.csv', 'r') as file:
        handler = csv.DictReader(file)
        for key in handler:
            if key['username'] == name.lower():
                print(f'{name} exist, try another one')
                return
        return name.lower()


def validate_gender(value):
    if value.lower() not in ['male', 'female']:
        print('Invalid, gender type')
    else:
        return value


def save_to_csv(data):
    with open('new_file.csv', 'a', newline='') as new_data:
        handler = csv.DictWriter(new_data, fieldnames=headers)
        handler.writerow(data)

def sign_up():
    username = str(input('Enter your username: '))
    first_name = validate_input(str(input('Enter your first name: ')))
    last_name = validate_input(str(input('Enter your last name: ')))
    password = validate_input(str(input('Enter password:')))
    confirm_password = validate_input(str(input('Confirm password: ')))
    dob = validate_input(str(input('provide your date of birth: ')))
    phone_number = validate_phone(validate_input(str(input('Enter your phone number: '))))
    gender = validate_gender(str(input('male(M) / female(F): ')))
    address = validate_input(str(input('provide your address: ')))

    if check_password(password, confirm_password) and check_username(username):
        user_data = {
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'password': password,
            'dob': dob,
            'phone_number': phone_number,
            'gender': gender,
            'address': address
        }
        save_to_csv(user_data)
        return True


def sign_in():
    username = str(input('Enter your username'))
    password = validate_input(str(input('Enter password')))

    with open('new_file.csv', 'r') as user_file:
        handler = csv.DictReader(user_file)
        for rows in handler:
            if rows['username'] == username.lower() and rows['password'] == password.lower():
                print(f"""
                        success:true
                        message:{username} logged in successfully
                        """)
                return username
        print(f'Invalid username or password!')
        return False


def edit_profile(username):
    user = {}
    with open('new_file.csv', 'r') as file:
        handler = csv.DictReader(file)
        for key in handler:
            if key['username'] == username.lower():
                user = key
                break
    print(f'User info\n {user}')
    phone_number = compulsory_input('phone-number')
    address = str(input('Enter new address: '))
    if not address:
        address = user['address']
    dob = str(input('Enter D.O.B: '))
    if not dob:
        dob = user['dob']
    gender = compulsory_input('gender')

    if gender and phone_number:
        with open('new_file.csv', 'r') as update_file:
            handler = csv.DictReader(update_file)
            # w_handler = csv.DictWriter(update_file, fieldnames=headers)
            data = []
            for i in handler:
                if i['username'].lower() == username:
                    i['phone_number'] = phone_number
                    i['address'] = address
                    i['dob'] = dob
                    i['gender'] = gender
                data.append(i)
        with open('new_file.csv', 'w') as save_data:
            handler = csv.DictWriter(save_data, fieldnames=headers)
            handler.writeheader()
            for i in data:
                handler.writerow(i)
    print('profile updated is successful')
    input_ = input('would you like take another action (y/n): ').lower()
    if 'y' == input_:
        return prompt(username)
    else:
        return


def change_password(username):
    user = {}
    with open('new_file.csv', 'r') as file:
        handler = csv.DictReader(file)
        for key in handler:
            if key['username'] == username.lower():
                user = key
                break
    print(f'User info\n {user}')
    old_password = compulsory_input('old_password')
    password = compulsory_input('phone-number')

    if old_password == user['password']:
        print('Old password does not match')
        sys.exit()

    if password:
        with open('new_file.csv', 'r') as update_file:
            handler = csv.DictReader(update_file)
            # w_handler = csv.DictWriter(update_file, fieldnames=headers)
            data = []
            for i in handler:
                if i['username'].lower() == username:
                    i['phone_number'] = password
                data.append(i)
        with open('new_file.csv', 'w') as save_data:
            handler = csv.DictWriter(save_data, fieldnames=headers)
            handler.writeheader()
            for i in data:
                handler.writerow(i)
    print('profile updated is successful')
    input_ = input('would you like take another action (y/n): ').lower()
    if 'y' == input_:
        return prompt(username)
    else:
        return


def logout(username):
    print(f'you have successfully logged out {username}')
    return


def prompt(username):
    action = input("""what will you like to do
    1. Edit profile
    2. Change password
    3. Logout
    """)

    if action not in ['1', '2', '3']:
        print('wrong input!')
    else:
        list_ = {
            '1': edit_profile,
            '2': change_password,
            '3': logout
        }
        return list_[action](username)


if __name__ == '__main__':
    # print('Welcome to lettr.com, sign up to continue')
    if sign_up():
        print('Sign up successfully, provide your details to sign in!')
        user = sign_in()
        prompt(user)
