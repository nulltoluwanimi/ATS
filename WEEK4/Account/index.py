from user import User

if __name__ == "__main__":
    user = User("Toluwanimi", "Smith")
    account = user.wallet.get_one_wallet()
    print(user.create_user())

    # print(user.wallet.fund_wallet(10, **account))
    # print(user.transaction.init_transaction(10))
