import csv
import sys


class auth:
    def __init__(self):
        self.headers = ['first_name', 'last_name', 'username', 'password', 'dob', 'phone_number', 'gender', 'address']

    @staticmethod
    def __call__(self, *args, **kwargs):
        return self

    def __getitem__(self, item):
        return self.headers[item]
    def validate_input(value):
        if value:
            return value
        else:
            print('empty input, field is required!')
            return input('Input value again: ')

    @staticmethod
    def validate_phone(value):
        if value.isnumeric():
            return value
        else:
            print('phone number can only contain numbers: ')
            return input('Input value again: ')

    def compulsory_input(self, i):
        value = str(input(f'Enter {i}: '))
        if value:
            return value
        else:
            print('compulsory input')
            return self.compulsory_input(i)

    @staticmethod
    def check_password(password, c_password):
        if password != c_password:
            print('Password does not match!')
            return
        if len(str(password)) < 8:
            print('At least 8 characters required')
            return False
        elif password == c_password:
            return True

    @staticmethod
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

    @staticmethod
    def validate_gender(value):
        if value.lower() not in ['male', 'female']:
            print('Invalid, gender type')
        else:
            return value

    def save_to_csv(self, data):
        with open('new_file.csv', 'a', newline='') as new_data:
            handler = csv.DictWriter(new_data, fieldnames=self.headers)
            handler.writerow(data)

    def sign_up(self):
        username = str(input('Enter your username: '))
        first_name = self.validate_input(str(input('Enter your first name: ')))
        last_name = self.validate_input(str(input('Enter your last name: ')))
        password = self.validate_input(str(input('Enter password:')))
        confirm_password = self.validate_input(str(input('Confirm password: ')))
        dob = self.validate_input(str(input('provide your date of birth: ')))
        phone_number = self.validate_phone(self.validate_input(str(input('Enter your phone number: '))))
        gender = self.validate_gender(str(input('male(M) / female(F): ')))
        address = self.validate_input(str(input('provide your address: ')))

        if self.check_password(password, confirm_password) and self.check_username(username):
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
            self.save_to_csv(user_data)
            return True

    def sign_in(self):
        username = str(input('Enter your username'))
        password = self.validate_input(str(input('Enter password')))

        with open('new_file.csv', 'r') as user_file:
            handler = csv.DictReader(user_file)
            for rows in handler:
                if rows['username'] == username.lower() and rows['password'] == password.lower():
                    print(f"""
                                success:true
                                message:{username} logged in successfully
                                """)
                    self.prompt(username)
            print(f'Invalid username or password!')
            return False

    def edit_profile(self, username):
        user = {}
        with open('new_file.csv', 'r') as file:
            handler = csv.DictReader(file)
            for key in handler:
                if key['username'] == username.lower():
                    user = key
                    break
        print(f'User info\n {user}')
        phone_number = self.compulsory_input('phone-number')
        address = str(input('Enter new address: '))
        if not address:
            address = user['address']
        dob = str(input('Enter D.O.B: '))
        if not dob:
            dob = user['dob']
        gender = self.compulsory_input('gender')

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
                handler = csv.DictWriter(save_data, fieldnames=self.headers)
                handler.writeheader()
                for i in data:
                    handler.writerow(i)
        print('profile updated is successful')
        input_ = input('would you like take another action (y/n): ').lower()
        if 'y' == input_:
            return self.prompt(username)
        else:
            return

    def change_password(self, username):
        user = {}
        with open('new_file.csv', 'r') as file:
            handler = csv.DictReader(file)
            for key in handler:
                if key['username'] == username.lower():
                    user = key
                    break
        print(f'User info\n {user}')
        old_password = self.compulsory_input('old_password')
        password = self.compulsory_input('password')

        print(old_password == user['password'])
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
                        i['password'] = password
                    data.append(i)
            with open('new_file.csv', 'w') as save_data:
                handler = csv.DictWriter(save_data, fieldnames=self.headers)
                handler.writeheader()
                for i in data:
                    handler.writerow(i)
        print('profile updated is successful')
        input_ = input('would you like take another action (y/n): ').lower()
        if 'y' == input_:
            return self.prompt(username)
        else:
            return

    @staticmethod
    def logout(username):
        print(f'you have successfully logged out {username}')
        return

    def prompt(self, username):
        action_ = input("""what will you like to do
            1. Edit profile
            2. Change password
            3. Logout
            """)

        if action_ not in ['1', '2', '3']:
            print('wrong input!')
        else:
            list__ = {
                '1': self.edit_profile,
                '2': self.change_password,
                '3': self.logout
            }
            return list__[action_](username)


if __name__ == '__main__':
    cls = auth()
    action = input("""what will you like to do
                1. Sign up
                2. Sign In
                """)
    if action not in ['1', '2']:
        print('wrong input!')
    else:
        list_ = {
            '1': cls.sign_in,
            '2': cls.sign_up,

        }
        list_[action]()
