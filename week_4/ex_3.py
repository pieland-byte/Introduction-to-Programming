#This program creates a dictionary from a text file of cars and prints the
#oldest and newest car from the original file

#create a list from the text file
def car_list():
    car_list = []                                           #Empty list
    with open ("cars_exercise_3.txt" , "r") as car_data:    #Open text file in read mode
        for line in car_data:                               #With every line in text file
            car_list.append(line.rstrip("\n"))              #Append line to car_list
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


#Return the newest car
def newest():
    newest = max(car_dict(), key=lambda x: x["year"])   #Find the car with the highest value in key "year"
    return newest                                       

def oldest():
    oldest = min(car_dict(), key=lambda x: x["year"])   #Find the car with the lowest value in key "year"
    return oldest

print("The newest car is: ", newest())
print("The oldest car is: ", oldest())
