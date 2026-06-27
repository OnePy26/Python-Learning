while True:
    option = str(input("choose student database option \n"
    "1 Add Student:\n"
    "2 Remove Student:\n"
    "3 Show Student List:\n"
    "4 Update Student:\n"
    "5 Exit:\n"
    "Enter Oprion: "))
    
    if  option == "1":
        name = str(input("Enter Student Name: "))
        names.append (name)
    elif option == "2":
        name = str(input("Enter Student Name: "))
        names.remove (name)
    elif option == "3":
        for n in names:
            print (name.index, n)
    elif option == "4":
        num = int(input("Enter Record Number: "))
        name1 = str(input("Enter New Student Name: "))
        names[num] = name1
    else:
        Print("Invalid Option: Try Again")