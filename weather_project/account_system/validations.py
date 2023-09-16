from re import match

class validations:
    
    def password_validation(password):
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        if match(pattern= pattern, string= password):
            return True
        else:
            return False
    
    def login_validation(login):
        pattern = r"^[a-zA-Z0-9_-]{4,16}$"
        if match(pattern, login):
            return True
        else:
            return False
    
    def mail_validation(mail):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if match(pattern, mail):
            return True
        else:
            return False
    
    def name_validation(name):
        if 3 < len(name) < 31:
            return True
        else:
            return False