#This program allows maximum 3 attempts to enter correct stored username and variable.

username = "petrol"
password = "P3254L"

count = 0
#Putting input for name before the while loop ensures that Name input is asked only once.
name = input("Enter your name: ")
while True:
    
    user_input = input("Enter username: ")
    pass_input = input("Enter password: ")

    if user_input == username and pass_input ==password:
        print(f"Login Successfull: Welcome {name}")
# Break is placed here so the program terminates upon successfull username and pass ignoring the rest of the loop.
        break
    else:
        count = count + 1
# number of attempts can be changed by changing 3 to any desired number number
        if count == 3:
            print("Maximum attempt reached")
            break
        if user_input != username:
            print("Wrong username")
        if pass_input != password:
            print("Wrong password")