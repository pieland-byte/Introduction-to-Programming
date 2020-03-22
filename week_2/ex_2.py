# This program determines if a person is eligible to vote after asking
# their relevent data

name = input("Enter your name: ")
age = input("Enter your age: ")
country = input("Enter your country of citizenship: ")

age = int(age)


if age < 18:
    print(name,"Sorry you are not yet old enough to vote.")

elif age >= 18 and (country == "Britain" or country == "Great Britain" or country == "UK" or country == "uk"):
    print (name,"You are eligible to vote")

elif (country != "Britain" or country != "Great Britain" or country != "UK" or country != "uk"):
    print(name,"Sorry you are not eligible to vote")
 


    
