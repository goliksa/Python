def golf(password):
    if password.isdecimal() or password.isalpha() or password.istitle() or len(password) < 10 or password.islower() or password.islower() or password.isupper() and not password.isalnum():
        print('False')
        return False
    elif password:
        letters = ""
        for i in range(len(password)):
            if password[i].isalpha():
                letters = letters + password[i]
        print(letters)
        if letters.isupper() or letters.islower():
            print('False')
            return False
        else:
            print('ERROR!')
    else:
        print('True')
        return True

golf("ULFFunH8ni")

