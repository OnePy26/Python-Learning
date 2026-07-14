# Simple beginner friendly To DO List code - Using Lists.
# Variables 
name  = "alan"
username1 = "alan24"
password1 = "alan42"

# list
task_list = [] #original list
#complete_task =[] # completed task's will be moved from last_list to this list for the show_complete function.

def add_task ():
    while True:
            task = input("Add task (N to main menu): ")
            if task.lower() == "n":
                break
            elif len(task) < 5:
                print("Task should be of at least 5 Characters|Try Again")
            task = task.capitalize().strip()
            task_list.append(task)
            

def replace_task ():
    while True:
            number_ = input("Add task number (N to main menu): ")
            if number_.lower() == "n":
                break
            number_= int(number_)
            new_task = input("Add New task (N to main menu): ")
            if new_task.lower() == "n":
                break
            task_list[number_] = new_task            


def remove_task ():
    pass


def mark_complete ():
    while True:
            number_ = input("Add task number (N to main menu): ")
            if task.lower() == "n":
                break
            number_.lower() = number_
            "[\u2713]" += task_list.index[number_]


def show_completed ():
    for i in task_list:
    if i startswith("[\u2731]")
        print(task_list.index(i), i.startswith("[\u2713]"))


def show_pending ():
    pass


def password ():
    count = 0
    while True:
        user1 = input("Username :")
        pass1 = input("Password :")
        if user1 == username1 and pass1 == password1:
            print("Welcome", name )
            return True
        else:
            count += 1
            if count == 3:
                print("Maximum attempt reached | User Locked")
                return False
            else:
                print ("Wrong Username/password: Try Again")

#Menu

result = password()

if result:

    print (f"==================Task Manager================ \n"
    f"1. Add task                   2. Remove Task \n"
    f"3. Mark Complete              4. Show Completed \n"
    f"                   5. Exit \n"
    f"============================================== \n")

#Choice
while True:
    try:
        choice = input("enter choice: ")
        choice = int(choice)
        if choice == 1:
            add_task()
        elif choice ==2:
            remove_task()
        elif choice == 3:
            mark_complete()
        elif choice == 4:
            show_completed()
        else:
            choice == 5
            break
    except:
        print("Invalid Choice | Try again")






# loop for Menu