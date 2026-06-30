
# First program: Mini Challenge 1
def square_num():
    number = int(input("Enter Number: "))
    return number * number
    
result = square_num()
print (result)


#Second Program: Mini Challenge 2
def is_even():
    number = int(input("Enter Number: "))
    if number % 2:
        return "False"
    else:
        return "True"
result = is_even()
print (result)