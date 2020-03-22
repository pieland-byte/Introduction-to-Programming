#This program calculates the area and circumference of a circle when
#the radius is entered

import math

circle_radius = input("Enter the radius of the circle: ")

circle_radius = int(circle_radius)

print("")

circle_area = (circle_radius * circle_radius) * math.pi

print("The area of the circle is approx",round(circle_area,2))

circle_circumference = (2 * math.pi) * circle_radius

print("")

print("The circumference of the circle is spprox",round(circle_circumference,2))
