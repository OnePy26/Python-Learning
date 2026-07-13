# Variables
bank_name = "Bank of Bankrupts"
name = "Subho"
account_number = "a98658965hn5"
pin = 9889
balance = 0


#Functions
def withdraw_amt ():    # Def function to Withdraw amount.
    global balance
    while True:
        try:
            amount = input("Enter amount to withdraw: ")
            if amount.lower() == "e":
                break
            amount = float(amount)
            if amount > balance:
                print ("Insufficient Funds: Try Again")
            elif amount <= 0:
                print ("Amount cannot be negative: Enter valid amount")
            else:
                balance -= amount
                print ("Amount Disbursed: Thank you for availing the services")
                break
        except:
            print("Invalid Input : Enter numbers only")
       
def deposit_amt ():    # Def function to diposit amount.
    global balance
    while True:
        try:
            amount = input("Enter deposit amount(E - Exit to main Menu): ")
            if amount.lower() == "e":
                break
            amount = float(amount)
            if amount <= 0:
                print ("Amount cannot be negative or 0: Enter valid amount")
            else:
                balance += amount
                print ("Amount Deposited: Thank you for availing the services: New balance: ", balance)
                break
        except:
            print("Invalid Input : Enter numbers only")

def show_balance ():    # Def function to show balance amount.
    print ("Available balance: ", balance)


def account_details ():     # Def function to show balance amount
    print (f"Bank Name: {bank_name}\n"
    f"Account Holder Name: {name}\n"
    f"Account numbere: {account_number}\n"
    f"Updated Balance: {balance}")
    

def enter_pin():
    count = 0
    while True:
        try:
            pin1 = input("Enter Pin: ")
            pin1 = int(pin1)
            if pin1 == pin:
                print("Welcome", name)
                return True
            else:
                # pin1 != pin - This line does nothing. Not deleting but keeping it as a ref for future , to look back.
                count += 1
                if count == 3:
                    print("Maximum Attempt Reached: Exiting simulation")
                    return False    # Will exit the function immediately after third failed attempt, returni
                else:
                    print("Wrong Pin: Try Again")   # Putting "Wrong Pin : try again" message here will not allow user to enter pin after the third time.                    
        except:
            print("Invali Input : Enter numbers only")
                    
 
# Menu gets printed immediately on execution.
print("Welcome to Bank of Bankrupts") #Funny Name LOL.


result = enter_pin() # Whether the enter_pin function returns True or False will be stored as a result here, which can be used with If function to run the rest of the ATM Simulator.
if result == True:

    print ("=================== ATM Menu =====================\n"
    "1. Withdraw                            2. Diposit\n"
    "3. Show Balance                        4. A/C info:\n"
    "                     5. Exit                        \n"
    "==================================================")

    #loop - post menu choice - Menu gets printed only once, not after every choice entered.
    try:
        while True:
            choice = input("Enter choice here: ")
            choice = int(choice)
            if choice == 1:
                withdraw_amt()
            
            elif choice == 2:
                deposit_amt ()

            elif choice == 3:
                show_balance()

            elif choice == 4:
                account_details()
            else:
                if choice == 5:
                    break
    except:
        print("Invalid Choice : Try Again")