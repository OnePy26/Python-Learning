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
                print("Task should be of at least 5 Characters|Try Again")
            tasks_new = tasks.split(",")
            for i in tasks_new:
                task_list.append(i.strip().title())


def remove_task ():
    pass            



def replace_task ():
    global task_list
    while True:
            number = input("Add task number (N to main menu): ")
            if number.lower() == "n":
                break
            number= int(number)
            new_task = input("Add New task (N to main menu): ")
            if new_task.lower() == "n":
                break
            task_list[number] = new_task            



def mark_complete ():
    while True:
        try:
            number = input("Add task number (N to main menu): ")
            if number.lower() == "n":
                break
            number = int.number
            "[\u2713]" + task_list.index[number]
        except:
            print("Invalid Input| Try Again")

def show_completed ():
    for i in task_list:
        if i.startswith("[\u2713]"):
            print(task_list.index(i), i)


def show_pending ():
    for i in task_list:
        if not i.startswith("[\u2713]"):
            print(task_list.index(i), i)


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
    f"3. Replace Task               4. Mark Complete \n"
    f"5. Show Completed               6. Show Pending \n"
    f"                     7.Exit                       \n"
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
        elif choice == 5:
            replace_task()
        else:
            choice == 6
            break
    except:
        print("Invalid Choice | Try again")






# loop for Menu