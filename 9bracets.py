eggs_number = 1
eggs_string = 'simple string'
eggs_list = [1, 2, 3]
eggs_dictionary = {1: 'one', 2: 'two', 3: 'three'}

print('This is a number: ' + str(eggs_number))
print('This is a string: ' + eggs_string)
print('This is a list: ' + str(eggs_list))
print('This is a 0 index value of list: ' + str(eggs_list[0]))
print('This is a 2 index value of list: ' + str(eggs_list[2]))
print('This is a dictionary: ' + str(eggs_dictionary))
print('This is a value of kay 1 in the dictionary: ' + eggs_dictionary[1])
print('If is ther 4 kay in the dictionary? ' + eggs_dictionary.get(4, 'No!'))

ham = {1: 'one', 2: 'two'}
print(ham)

ham.setdefault(3, 'three')
print(ham)

ham.setdefault(3, '3')
print(ham)
