def golf(number):
    result = 1
    for i in range(len(str(number))):
        if int(str(number)[i]) == 0:
            continue
        else:
            result *= int(str(number)[i])
    return result
    
golf(1034)

'''
num = 123456

for i in range(len(str(num))):
               print(i)
'''
