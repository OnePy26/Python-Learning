# Simple beginner friendly To DO List code - Using Lists.

#symbols: UPPER case denotes constants, values that should not be changed. 
CHECK = "\u2713"
CROSS = "\u2717"
WARNING = "\u26A0"
STAR = "\u2605"
#This is not enforced in Python, it can be changed. This acts as a reminder that these values are better kept unchanged.

#list of tasks (to save time) : wake up, go to gym, have food, go to office, take a bath, have lunch
# Variables 
name  = "alan"
username1 = "alan24"
password1 = "alan42"

# list
task_list = [] #original list
#complete_task =[] # completed task's will be moved from last_list to this list for the show_complete function. Not needed, found a better way to do it.

def add_task ():
    #global task_list - This is not needed. since the Global task_list will be referred to anyways.
    while True:
            tasks = input("Add tasks (Separate tasks by ',')\n"
            "('E' Exit to main menu) \n"
            "Input tasks: ")
            if tasks.lower().strip() == "e":
                break
            elif len(tasks.strip()) <= 5:
                print(f"Task Cannot be blank | Task should be of at least 5 Characters|Try Again")
                continue
            tasks_new = tasks.split(",")
            for i in tasks_new:
                task_list.append(i.strip().title())


def remove_task ():
    #global task_list - This is not needed. since the Global task_list will be referred to anyways.
    while True:
            number = input("Add task number ('E' to main menu): ")
            if number.lower() == "e":
                break
            number = int(number)
            if number <=0 or number > len(task_list):
                print(f"Invalid task number, number should be between 1 and {len(task_list)}")
                continue
            number -= 1
            task_list.pop(number)
                

def replace_task ():
    #global task_list - This is not needed. since the Global task_list will be referred to anyways.
    while True:
            number = input(f"Add task number ('E' to main menu): ")
            if number.lower() == "e":
                break
            number = int(number)
            if number <=0 or number > len(task_list):
                print(f"Invalid task number, number should be between 1 and {len(task_list)}")
                continue
            new_task = input(f"Add New task ('E' to main menu): ")
            if len(new_task.strip()) <= 5:
                print(f"Task should be of at least 5 Characters|Try Again")
                continue
            task_list[number] = new_task.strip().title()
                

def mark_complete ():
    while True:
        try:
            number = input(f"Add task number ('E' to main menu): ")
            if number.lower() == "e":
                break
            number = int(number) - 1
            task_list[number] = "[\u2713] " + task_list[number]
        except:
            print(f"Invalid Input| Try Again")


def show_completed ():
    for i in task_list:
        if i.startswith("[\u2713]"):
            print(task_list.index(i) + 1, i)


def show_pending ():
    for i in task_list:
        if not i.startswith("[\u2713]"):
            print(task_list.index(i) + 1, i.title())


def show_all_tasks ():
    if len(task_list) == 0:
        print(f"No Tasks Found | Add Tasks First")
    for i in task_list:
        print(task_list.index(i) + 1, i.title())


def login ():
    count = 0
    while True:
        user1 = input("Username :")
        pass1 = input("Password :")
        if user1 == username1 and pass1 == password1:
            print(f"Welcome {name.title()}")
            return True
        else:
            count += 1
            if count == 3:
                print(f"Maximum attempt reached | User Locked")
                return False
            else:
                print (f"Wrong Username/Password: Try Again")

#Menu

result = login()

if result:
    while True: # loop for Menu

        print (f"==================Task Manager================ \n"
        f"1. Add task                   2. Remove Task \n"
        f"3. Replace Task               4. Mark Complete \n"
        f"5. Show Completed             6. Show Pending \n"
        f"7. Show All Tasks             8. Exit\n"
        f"============================================== \n")

    #Choice

        try:
            choice = input("Enter choice: ")
            choice = int(choice)
            if choice > 8 or choice <= 0:
                print("Choice option does not exist | please enter choice from 1 to 8.")
                continue
            elif choice == 1:
                add_task()
            elif choice ==2:
                remove_task()
            elif choice == 3:
                replace_task()
            elif choice == 4:
                mark_complete()
            elif choice == 5:
                show_completed()
            elif choice == 6:
                show_pending()
            elif choice == 7:
                show_all_tasks()
            elif choice == 8:
                break
        except:
            print("Invalid Choice | Try again")

