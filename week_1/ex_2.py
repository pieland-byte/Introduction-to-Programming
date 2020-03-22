import math

radius_v = input("Type the length of the vertical radius: ")
radius_h = input("Type the length of the horizontal radius: ")

radius_v = int(radius_v)
radius_h = int(radius_h)

area_ellipse = (math.pi * radius_v * radius_h)

print("This is the area of the ellipse", area_ellipse)

