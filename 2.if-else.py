password = "123abc" #etalon password

print("Hallo, rookey! What is you name?")
print("Please, inpit here:")

name = input()

if name:
    print("Thank you!")
else:
    print("You didn't inpit your name, please,do it!")
    name = input()

    if name:
      print("Thank you, " + name + "!")
    else:
      name = "INCOGNITO"
      print("Ok, lets it be " + name + "!")
    

print(name + ", to continue, you should enter password:")

user_password = input()

if user_password:
    if user_password == password:
        print("Hooraaah" + "!" * 3 + name + ", now you are a new member!")
    else:
        print("Yor password is wrong. Please, try againe later!")
else:
    if name == "INCOGNITO":
              print("If you don't want to enter you name and don't want to enter the password what do you do here????")
    else:  
              print("You missed your attempt. Please, try againe later!")


              
print()              
print("Good by, " + name + "!")

input()
