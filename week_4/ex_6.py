#This program takes the information from the original text file and
#creates a file where the information is moved to a new position


#Create a list from the text file
def car_list():
    car_list = []
    with open ("cars_exercise_3.txt" , "r") as car_data:
        for line in car_data:
            car_list.append(line.rstrip("\n"))
        return car_list

#Create a dictionary of the car information giving the keys as "make", "model" and "year"

def car_dict():
    i = 0
    car_dict = []
    car_1 = car_list()
    while i <len(car_1):
        car_dict.append({"make" : car_1[i], "model" : car_1[i + 1], "year" : car_1[i + 2]})
        i += 3
    return car_dict

cars = car_dict()

#Function to write the car information in a new order swapping the model and the year from the original data
def prepend_year():
    with open ("cars_prepend.txt", "w") as car_y:                   #Open a text file in write mode
        for cars in car_dict():                                     #For the cars in the dictionary                
            car_y.write(cars["make"] + "\n")                        #Write the make of the car
            car_y.write(cars["year"] + " " + cars["model"] + "\n")  #Write the year and then the model
        
#prepend_year()
