spam = '1, 2, 3'

def eggs (cheese):
    chees = '1, 2, 3, Hello'
    

eggs(spam)
print(spam)
print()    

spam = [1, 2, 3]

def eggs (cheese):
    cheese.append('Hello')
        

eggs(spam)
print(spam)
print()

import copy

spam = ['A', 'B', 'C', 'D']
spam2 = spam
cheese = copy.deepcopy(spam)
cheese2 = cheese
print('cheese2 = ' + str(cheese2))
cheese[1] = 42

print(spam)
print(cheese)

print(spam2)
print(cheese2)












