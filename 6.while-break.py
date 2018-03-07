def attempt (name):
    print (name + ", how are you? \"good\"  or \"bad\"" )
    

print('Enter you name')
input_name = input()

while True:
    attempt(input_name)
    mood = input()
    if mood == 'good' or mood == 'bad' or mood == 'Good' or mood == 'Bad':
        break
    else:
        print('It is should be \"good\"  or \"bad\"' )

if mood == 'good' or mood == 'Good':
    print('I glad to hear it!')
else:
    print('I realy hop It\'ll be  OK')
    
