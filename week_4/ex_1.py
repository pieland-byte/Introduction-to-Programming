#This program asks the user to name a sandwich and shows corresponding
#sandwiches from the menu


sandwiches = []

with open ("menu.txt","r") as menu:
    for line in menu:
        sandwiches.append(line.rstrip("\n"))

def sandwich_choice():
    choice = input("Enter which sarnie you would like: ")
    for ind in sandwiches:
        if choice in sandwiches:
            print("We have",choice,"available")
            break
        else:
            print("That is unavailable, sorry.")
            break
sandwich_choice()
