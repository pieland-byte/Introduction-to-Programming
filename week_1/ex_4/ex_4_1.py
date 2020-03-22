# This is my program to calculate the area of rooms
# in a house and the total area of the house

length_1 = input("Enter the length of room 1 in feet: ")
width_1 = input("Enter the width of room 1 in feet: ")

print("")

length_2 = input("Enter the length of room 2 in feet: ")
width_2 = input("Enter the width of room 2 in feet: ")

print("")

length_3 = input("Enter the length of room 3 in feet: ")
width_3 = input("Enter the width of room 3 in feet: ")

print("")

length_4 = input("Enter the length of room 4 in feet: ")
width_4 = input("Enter the width of room 4 in feet: ")

length_1 = int(length_1)
length_2 = int(length_2)
length_3 = int(length_3)
length_4 = int(length_4)

width_1 = int(width_1)
width_2 = int(width_2)
width_3 = int(width_3)
width_4 = int(width_4)

area_1 = (length_1 * width_1)
area_2 = (length_2 * width_2)
area_3 = (length_3 * width_3)
area_4 = (length_4 * width_4)

area_total = (area_1 + area_2 + area_3 + area_4)

print("")
print("")

print("This is the area of room 1: ", area_1, "square feet.")
print("This is the area of room 2: ", area_2, "square feet.")
print("This is the area of room 3: ", area_3, "square feet.")
print("This is the area of room 4: ", area_4, "square feet.")
print("This is the total area of the house: ", area_total, "square feet.")
