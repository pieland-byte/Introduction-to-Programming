#This program will output a grade when a user inputs an amount of marks gained

marks = input("Enter your marks: ")




if (marks.isdigit()):
    marks = int(marks)
    if marks <0 or marks > 100:
        print("Please enter a valid number of marks.")
    elif marks == 0:
        print("Your grade is N/S")
    elif 1 <= marks <= 39:
        print("Your grade is F")
    elif 40 <= marks <= 49:
        print("Your grade is D")
    elif 50 <= marks <= 59:
        print("Your grade is C")
    elif 60 <= marks <= 69:
        print("Your grade is B")
    elif 70 <= marks <= 79:
        print("Your grade is A")
    elif 80 <= marks <= 100:
        print("Your grade is A*")
    
else:
    print("Please enter a valid number of marks.")
    
