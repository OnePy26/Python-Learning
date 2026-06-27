names = []

def add_name():
    name = str(input("Enter Student Name: "))
    names.append (name)

def remove_name():
    name = str(input("Enter Student Name: "))
    names.remove (name)

def show_name():
    if len(names) == 0:
        print("No records to display")
    else:
        for n in names:
            print (names.index(n), n)
def update_name():
    num = int(input("Enter Record Number: "))
    name1 = str(input("Enter New Student Name: "))
    names[num] = name1


print(
    "===============*Student Record Manager*================ \n"
    "1 Add Student:\n"
    "2 Remove Student:\n"
    "3 Show Student List:\n"
    "4 Update Student:\n"
    "5 Exit:\n"
    "========================================================\n")
while True:
    option = str(input("Enter input: "))
    if  option == "1":
        add_name()
    elif option == "2":
        remove_name()
    elif option == "3":
        show_name()
    elif option == "4":
        update_name()
    elif option == "5":
        break
    else:
        print("Invalid Option:Try Again")