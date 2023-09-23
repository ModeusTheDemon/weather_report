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
            5. check latest search
            6. quit from account
            7. quit
            
            warning!!!
            After you exit the program, you will need to log into your account again
            """)


def main():
    loged_in = False
    welcome()
    while True:
        inp = input("input command number: ")
        if inp == '0':
            if loged_in:
                print(f'''
                      ***
                      {user.name}
                      ***
                      ''')
            else:
                print('you need to log in first\n\n')
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
                print('you need to log in first\n\n')
        elif inp == '4':
            if loged_in:
                weather_report.weather_output(user)
                welcome()
            else:
                print('you need to log in first\n\n')
        elif inp == '5':
            if loged_in:
                with open(f'{user.login} history.txt', 'r') as file:
                    file = file.readlines()[-10:]
                    time = file[1]
                    city = file[2]
                    weather = file[3]
                    temperature = file[4]
                    delta = file[5]
                    feels_like = file[6]
                    pressure = file[7]
                    wind = file[8]
                    print(f'''time: {time}
city: {city.strip()}
weather: {weather.strip()}
temperature: {temperature.strip()} °C
delta: +-{delta.strip()} °C
feels like: {feels_like.strip()} °C
pressure: {pressure.strip()} 
wind: {wind.strip()} m/s\n\n''')
            else:
                print('you need to log in first\n\n')
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