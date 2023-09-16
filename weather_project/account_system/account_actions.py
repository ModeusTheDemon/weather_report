from account_system.validations import validations
from account_system.user_account import User
import os

class account_actions:
    
    def menu(user: User):
        global loged_in
        print("""
                account actions:
                1. change name
                2. change mail
                3. change login
                4. change password
                5. delete account
                6. exit menu
                """)
        while inp != '6':    
            inp = input("enter action number: ")
            print('\n')
            if inp == '1':
                account_actions.account_rename(user= user)
            elif inp == '2':
                account_actions.account_change_mail(user= user)
            elif inp == '3':
                account_actions.account_change_login(user= user)
            elif inp == '4':
                account_actions.account_change_password(user= user)
            elif inp == '5':
                account_actions.account_delete(user= user)
                loged_in = False
            else:
                print('unknown command')
    
    def account_delete(user: User) -> None:   # функция удаления аккаунта
        print("Do you really want to delete your account?\n")
        answer = input("Y/N?\n")
        if answer == "Y":
            os.chdir(path= r'pythonprojects\weather_project\accounts and history')
            os.remove(f"{user.login}.txt")
            os.remove(f"{user.login} history.txt")
            print("Done!")
        else:
            print("canceling account deliting")
    
    
    def account_rename(user: User) -> None:   # функция смены имени аккаунта
        print("Do you really want change your account name?\n")
        answer = input("Y/N?\n")
        if answer == "Y":
            new_name = input("Enter new name: ")
            while not validations.name_validation(name= new_name):
                print('invalid name, please try again\n')
                new_name = input("Enter new name: ")
            os.chdir(path= r'pythonprojects\weather_project\accounts and history')
            with open(f'{user.login}.txt', 'r') as file:
                old_data = file.read()
                old_name = old_data.split()[0].strip()
            new_data = old_data.replace(old_name, new_name)
            with open(f'{user.login}.txt', 'w') as file:
                file.write(new_data)
            user.name = new_name
            print("Done!")
        else:
            print("canceling name changing")

    
    def account_change_mail(user: User) -> None:   # функция смены почты аккаунта
        print("Do you really want change your account mail?\n")
        answer = input("Y/N?\n")
        if answer == "Y":
            new_mail = input("Enter new mail: ")
            while new_mail != '' and not validations.mail_validation(new_mail):
                print('invalid mail, try again\n')
                new_mail = input("Enter new mail: ")
            os.chdir(path= r'pythonprojects\weather_project\accounts and history')
            with open(f'{user.login}.txt', 'r') as file:
                old_data = file.read()
                old_mail = old_data.split()[1].strip()
            new_data = old_data.replace(old_mail, new_mail)
            with open(f'{user.login}.txt', 'w') as file:
                file.write(new_data)
            user.mail = new_mail
            print("Done!")
        else:
            print("canceling mail changing")
    
    
    def account_change_login(user: User) -> None:   # функция смены логина аккаунта
        print("Do you really want change your account login?\n")
        answer = input("Y/N?\n")
        if answer == "Y":
            new_login = input("Enter new login: ")
            while not validations.login_validation(new_login):
                print('invalid login, try again\n')
                new_login = input("Enter new login: ")
            os.chdir(path= r'pythonprojects\weather_project\accounts and history')
            with open(f'{user.login}.txt', 'r') as file:
                old_data = file.read()
                old_login = old_data.split()[2].strip()
            new_data = old_data.replace(old_login, new_login)
            with open(f'{user.login}.txt', 'w') as file:
                file.write(new_data)
            os.rename(f"{old_login}.txt", f"{new_login}.txt")
            os.rename(f"{old_login} history.txt", f"{new_login} history.txt")
            user.login = new_login
            print("Done!")
        else:
            print("canceling login changing")
    
    
    def account_change_password(user: User) -> None:   # функция смены пароля аккаунта
        print("Do you really want change your account password?\n")
        answer = input("Y/N?\n")
        if answer == "Y":
            new_password = input("Enter new password: ")
            while not validations.password_validation(new_password):
                print('invalid password, try again\n')
                new_password = input("Enter new password: ")
            os.chdir(path= r'pythonprojects\weather_project\accounts and history')
            with open(f'{user.login}.txt', 'r') as file:
                old_data = file.read()
                old_password = old_data.split()[3].strip()
            new_data = old_data.replace(old_password, new_password)
            with open(f'{user.login}.txt', 'w') as file:
                file.write(new_data)
            user.password = new_password
            print("Done!")
        else:
            print("canceling password changing")