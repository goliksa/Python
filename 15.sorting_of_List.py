spam = []
print('Please, input random values 10 times. \
It may be letter, word or number')

for i in range(10):
    print(str(i +1 )+ ':')
    spam.append(input())

# spam = [3, 11, 2, 4, 9, 1, '4', 'four', 'nine', 'a', 'A', 'H']
print('"spam" before sorting: ' + str(spam))

# separate int and str
spam_int = []
spam_str = []

for i in range(len(spam)):
    if type(spam[i]) == int:
        spam_int.append(spam[i])
    else:
        spam_str.append(spam[i])

# sort the lists
spam_int.sort()
spam_str.sort()
spam = spam_int + spam_str

print('"spam after sornting: ' + str(spam))


