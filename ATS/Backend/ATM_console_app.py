saved_pin = 0
user_data = { }



def create_PIN():
        pin1 =  int(input('Please choose a 4-digit PIN'))
        pin2 =  int(input('Please input your PIN again'))
        if pin1 != pin2:
            print("choose PIN doesn't match! Please try again ")
        saved_pin  = pin1
        user_data = { }
        print('Yoo! PIN attached to your account')



user_data = { }


def open_account_or_create_PIN():
        firstName =  str(input('Please input your first name:'))
        lastName =  str(input('Please input your last name:'))
        
        user_data = {
            "firstname": firstName,
            "lastname": lastName
        }
        print(f'Welcome {firstName}{lastName}')
        create_PIN()
        


        userName2 =  input('Please validate your Username:')
        password2 =  input('Please validate your Password:')

       
           


output = print('Welcome please choose an operation')
print("1 Open Accout/Validate PIN ")
print("2 Check Balance ")
print("3 Buy Airtime ")
print("4 Buy Data ")

keyed_num = int(input(''))
if keyed_num == 1:
        open_account_or_create_PIN

account_balance = 1000



















def validate_PIN(pin:int):
        if  (pin != saved_pin):
                print("Incorrect PIN! Please try again. ")
        return "Transaction Successful"
                # return "Incorrect PIN! Please try again. "