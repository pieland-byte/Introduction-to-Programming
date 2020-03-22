#This program asks the user to name a sandwich ingredient and shows
#corresponding sandwiches from the menu


sandwiches = []                 #Empty list

with open ("menu.txt","r") as menu:             #Read menu.txt
    for line in menu:                           #For each line
        sandwiches.append(line.rstrip("\n"))    #Add line to sandwiches list without newline

def sand_choice():
    choice = input("Enter which sarnie you would like: ")   #User input choice
    choice = choice.title()                                 #Convert input to title case
    if len(choice) < 3:                                     #To prevent input of string with 1 or 2 characters or spaces from returning a valid result
        print("Please enter a valid choice")
        sand_choice()
    else:
        for n in sandwiches:                                    #Look through sandwich list
            if choice in n:                                     #If user input matches substring in string list sandwiches
                print("We have",n,"available")                  #Print multiple response

sand_choice()






            

