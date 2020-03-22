#This program takes all of the individual code from the cars
#database exercises combined together.
#See individual code files for annotation


def car_list():
    car_list = []
    with open ("cars_exercise_3.txt" , "r") as car_data:
        for line in car_data:
            car_list.append(line.rstrip("\n"))
        return car_list


def car_dict():
    i = 0
    car_dict = []
    car_1 = car_list()
    while i <len(car_1):
        car_dict.append({"make" : car_1[i], "model" : car_1[i + 1], "year" : car_1[i + 2]})
        i += 3
    return car_dict



def newest():
    newest = max(car_dict(), key=lambda x: x["year"])
    return newest

def oldest():
    oldest = min(car_dict(), key=lambda x: x["year"])
    return oldest

cars = car_dict()

def car_fname(car):
    return car["make"] + "_" + car["model"] + "_" + car["year"] + ".txt"

for car in cars:
    with open(car_fname(car), "w") as car_f:
        car_f.write(car["make"] + "\n")
        car_f.write(car["model"] + "\n")
        car_f.write(car["year"] + "\n")

        
def write_no_year():
    with open ("cars_no_years.txt", "w") as car_file:
        for car in car_dict():
            car_file.write(car["make"] + "\n")
            car_file.write(car["model"] + "\n")

def prepend_year():
    with open ("cars_prepend.txt", "w") as car_y:
        for cars in car_dict():
            car_y.write(cars["make"] + "\n")
            car_y.write(cars["year"] + " " + cars["model"] + "\n")
        
        

#print(car_dict())
print("The newest car is: ", newest())
print("The oldest car is: ", oldest())



write_no_year()
prepend_year()
