#This program compares two numbers and displays
#which of the two is larger

num_1 = int (input("Enter the first number: "))
num_2 = int (input("Enter the second number: "))

if num_1 == num_2:
    print("Numbers are equal")
elif num_1 > num_2:
    print("Number one is larger")
else :
    print("Number two is larger")
