text = "apple,banana,mango"
fruits_list = text.split(",")

for i in fruits_list:
    print(fruits_list.index(i), i)
    
fruit = input("Enter Fruits Name: ")
fruits_list1 = fruit.split(",")
for i in fruits_list1:
    fruits_list.append(i)

for i in fruits_list:
    print(fruits_list.index(i), i)
    
eaten_fruit = input("Enter eaten fruit Name: ")
fruits_list.append("[\u2713]"+ eaten_fruit)
 
for i in fruits_list:
    print(fruits_list.index(i), i.title())
    
for i in fruits_list:
    if i.startswith(["\u2713"]):
        print(fruits_list.index(i), i.title())