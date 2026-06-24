#This one tests the user name and password against stored variable.
# != (not equal to)
#== (equals to; compares if true to condition )

username = ("petrol")
password = ("P3254L")

name = input("Enter your name: ")
user_input = input("Enter username: ")
pass_input = input("Enter password: ")

if user_input == username and pass_input ==password:
    print(f"Login Successfull: Welcome {name}")
elif user_input != username and pass_input !=password:
    print("Incorrect Username & Password")
elif user_input != username:
    print("Incorrent username")
elif pass_input != password:
    print("Incorrent password")
else:
    print("Invalid Input")