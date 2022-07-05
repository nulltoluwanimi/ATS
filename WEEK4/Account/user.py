import csv
import os
import uuid
import bcrypt
from decimal import Decimal
from wallet import Wallet
from transaction import Transaction


class User(Wallet, Transaction):
    def __init__(self, first_name, last_name, balance=Decimal('0.00'), count=0, user=uuid.uuid4()) -> None:
        # super().__init__(balance, count)
        self._id = user
        self.__first_name = first_name
        self.__last_name = last_name
        self.balance = balance
        self.wallet = Wallet(balance, count, user=self._id)
        self.transaction = Transaction(user=self._id, amount=0.00, transaction_type='basic')

    @property
    def id(self):
        return self._id

    @id.setter
    def set_id(self, value):
        all_user = self.get_all_users()
        for user in all_user:
            if user['_id'] == value:
                self.generate_uniqueid()
            else:
                self._id = value

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def set_first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def set_last_name(self, value):
        return self.__last_name

    @staticmethod
    def save_user(**kwargs):
        print("saving user...")
        try:
            if not os.path.exists("user.csv"):
                with open('user.csv', 'x') as user:
                    pass
                with open('user.csv', 'a', newline='') as new_data:
                    handler = csv.DictWriter(
                        new_data, fieldnames=kwargs.keys())
                    handler.writeheader()
                    handler.writerow(**kwargs)

            else:
                with open('user.csv', 'a', newline='') as new_data:
                    handler = csv.DictWriter(
                        new_data, fieldnames=kwargs.keys())
                    handler.writerow(kwargs)
                    return 'Successful'
        except IOError as err:
            return err

    @staticmethod
    def get_all_users():
        with open('user.csv', 'r') as file:
            handler = csv.DictReader(file)
            return handler

    @staticmethod
    def get_one_user(_id):
        user = {}
        with open('user.csv', 'r') as file:
            handler = csv.DictReader(file)
            for key in handler:
                if key['_id'] == _id:
                    user = key
                    break
        return user

    @staticmethod
    def generate_uniqueid():
        return uuid.uuid4()

    def create_user(self):
        user_data = {
            '_id': self._id,
            'first_name': self.first_name,
            'last_name': self.last_name,
        }
        print('Creating user %s' % user_data)
        if self.save_user(**user_data):
            return 'User created successfully'
        else:
            return 'Seems operation is down at the moment, please try again later'

    @staticmethod
    def hash_password(value):
        salt = bcrypt.gensalt(10)
        hashed = bcrypt.hashpw(value, salt)
        return hashed

    @staticmethod
    def get_password(hashed, value):
        return bcrypt.checkpw(value, hashed)

    @classmethod
    def delete_user(cls, _id):
        user = {}
        new_data = []
        with open('user.csv', 'r') as file:
            handler = csv.DictReader(file)
            for key in handler:
                if key['_id'] == _id:
                    user = key
                    break
        password = str(input('Enter password'))
        if cls.get_password(user.password, password):
            users = cls.get_all_users()
            for user in users:
                if user['_id'] == _id:
                    user.remove(users[user])
                new_data.append(user)
        with open('user.csv', 'w') as save_data:
            handler = csv.DictWriter(save_data, fieldnames=user.keys())
            handler.writeheader()
            for i in new_data:
                handler.writerow(i)
            else:
                print('Wrong password')
                cls.delete_user(_id)
