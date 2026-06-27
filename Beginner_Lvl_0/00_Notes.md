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