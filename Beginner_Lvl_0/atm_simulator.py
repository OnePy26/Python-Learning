#Variables
bank_name = "Bank of Bankrupts"
name = "Subho"
account_number = "a98658965hn5"
pin = 9889
balance = 0

#Functions
def withdraw_amt ():
    global balance
    while True:
        try:
            amount = int(input("Enter amount to withdraw: "))
            if amount == "e":
                break
            elif amount > balance:
                print ("Insufficient Funds: Try")
            elif amount <= 0:
                print ("Amount cannot be negative: Enter valid amount")
            else:
                balance = balance - amount
                print ("Amount Disbursed: Thank you for availing the services")
                break
        except:
            break

        
        
def diposite_amt ():
    global balance
    while True:
        try:
            amount = int(input("Enter diposite amount: "))
            if amount == "e":
                break
            elif amount <= 0:
                print ("Amount cannot be negative or 0: Enter valid amount")
            else:
                balance = balance + amount
                print ("Amount Diposited: Thank you for availing the services: New balance: ", balance)
                break
        except:
            break

def show_balance ():
    print ("Available balance: ", balance)
    break


def account_details ():
    print ("Bank Name: \n", name
    "Account Holder Name: \n"
    "Account numbere: \n"
    "Updated Balance: ", balance)
    

def enter_pin():
    count = 0
    while True:
        try:
            pin1 = int(input("Enter Pin: "))
            if  count == 2:
                print("Maximum Attempt Reached: Exiting simulation")
                break
            elif pin1 == pin:
                print("Welcome", name)
                break
            elif pin1 != pin:
                count += 1
                print("Wrong Pin: Try again")
        except:
            break
                    
 
#menu
print("Welcome to Bank of Bankrupts")
enter_pin()



print ("=================== ATM Menu =====================\n"
"1. Withdraw                            2. Diposit\n"
"3. Show Balance                        4. A/C info:\n"
"                     5. Exit                        \n"
"==================================================")

#loop post menu
while True:

    choice = input("Enter choice here: ")

    if choice == "1":
        withdraw_amt()
    
    elif choice == "2":
        diposite_amt ()

    elif choice == "3":
        show_balance()

    elif choice == "4":
        account_details()