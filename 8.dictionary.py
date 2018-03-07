spam = {'name': 'Serg', 'age': 32, 'sex': 'man'}

print('Keys of spam: ' + str(spam.keys()) + '.')

spam_keys = list(spam.keys())

print(spam_keys)

print('Keys of spam: ' + str(spam_keys[0]) + ', ' + str(spam_keys[1]) + ', ' +  str(spam_keys[2]) + '.')

print('name = ' + spam.get('name') + ', age = ' + str(spam.get('age')) + ', adress = ' + spam.get('adress', 'none'))
