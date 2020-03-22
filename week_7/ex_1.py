#This program is my first experiment with oop
#I got a bit confused so just started playing around a little.



class Greeter:
    name = ""
    def __init__(self, name,age, gender, pet):
        self.name = name
        self.age = age
        self.gender = gender
        self.pet = pet
        
    def greet_to_screen(self):
        print("Hello", self.name)
        
    def age_appropriate(self):
        if 20 < self.age <= 40:
            print("Hi",self.name,"you can join")
        elif self.age < 20:
            print("Arent you a bit young for this kind of holiday",self.name,"?")
        else:
            print("Why dont you try a saga holiday",self.name,"?")

    def animal_lover(self):
        pet_list = []
        with open ("animals.txt","r")as pets:
            for line in pets:
                pet_list.append(line.rstrip("\n"))
        if self.pet in pet_list:
            print("Oh so you have a",self.pet,self.name)
        
    #Think I was trying to make this too simple        
    def greet_to_file(self, filename):
        with open ("Hi.txt","w")as hi:
            hi.write(greet_to_screen())



greeter = Greeter("Fred", 35, "Male", "Cat")
greeter2 = Greeter("Steph", 30, "Female", "Dog")
greeter3 = Greeter("Hank", 60, "Male", "None")
greeter4 = Greeter("Tracy", 18, "Female", "Hamster")
greeter.greet_to_screen()
greeter2.greet_to_screen()
greeter3.greet_to_screen()
greeter4.greet_to_screen()
greeter.age_appropriate()
greeter2.age_appropriate()
greeter3.age_appropriate()
greeter4.age_appropriate()
greeter.animal_lover()
greeter2.animal_lover()
greeter3.animal_lover()
greeter4.animal_lover()
