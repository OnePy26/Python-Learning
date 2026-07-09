#Variables
bank_name = "Bank of Bankrupts"
name = "Subho"
account_numeber = "a98658965hn5"
pin = 9889
balance = 0
count = 0
#Functions


def diposite_amt ():
    try:
        diposit = int(input("Enter diposit amount: "))
        balance += diposit
    except:
        print = ("Invalid input - try again..")

def show_balance ():
    pass

def withdraw_amt ():
    pass

def account_details ():
    pass

def enter_pin():
    while True:
        if  count == 3:
            print("Maximum Attempt reached")
            break
        elif pin1 == pin:
            print("Welcome", name)
            break
        elif pin1 != pin:
            count += 1 
            
 

#menu
print("Welcome to Bank of Bankrupts")
enter_pin()



print ("=================== ATM Menu =====================\n"
"1. Withdraw                            2. Diposit\n"
"3. Show Balance                        4. A/C info:\n"
"                     5. Exit                        \n"
"==================================================")

while True:

    choice = input("Enter choice here: ")

    if choice == "1":
        withdraw_amt()
    
    elif choice == "2":
        diposite_amt()

    elif choice == "3":
        show_balance()

    elif choice == "4":
        account_details()