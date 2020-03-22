# This is my program to calculate the volume of rooms
# in a house and the total volume of the house

length_1 = input("Enter the length of room 1 in feet: ")
width_1 = input("Enter the width of room 1 in feet: ")
height_1 = input("Enter the height of room 1 in feet: ")

print("")

length_2 = input("Enter the length of room 2 in feet: ")
width_2 = input("Enter the width of room 2 in feet: ")
height_2 = input("Enter the height of room 2 in feet: ")

print("")

length_3 = input("Enter the length of room 3 in feet: ")
width_3 = input("Enter the width of room 3 in feet: ")
height_3 = input("Enter the height of room  in feet3: ")

print("")

length_4 = input("Enter the length of room 4 in feet: ")
width_4 = input("Enter the width of room 4 in feet: ")
height_4 = input("Enter the height of room 4 in feet: ")

length_1 = int(length_1)
length_2 = int(length_2)
length_3 = int(length_3)
length_4 = int(length_4)

width_1 = int(width_1)
width_2 = int(width_2)
width_3 = int(width_3)
width_4 = int(width_4)

height_1 = int(height_1)
height_2 = int(height_2)
height_3 = int(height_3)
height_4 = int(height_4)

area_1 = (length_1 * width_1)
area_2 = (length_2 * width_2)
area_3 = (length_3 * width_3)
area_4 = (length_4 * width_4)

area_total = (area_1 + area_2 + area_3 + area_4)

volume_1 = (area_1 * height_1)
volume_2 = (area_2 * height_2)
volume_3 = (area_3 * height_3)
volume_4 = (area_4 * height_4)

volume_total = (volume_1 + volume_2 + volume_3 + volume_4)

print("")
print("")

print("This is the volume of room 1: ", volume_1, "cubic feet.")
print("This is the volume of room 2: ", volume_2, "cubic feet.")
print("This is the volume of room 3: ", volume_3, "cubic feet.")
print("This is the volume of room 4: ", volume_4, "cubic feet.")
print("This is the total volume of the house: ", volume_total, "cubic feet.")
