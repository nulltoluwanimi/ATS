import numbers
import csv


def validate_input(value):
    if value:
        return value
    else:
        print('empty input, field is required!')
        return


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
        print('Username can not be less than 6')
        return

    with open('new_file.csv', 'r') as file:
        handler = csv.DictReader(file)
        for key in handler:
            if key['username'] == name.lower():
                print(f'{name} exist, try another one')
                break
        return name.lower()


def save_to_csv(data):
    with open('new_file.csv', 'a', newline='') as new_data:
        headers = ['first_name', 'last_name', 'username', 'password']
        handler = csv.DictWriter(new_data, fieldnames=headers)
        # handler.writeheader()
        handler.writerow(data)


def get_username(name):
    with open('new_file.csv', 'r') as file:
        handler = csv.DictReader(file)
        print(handler)
        for key in handler:
            if key['Username'] == name.lower():
                return name
            break


def take_input(value):
    if '1' == value:
        username = str(input('Enter your username'))
        first_name = validate_input(str(input('Enter your first name')))
        last_name = validate_input(str(input('Enter your last name')))
        password = validate_input(str(input('Enter password')))
        confirm_password = validate_input(str(input('Confirm password')))
        print(check_password(password, confirm_password) and check_username(username))
        if check_password(password, confirm_password) and check_username(username):
            user_data = {
                'first_name': first_name,
                'last_name': last_name,
                'username': username,
                'password': password,
            }
            save_to_csv(user_data)
            print('Sign up successfully')


    elif '2' == value:

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
                    return
            print(f'{username} not found')
            return


if __name__ == '__main__':
    action = str(input('Input 1 for signup or 2 for signin: '))
    if action not in ['1', '2']:
        print('Invalid input')
    else:
        take_input(action)
