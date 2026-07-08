#student record manager - This should be the final one at beginner level. Later we can build a one with file haldling ... maybe later :)

names = []

def add_name ():
    name = input("Enter Name 0 for main Menu: ")
    if  name == "0":
        return False
    names.append(name)
    return True

def show_names():
    pass


def remove_name():
    pass


def update_name():
    pass


def rec_num():
    pass


print("Student Record Manager ============== \n"
"1. To enter new name \n"
"2. To show student names \n"
"3. To enter new name \n"
"4. To enter new name \n"
"5. To enter new name \n"
"========================================")
while True:
    choice = input("Enter choice here: ")

    if  choice == "1":
        while True:
            if not add_name():
                break

    elif  choice == "2":
        pass

    elif  choice == "3":
        pass

    elif  choice == "4":
        pass

    elif  choice == "5":
        pass

    else:
        pass