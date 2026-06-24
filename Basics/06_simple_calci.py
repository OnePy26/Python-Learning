# This is a simple calculator with + - * and / with two numbers only.
# No loop here. this will work for one calculation and needs to be run again to re calculate.
#no error handling.

num1 = float(input("Enter  first number here : "))
num2 = float(input("Enter second number here : "))

calc = int(input("Select calculation: \n"
"Choose 1 for Addition \n"
"Choose 2 for Substraction \n"
"Choose 3 for Multiplication \n"
"Choose 4 for Division \n"
"ENter your choice here: "))

if calc == 1:
    print(f"{num1 + num2:.2f}")
elif calc == 2:
    print(f"{num1 - num2:.2f}")
elif calc == 3:
    print(f"{num1 * num2:.2f}")
elif calc == 4:
    print(f"{num1 / num2:.2f}")
else:
    print("Invalid input")