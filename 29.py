import re

def validate_email(email):
    if re.match('^[a-zA-Z1-9\.\_]+@[a-zA-Z1-9]+\.[a-zA-Z1-9]{3}$',email):
        return(bool(True))
    else:
        return(bool(False))

def validate_phone(number):
    if re.match('^\+989[0-9]{9}$',number):
        return(bool(True))
        pass
    elif re.match('^09[0-9]{9}$',number):
        return(bool(True))
        pass
    elif re.match('^00989[0-9]{9}$',number):
        return(bool(True))
        pass
    else:
        return(bool(False))
        pass