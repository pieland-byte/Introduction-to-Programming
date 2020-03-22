#This program compares two numbers and displays
#which of the two is larger and keeps asking until "quit" is entered

while True:

    num_1 = (input("Enter the first number: "))


    if num_1 == "quit" or num_1 == "Quit":
        print("Goodbye")
        break
    elif (num_1.isdigit()):
        num_1 = int(num_1)
        num_2 = int(input("Enter the second number: "))
        if num_1 == num_2:
            print("Numbers are equal")
        elif num_1 > num_2:
            print("Number one is larger")
        else :
            print("Number two is larger")

