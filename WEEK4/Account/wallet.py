import csv
import os
import uuid
from decimal import Decimal


class Wallet:
    def __init__(self, balance, transaction_count, user):
        self.balance = balance
        self.transaction_count = transaction_count
        self.user = user

    @staticmethod
    def save_wallet(**kwargs):
        if not os.path.exists("wallet.csv"):
            with open('wallet.csv', 'x') as wallet:
                pass
            with open('wallet.csv', 'a', newline='') as new_wallet:
                handler = csv.DictWriter(new_wallet, fieldnames=kwargs.keys())
                handler.writeheader()
                handler.writerow(**kwargs)
        else:
            with open('wallet.csv', 'a', newline='') as new_wallet:
                handler = csv.DictWriter(new_wallet, fieldnames=kwargs.keys())
                handler.writerow(kwargs)

    @staticmethod
    def get_all_users():
        with open('wallet.csv', 'r') as file:
            handler = csv.DictReader(file)
            return handler

    def create_wallet(self):
        try:
            new_wallet = {
                '_userid': self.user,
                'balance': self.balance,
                'transaction_count': self.transaction_count
            }
            if self.save_wallet(**new_wallet):
                return 'User created successfully'
        except Exception as e:
            return e

    @staticmethod
    def get_all_wallet():
        with open('wallet.csv', 'r') as file:
            handler = csv.DictReader(file)
            return handler

    def get_one_wallet(self):
        user = {}

        with open('wallet.csv', 'r') as file:
            handler = csv.DictReader(file)
            for key in handler:
                if key['_userid'] == self.user:
                    user = key
                    break
        return user

    @staticmethod
    def fund_wallet(amount, **kwargs):
        try:
            with open('wallet.csv', 'r') as update_file:
                handler = csv.DictReader(update_file)
                data = []
                for i in handler:
                    if i['_userid'] == kwargs['_userid']:
                        i['balance'] = Decimal(amount) + Decimal(kwargs['balance'])
                    data.append(i)
                print(data)
            with open('wallet.csv', 'w') as save_data:
                handler = csv.DictWriter(save_data, fieldnames=kwargs.keys())
                handler.writeheader()
                for i in data:
                    handler.writerow(i)
            return 'Transaction successful'
        except IOError as err:
            return err

    @staticmethod
    def send_funds(_id, amount, **kwargs):
        try:
            with open('wallet.csv', 'r') as update_file:
                handler = csv.DictReader(update_file)
                data = []
                for i in handler:
                    if i['_userid'] == _id:
                        i['amount'] = kwargs['available_balance'] - \
                            Decimal(amount)
                    data.append(i)
            with open('wallet.csv', 'w') as save_data:
                handler = csv.DictWriter(save_data, fieldnames=kwargs.keys())
                handler.writeheader()
                for i in data:
                    handler.writerow(i)
            return 'Transaction successful'
        except IOError as err:
            return err
