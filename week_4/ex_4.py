#This program writes individual files containing each cars information

#create a list from the text file
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

#Function using the car dictionary to create file names based on the cars information
def car_fname(car):
    return car["make"] + "_" + car["model"] + "_" + car["year"] + ".txt"
#Function to write the files
for car in cars:                                #For each instance in cars
    with open(car_fname(car), "w") as car_f:    #Open a text file in write mode using car_fname function to name the file
        car_f.write(car["make"] + "\n")         #Write car make to file
        car_f.write(car["model"] + "\n")        #Write car model to file
        car_f.write(car["year"] + "\n")         #Write car year to file
