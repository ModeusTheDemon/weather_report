from account_system.user_account import User
from account_system.validations import validations
import os

class account_cl_actions:
    def Create_account() -> User:
        try:
            print('to create your account we need to get next information:')
            
            print('\naccount name(from 4 to 30 symbols)\n')   # создание имени аккаунта
            name = input()
            while not validations.name_validation(name= name):
                print('please, enter your name\n')
                name = input()
            
            print('\naccount mail(to skip press Enter)\n')
            mail = input()         # ввод почты (опционально)
            while mail != '' and validations.mail_validation(mail= mail):
                print('invalid mail, try again\n')
                mail = input()
            else:
                mail = None
            
            print("\naccount login\nyour password must be 4-16 letters long and contain any of any english letter, number or '-', '_' symbols\n")
            login = input()       # создание логина (>= 4 символов)
            while not validations.login_validation(login= login):       # валидация логина
                print('invalid login, try again\n')
                login = input()
            
            print('''\naccount password.
- The password must contain at least one lowercase letter.
- The password must contain at least one capital letter.
- The password must contain at least one number.
- The password must contain at least one special character [@ $!%*?&].
- The password must be 8 or more characters.\n''')
            password = input()     # создание пароля (>= 8 символов)
            while not validations.password_validation(password= password):    # валидация пароля
                print('invalid password, try again\n')
                password = input()
            
            #создание объекта класса User
            user = User(name= name,
                        mail= mail,
                        login= login,
                        password= password)
            
            try:
                # создание файлов с данными и историей аккаунта
                os.chdir(path= r'pythonprojects\weather_project\accounts and history')
                account_info_file = open(f'{login}.txt', 'w')
                account_history_file = open(f'{login} history.txt', 'x')
                account_info_file.write(f"{name}\n{mail}\n{login}\n{password}")
                account_info_file.close()
            except FileExistsError:   # аккаунт уже существует
                print("account already exist\n")
                return False
            
            return user
        except Exception as e:   # непредвиденная ошибка
            print("unexpected error, try again\n", e)
            return False
    
    def Log_in_account() -> User:
        print("Please input login and password")
        t_login = input("input login\n")   # введеный пользователем логин аккаунта
        t_password = input("input password\n")   # введеноый пользователем пароль от аккаунта
        try:   # проверка на наличие аккаунта
            os.chdir(path= r'pythonprojects\weather_project\accounts and history')
            account_info = open(f"{t_login}.txt", "r").readlines()
        except:
            print("no account with that login")
            return False
        if account_info[2].strip() == t_login and account_info[3].strip() == t_password:   # вход в аккаунт
            user = User(name= account_info[0].strip(),
                        mail= account_info[1].strip(),
                        login= account_info[2].strip(),
                        password= account_info[3].strip())
        else:   # ошибка входа
            print("wrong login or password")
            return False
        print(f'{user.name} now loged in!')
        return user