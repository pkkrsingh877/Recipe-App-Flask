import string 

def validate_password(password):
    # 1 uppercase, 1 lowercase, 1 digit, min length = 8, max length = 20
    # 1 special character
    isUppercase = False
    isLowercase = False
    minLength = False
    maxLength = False
    isDigit = False
    isSpecialCharacter = False
    
    if len(password) >= 8 and len(password) <= 20:
        minLength = True
        maxLength = True
        for letter in password:
            
            if letter in string.ascii_uppercase:
                isUppercase = True
            if letter in string.ascii_lowercase:
                isLowercase = True
            if letter in string.digits:
                isDigit = True
            if letter in string.punctuation:
                isSpecialCharacter = True
    
    if isUppercase and isLowercase and minLength and maxLength and isDigit and isSpecialCharacter:
        return True
    else:
        return False