#This is a more refined version of the calculator with while loop.
#It exits with user command.
#Error handling not available.

while True:
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    calc = int(input("Choose calculation :\n"
    "1. For Addition: \n"
    "2. For Subtraction: \n"
    "3. For Multiplication: \n"
    "4. For Division: \n"
    "Enter your choice here: "))

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
 #user command exit in current loop to be indented same with the earlier If and elif's.   
    choice = input("Do you want another calculation (Y/N): ").upper()
    if choice == "Y":
        continue
    elif choice == "N":
        break