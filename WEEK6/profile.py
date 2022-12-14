import csv
from typing import AnyStr


class Profile:
    def __init__(self):
        self.users = self.get_all_users()

    def __repr__(self):
        return f'<User {self.users}>'

    @staticmethod
    def get_all_users():
        with open('users.csv', 'r') as file:
            handler = csv.DictReader(file)
            return handler

    def get_one_user(self, username):
        user = {}
        for key in self.users:
            if key['username'] == username:
                user = key
                break
        return user

    @staticmethod
    def save_user(**kwargs) -> AnyStr:
        print("saving user...")
        try:
            with open('user.csv', 'a', newline='') as new_data:
                handler = csv.DictWriter(
                    new_data, fieldnames=kwargs[0].keys())
                handler.writerows(kwargs)
                return 'Successful'
        except Exception as err:
            return str(err)

    def edit_profile(self, user, key, value):
        try:
            data = []
            for i in self.users:
                if i['username'] == user:
                    i[f'{key}'] = value
                data.append(i)
            return data
        except Exception as err:
            return err

