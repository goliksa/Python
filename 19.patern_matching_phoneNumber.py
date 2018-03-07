def isPhoneNumber (text):  # 123-123-1234
    if len(text) != 12:
        return False
    for i in range(0, 3) and range(4, 7) and range(8, 12):
        if not text[i].isdecimal():
            return False
    if text[3] and text[7] != '-':
        return False
    return True

print(isPhoneNumber('123-123-1234'))
    
