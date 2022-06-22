import random

print('O/P => **************Welcome to Afex Bank ******************')


available_balance = 1000
pin_created = False

def resolve_list(type):
    list_type = {
        '1':100,
        '2':200,
        '3':300,
        '4':400,
    }    
    return list_type.get(type, 'No such services, please check again')

def balance():
    print(f'your available balance is ₦{available_balance}')
    action = input("Would you like to perform another action (y for yes /n for n): ")
    if (action == 'y'):
        ussd()
    else:
        print('Thank you for using our services')

def make_transfer():
    transfer_price = int(input("enter transfer amount: "))
    if transfer_price > available_balance:
        return 'Insufficient funds to make transfer'
    else:
        to = input("enter recipient number: ")
        bank = input("enter recipient bank: ")
        print(f"""
        {transfer_price} transferred to {to}
        New Balance: ₦ {available_balance - transfer_price}
    """)

def generate_OTP():
    print(f' your OTP is {random.randint(9999, 99999)}')

def load_data():
    data_list = int(input("""
    Airtime list 
    1 - 100MB - N100
    2 - 200MB - N200
    3 - 300MB - N300
    4 - 1GB   - N1400
    """))
    resolve_Airtime = resolve_list(data_list)
    if type(resolve_Airtime) == int and resolve_Airtime < available_balance:
        to = input("enter recipient number: ")
        print(f"""
        N{resolve_Airtime} worth  of data transferred to {to} successfull!
        New Balance: ₦ {available_balance - resolve_Airtime}
    """)
    elif resolve_Airtime > available_balance:
        print('Insufficient funds to make request')
        action = input("Would you like to perform another action (y for yes /n for n): ")
        if (action == 'y'):
            ussd()
        else:
            print('Thank you for using our services')
    else:
        return resolve_Airtime

def load_airtime():
    recharge_amount = int(input("""
    Amount you wish to recharge: 
    """))
    if recharge_amount > available_balance:
        print('Insufficient funds to make request')
        action = input("Would you like to perform another action (y for yes /n for n): ")
        if (action == 'y'):
            ussd()
        else:
            print('Thank you for using our services')
    else:
        to = input("enter recipient number: ")
        print(f"""
        N{recharge_amount} airtime sent to {to} successfullly!
        New Balance: ₦ {available_balance - resolve_Airtime}""")


    

def actions(action = None, pin = None, exit_key = 0):
    pin = str(input("please input your PIN: "))
    if '0' == pin:
            ussd()
    elif '1234' == pin:
        action_request = {
            '1': balance,
            '2': make_transfer,
            '3': load_airtime,
            '4': load_data,
            '5': generate_OTP

        }
        print(action)
        action_request[action]()
        return action_request.get(action, 'request failed!, try again later')()

    elif '1234' != pin:
        print('Pin does not match!, enter 0 to go back')
        # exit_key += 1
        actions()
  
def ussd( pin_set:bool = False,pin_created:bool = False):
    action = str(input("""
        You have created a unique pin. what action you will like to perform:
         1. Check Availble Balance
         2. Make Transfer
         3. Load Airtime
         4. Load Data
         5. Generate OTP         
         6, Exit
        """))
    if action not in ['1','2','3','4','5','6']:
        print('Wrong action, Please check again')
        ussd()
    elif '6' == action:
        print('Thanks for using our ussd services')
    else:
        return actions(action)
        

if __name__ == '__main__':
    ussd()



