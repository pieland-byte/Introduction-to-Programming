#This program calculates the volume of given shapes specified by
#the user using recursion

import math

# creating a menu with options for user input
def main_menu():
    menu_choice = input("Please type 1 for sphere, 2 for cylinder and 3 for cone: ")
    if menu_choice == "1":
        result = sphere(int(input("Enter radius of sphere ")))
        print("volume of sphere is", result)
    
    elif menu_choice == "2":
        radius = int(input("Enter radius: "))
        height = int(input("Enter height: " ))
        
        result = cylinder(radius, height)
        print("Volume of cylinder is ", result)
    
    
    elif menu_choice == "3":
        radius = int(input("Enter radius: "))
        height = int(input("Enter height: " ))
        result = cone(radius,height)
        print("volume of cone is", result)
        
    else:
        print("input error")
        main_menu()
    
# function to calculate volume of sphere radius r
def sphere(r):
    return (math.pi *(r **3))* (4/3)

#function to calculate volume of cylinder with radius r and height h
def cylinder(r,h):
    return (math.pi * r**2) * h

# function to calculate volume of cone with radius r and height h
def cone(r,h):
    return ((math.pi * r**2) * h)* (1/3)


    
main_menu()
