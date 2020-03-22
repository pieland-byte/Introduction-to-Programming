#This program calculates the volume of a cylinder when the
#radius of a face and height is entered

import math

cylinder_radius = input("Enter the radius of the cylinder: ")
cylinder_radius = int(cylinder_radius)

cylinder_height = input("Enter the height of the cylinder: ")
cylinder_height = int(cylinder_height)

cylinder_volume = (math.pi * cylinder_radius**2 ) * cylinder_height

print("")

print("The volume of the cylinder is approx: ",round(cylinder_volume,2))
