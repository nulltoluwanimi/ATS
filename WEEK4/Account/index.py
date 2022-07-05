from user import User

if __name__ == "__main__":
    user = User("Toluwanimi", "Smith", user="f9909957-e4dd-4be8-8a57-89b618f4ff04")
    account = user.wallet.get_one_wallet()
    print(user.wallet.fund_wallet(10, **account))
    print(user.transaction.init_transaction(10))
