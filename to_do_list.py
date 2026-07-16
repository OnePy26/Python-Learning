# Simple beginner friendly To DO List code - Using Lists.

#list of tasks (to save time) : wake up, go to gym, have food, go to office, take a bath, have lunch
# Variables 
name  = "alan"
username1 = "alan24"
password1 = "alan42"

# list
task_list = [] #original list
#complete_task =[] # completed task's will be moved from last_list to this list for the show_complete function. Not needed, found a better way to do it.

def add_task ():
    global task_list
    while True:
            tasks = input("Add tasks (Separate tasks by ',')\n"
            "('E' Exit to main menu) \n"
            "Input tasks: ")
            if tasks.lower() == "e":
                break
            elif len(tasks) <= 5:
                print(f"Task should be of at least 5 Characters|Try Again")
            tasks_new = tasks.split(",")
            for i in tasks_new:
                task_list.append(i.strip().title())


def remove_task ():
    global task_list
    while True:
            number = input("Add task number ('E' to main menu): ")
            if number.lower() == "e":
                break
            number= int(number) - 1
            task_list.pop(number)
                

def replace_task ():
    global task_list
    while True:
            number = input(f"Add task number ('E' to main menu): ")
            if number.lower() == "e":
                break
            number= int(number) - 1
            new_task = input(f"Add New task ('E' to main menu): ")
            if len(new_task) <= 5:
                print(f"Task should be of at least 5 Characters|Try Again")
            task_list[number] = new_task
                

def mark_complete ():
    while True:
        try:
            number = input(f"Add task number ('E' to main menu): ")
            if number.lower() == "e":
                break
            number = int(number) - 1
            task_list[number] = "[\u2713]" + task_list[number]
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


def password ():
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

result = password()

if result:

    print (f"==================Task Manager================ \n"
    f"1. Add task                   2. Remove Task \n"
    f"3. Replace Task               4. Mark Complete \n"
    f"5. Show Completed             6. Show Pending \n"
    f"7. Show All Tasks             8. Exit\n"
    f"============================================== \n")

#Choice

while True: # loop for Menu
    try:
        choice = input("enter choice: ")
        choice = int(choice)
        if choice == 1:
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

