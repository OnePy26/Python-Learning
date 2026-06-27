names = []

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
        name = str(input("Enter Student Name: "))
        names.append (name)
    elif option == "2":
        name = str(input("Enter Student Name: "))
        names.remove (name)
    elif option == "3":
        if len(names) == 0:
            print("No records to display")
        else:
            for n in names:
                print (names.index(n), n)
    elif option == "4":
        num = int(input("Enter Record Number: "))
        name1 = str(input("Enter New Student Name: "))
        names[num] = name1
    elif option == "5":
        break
    else:
        print("Invalid Option:Try Again")