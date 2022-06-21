import random

print('O/P => **************Welcome to Afex Bank ******************')

available_balance = 1000
pin_created = False


def resolve_list(type):
    list_type = {
        '1': 100,
        '2': 200,
        '3': 300,
        '4': 1400,
    }

    return list_type.get(type, 'No such services, please check again')


def call_main():
    action = input("Would you like to perform another action (y for yes /n for n): ")
    if action == 'y':
        ussd()
    else:
        print('Thank you for using our services')


def deduct_balance(amount):
    return available_balance - amount


def balance():
    print(f'Your available balance ₦{available_balance}')
    call_main()


def make_transfer():
    transfer_price = int(input("enter transfer amount: "))
    if transfer_price > available_balance:
        print('Insufficient funds to make transfer')
        call_main()
    else:
        to = input("enter recipient number: ")
        bank = input('enter recipient bank: ')
        deduct_balance(transfer_price)
        print(f"""
        {transfer_price} transfer to {bank} - {to}
        New Balance: ₦ {available_balance - transfer_price}
    """)


def generate_otp():
    print(f' your OTP is {random.randint(999, 9999)}')
    call_main()


def load_data():
    airtime_list = input("""
    Data list 
    1 - 100MB - N100
    2 - 200MB - N200
    3 - 300MB - N300
    4 - 1GB   - N1400
    """)
    resolve_airtime = resolve_list(airtime_list)
    if type(resolve_airtime) == int and resolve_airtime < available_balance:
        to = input("enter recipient number: ")
        deduct_balance(resolve_airtime)
        print(f"""
        N{resolve_airtime} worth  of data transferred to {to} successfully!
        New Balance: ₦ {available_balance - resolve_airtime}
    """)
    elif resolve_airtime > available_balance:
        print('Insufficient available to process request')
        call_main()
    else:
        print(resolve_airtime)


def load_airtime():
    recharge_amount = int(input("enter recharge amount: "))
    if recharge_amount > available_balance:
        print('Insufficient funds to make transfer')
        call_main()
    elif recharge_amount < available_balance:
        to = input("enter recipient number: ")
        deduct_balance(recharge_amount)
        print(f"""
            N{recharge_amount} worth  of data transferred to {to} successfully!
            New Balance: ₦ {available_balance - recharge_amount}
        """)


def actions(action=None, pin=None, exit_key=0):
    pin = input("please input your PIN: ")
    if '0' == pin:
        ussd()
    elif '1234' == pin:
        action_request = {
            '1': balance,
            '2': make_transfer,
            '3': load_airtime,
            '4': load_data,
            '5': generate_otp

        }
        return action_request.get(action, 'request failed!, try again later')()

    elif '1234' != pin:
        print('Pin does not match!, enter 0 to go back')
        actions()


def ussd(pin_set: bool = False, ):
    action = str(input("""
         USSD options
         what action you will like to perform:
         1. Check Available Balance
         2. Make Transfer
         3. Load Airtime
         4. Load Data
         5. Generate OTP         
         6. Exit
        """))
    if action not in ['1', '2', '3', '4', '5', '6']:
        print('Wrong action, Please check again')
        ussd()
    elif '6' == action:
        print('Thanks for using our ussd services')
    else:
        return actions(action)


if __name__ == '__main__':
    ussd()
