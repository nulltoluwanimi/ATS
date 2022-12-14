import csv
import os
from datetime import datetime
import uuid


class Transaction():
    def __init__(self, transaction_type, amount, user):
        self.transaction_type = transaction_type
        self.amount = amount
        self.date = datetime.today().strftime('%Y-%m-%d')
        self.user = user
        self.id = uuid.uuid4().hex

    def init_transaction(self, amount):
        user_transactions = {
            "_id": self.id,
            "_userId": self.user,
            "_amount": amount,
            "_date": self.date,
            "type": self.transaction_type
        }
        if self.save_transaction(**user_transactions):
            return

    @staticmethod
    def save_transaction(**kwargs):
        try:
            if not os.path.exists("transaction.csv"):
                with open('transaction.csv', 'x') as transaction:
                    pass
                with open('transaction.csv', 'a', newline='') as new_transaction:
                    handler = csv.DictWriter(
                        new_transaction, fieldnames=kwargs.keys())
                    handler.writeheader()
                    handler.writerow(**kwargs)
                    return handler
            else:
                with open('transaction.csv', 'a', newline='') as new_transaction:
                    handler = csv.DictWriter(
                        new_transaction, fieldnames=kwargs.keys())
                    handler.writerow(kwargs)
                    return handler
        except Exception as e:
                return e

    @staticmethod
    def get_all_transactions(self):
        with open('transaction.csv', 'r') as file:
            handler = csv.DictReader(file)

            return handler

    @staticmethod
    def get_one_transaction(self):
        user = {}
        with open('wallet.csv', 'r') as file:
            handler = csv.DictReader(file)
            for key in handler:
                if key['_id'] == self.id:
                    user = key
                    break
        return user

    @staticmethod
    def get_all_user_transaction(self):
        user = []
        with open('wallet.csv', 'r') as file:
            handler = csv.DictReader(file)
            for key in handler:
                if key['_userid'] == self.user:
                    user.append(key)
        return user
