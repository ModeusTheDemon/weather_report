from account_system.account_create_and_login import account_cl_actions
from account_system.account_actions import account_actions
from weather_system.weather_report import weather_report


def welcome():
    print("""
            Weather report V0.0.1
            
            commands:
            0. current account
            1. create account
            2. log in account
            3. account actions
            4. check weather report
            5. check history
            6. quit from account
            7. quit
            
            warning!!!
            After you exit the program, you will need to log into your account again
            """)


def main():
    loged_in = False
    welcome()
    while True:
        inp = input("\ninput command number: ")
        if inp == '0':
            if loged_in:
                print(f'''
                      ***
                      {user.name}
                      ***
                      ''')
            else:
                print('not loged in!')
        elif inp == '1':   
            user = account_cl_actions.Create_account()
            loged_in = True if user else False
            welcome()
        elif inp == '2':   
            user = account_cl_actions.Log_in_account()
            loged_in = True if user else False
            welcome()
        elif inp == '3':   
            if loged_in:
                account_actions.menu(user= user)
            else:
                print("you need to log in account first")
        elif inp == '4':
            if loged_in:
                weather_report.weather_output()
                welcome()
            else:
                print('you need to log in first\n\n')
        elif inp == '5':
            pass
        elif inp == '6':
            if loged_in:
                del user
                loged_in = False
                welcome()
        elif inp == '7':
            break
        else:
            print('Unknown command')


if __name__ == '__main__':
    main()