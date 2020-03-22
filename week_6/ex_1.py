



x = int(input("Please enter a number: "))


y = int(input("Please enter a number: "))


choice = input("Please enter 1 to add, 2 to subtract, 3 to multiply or 4 to divide: ")

if choice == "1":
    print(x + y)
elif choice == "2":
    print((x-y))
elif choice == "3":
    print((x*y))
elif choice == "4":
    print((x/y))




while True:
    re_calculate = input("Would you like to input further numbers? Y/N: ")
    if re_calculate == "Y" or re_calculate == "y":
        x = int(input("Please enter a number(x): "))
        y = int(input("Please enter a number:(y) "))

        
        choice = input("Please enter 1 to add, 2 to subtract, 3 to multiply or 4 to divide: ")

        if choice == "1":
            print(x + y)
        elif choice == "2":
            print((x-y))
        elif choice == "3":
            print((x*y))
        elif choice == "4":
            print((x/y))
    elif re_calculate == "N" or re_calculate == "n":
        print("Goodbye.")
        exit()


