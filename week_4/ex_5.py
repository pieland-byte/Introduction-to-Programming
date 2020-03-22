#This program takes data from an original text file and writes a new file
#with some of the information omitted


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

#Function to write the car information to file omitting the data in the key "year
def write_no_year():
    with open ("cars_no_years.txt", "w") as car_file:   #Open a text file in write mode
        for car in car_dict():                          #For each dictionary entry
            car_file.write(car["make"] + "\n")          #Write the car make
            car_file.write(car["model"] + "\n")         #Write the car model

#write_no_year()
