while True:

    name = input("Enter name here : ")
    age = int(input("Enter age here : "))
    
    if age < 18:
        print(f"{name}, is not elligible")
    elif age >= 18:
        print(f"{name}, is elligible")
    else:
        print("Invalid input")
        
    check = str(input("Do you wish to check another: (Y/N) ") )
    if check == "Y":
        continue
    elif check =="N":
        break