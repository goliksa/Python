# Program for guess the number

import random

print("Hello, what is you name?")
user_name = input()

print("Well, " + user_name + ", I am thinking of a number between 1 and 20. ")

secret_number = random.randint(1, 20)

# print("DEBAG: secret_number is: " + str(secret_number))

for guess_attempt in range (1, 7):
    print("Please, take a guess.")
    user_number = int(input())
    
    if user_number < secret_number:
        print("To low!")
    elif user_number > secret_number:
        print("To big!")
    else:
        break
    
if user_number == secret_number:
    print("Well done, " + user_name + "! You guess my namber in " + str(guess_attempt) + " attemps!") 
else:
    print("You didn't manage with the task, my number was: " + str(secret_number))
