import json
import os
import csv

first_name = str(input('Enter your first_name: '))
last_name = str(input('Enter your last name: '))
username = str(input('Enter a preferred username: '))
password = str(input('input password:'))
c_password = str(input('confirm password:'))


# assert(password,c_password)
def check_password():
    if password != c_password:
        print('Password does not match!')
        return False
    elif password == c_password:
        return True


user_dict = {'first_name': first_name, 'last_name': last_name, 'username': username, 'password': password}


def file_to_file():
    if check_password():
        if not os.path.exists(f"{username}.txt"):
            with open(f"{username}.txt", 'x') as f:
                pass
            file_handler = open(f"{username}.txt", 'w')
            # data = str(user_dict)
            csv.DictWriter(user_dict)
            print('data saves to file')
            return
        else:
            file_handler = open(f"{username}.txt", 'w')
            data = str(user_dict)
            file_handler.write(data)
            print('data saves to file')
            return


if __name__ == '__main__':
    file_to_file()
