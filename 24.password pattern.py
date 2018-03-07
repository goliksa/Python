import re

def passwordValidation (password):
    passRegex = re.compile(r'[a-z]+[A-Z]+[0-9]+')
    mo = passRegex.search(password)
    print(mo)
    if mo != None and len(password) >9:
        print('True')
        return True
    else:
        print('False')
        return False

passwordValidation('Fa11con77YES')    
    
