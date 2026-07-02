NB: Local and Global Variables: 
----------------------------------------
Python treats variables differently depending on where they are:
Inside a function → local variable
Outside → global variable

so in this example - 
-----------------------------------------
x = 10 # 10 is the global varible

def test():
    x = 5 # here 5 this is the local variable
    print("Inside:", x)

test()
print("Outside:", x)
------------------------------------------
They are basically two separate “copies” unless you explicitly connect them.

===================================================================================

NB: Indexing and Slicing in String, Lists :

| Type     | Example     | Meaning         |
| -------- | ----------- | --------------- |
| Indexing | `name[0]`   | One item        |
| Indexing | `name[-1]`  | One item (last) |
| Slicing  | `name[0:3]` | Multiple items  |
| Slicing  | `name[:-1]` | Multiple items  |

[ ] = one thing
[:] = a range of things

=====================================================================================

append add to the existing list []
 + [] creates a new list

 If you want next level, I can now show you:

⚡ “Why modifying lists inside functions can secretly change your original data”

That’s the next real Python trap.

names = []

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


Today's New Concept: Function Parameters

So far you've written:

def square_num():
    number = int(input("Enter Number: "))
    return number * number

It works.

But now let's make the function more flexible.

Instead of asking for input inside the function, pass the value to it.

def square_num(number):
    return number * number

num = int(input("Enter Number: "))
print(square_num(num))



names = []

def add_name():
    name = input("Enter name (0 for Main Menu): ")

    if name == "0":
        return False      # Tell the caller to stop

    names.append(name)
    return True           # Tell the caller to continue


def remove_name():
    name = input("Enter name: ")
    names.remove(name)


def show_name():
    for i, n in enumerate(names):
        print(i, n)


def update_name():
    num = int(input("Enter record Number: "))
    name1 = input("Enter new Name: ")
    names[num] = name1


print(
"===============Student Record Manager=================\n"
"1 to Add Student                   2 to Remove Student\n"
"3 to Show Student List             4 to Update Student Name\n"
"                       5 to Exit \n"
"======================================================"
)

while True:
    choice = int(input("Enter choice here: "))

    if choice == 1:
        while True:
            if not add_name():
                break

    elif choice == 2: