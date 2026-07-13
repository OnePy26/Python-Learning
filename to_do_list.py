# Simple beginner friendly To DO List code - Using Lists.
# Variables 
name  = "alan"
username = "alan24"
password = "alan42"

list
task_list = [] #original list
complete_task =[] # completed task's will be moved from last_list to this list for the show_complete function.

def add_task ():
    pass

def remove_task ():
    pass

def mark_complete ():
    pass

def show_complete ():
    pass

def show_pending ():
    pass

def password ():
    count = 0
    while True:
        user1 = input("Username :")
        pass1 = input("Password :")
        if user1 == username and pass1 == password:
            print("Welcome", name )
            return True
            if user1 != username or pass1 != password:
                count += 1
                if count == 3:
                    print("MAximum attempt reached | User Locked")
                    return False
                else:
                    print ("Wrong Username/password: Try Again")

#Menu

result = password()

if result == True:

    print (f"==================Task Manager================ \n"
    f"1. Add task                   2. Remove Task \n"
    f"3. Mark Complete              4. Show Complete \n"
    f"                   5. Exit \n"
    f"============================================== \n")

#Choice


# loop for Menu