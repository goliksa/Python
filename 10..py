print('This is a simpl prin of a dictionary, the items is printed with out order')
print()

message = 'Hi, my name is Sergey, I am 32 ears old and I live in\
                    Germany now'
count = {}

for character in message:           # for character in message.upper(): 
    count.setdefault(character, 0)
    count[character] += 1 

print(count)
print()


print('This is a \"pprint\" prin of a dictionary, the items is printed IN ordered column')
print()

import pprint
message = 'Hi, my name is Sergey, I am 32 ears old and I live in\
                    Germany now'
count = {}

for character in message:           # for character in message.upper(): 
    count.setdefault(character, 0)
    count[character] += 1 

pprint.pprint(count)
print()

rjtext = pprint.pformat(count)
print('rjtext = ')
print(rjtext)


