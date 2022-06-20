import random



# saved_pin,firstname,lastname,amount
# user_data = {
#         saved_pin: 0,
#         firstname : "",
#         lastname :"",
#         amount : 0.00,
#     }
    
def atm_app():
        def open_account_or_create_pin():
                first_name = input('Please input your first name: ')
                last_name = input('Please input your last name: ')
                pin1 = int(input('Please choose a 4-digit PIN: '))
                pin2 = int(input('Please input your PIN again: '))
                balance = 0
                if pin1 != pin2:
                    print("PIN doesn't match! Please try again ")
                    pin1 = int(input('Please choose a 4-digit PIN: '))
                    pin2 = int(input('Please input your PIN again: '))
                else:
                    saved_pin = pin1
                    print('Yoo! PIN attached to your account')
                    user_data = {
                        "firstname": first_name,
                        "lastname": last_name,
                        "saved_pin":saved_pin,
                        "balance": balance
                    }
                    print(f'Welcome {first_name}{last_name}')
                    return user_data

       

        def check_balance():
            remaining_balance = balance
            print(f"Your balance is: #{remaining_balance}.00")
            return 

        def buy_airtime():
            print("1 This Phone")
            print('2 Another number')
            choice = input(": ")
            amount = input("please input amount: ")
            
            if amount < balance: print("Insufficient funds!")
            
            elif (choice == "1"):
                validate_user()
                print(f"Your recharge of {amount} was successful!")
                balance -= amount
            elif choice == 2:
                phone_number = int(input(" Input recipient phone number: "))
                print(f"Your recharge of {amount} to {phone_number} was successful!")
                balance -= amount
                return


        def buy_data():
            print("1 This Phone")
            print('2 Another number')
            phone_number = input("")
            
            print("1 Daily Plans")
            print('2 Weekly Plans')
            print("3 Mega Plans")
            print('4 Night/Weekend Plans')
            plan = int(input(': '))

            def daily_plans():
                print("1 This Phone")
                print('2 Another number')
                return
                
            def weekly_plans():
                print("1 2GB for #700")
                print("2 5GB for #1500")
                print("3 10GB for #3000")
                return 
            def mega_plans():
                return


            if  plan == 1:
                daily_plans()
            elif plan == 2:
                weekly_plans()
            elif plan == 3:
                mega_plans()
                print(f"Your recharge of {amount} to {phone_number} was successful!")
            return
   
        def generate_otp():
            uniqueotp = random.randint(1000,9999)
            print(f"Your unique otp is  {uniqueotp}")
            return uniqueotp

        def home_info():
                print('Welcome to USSD Banking with AFEX! please choose an operation')
                print("1 Open Account/Validate PIN ")
                print("2 Check Balance ")
                print("3 Buy Airtime ")
                print("4 Buy Data ")
                print("5 Generate a one-time OTP ")
                keyed_num = int(input(':'))

                if keyed_num == 1:
                     open_account_or_create_pin()
                elif keyed_num == 2:
                    check_balance()
                elif keyed_num == 3:
                    buy_airtime()
                elif keyed_num == 4:
                    buy_data()
                elif keyed_num == 5:
                    generate_otp()
        home_info()

        user_data = open_account_or_create_pin()
        print(user_data)
        saved_pin = user_data["saved_pin"]
        balance = user_data["balance"]

        def validate_user():
                pin = input('Please input your pin:')
                if pin != saved_pin:
                    print("Incorrect pin! Please input a correct or create a unique pin")
                    # open_account_or_create_pin()
                print("Success!")
                return 


                

        



        


        
        home_info()

print(atm_app())