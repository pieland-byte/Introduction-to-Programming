#This program uses a defined function to quickly calculate the volume of shapes 

import math

#calculate volume of sphere with radius r
def sphere(r):
    return "volume of sphere is",(math.pi *(r **3))* (4/3)

#calculate volume of cylinder with radius r and height h
def cylinder(r,h):
    return "volume of cylinder is",(math.pi * r**2) * h

#calculate volume of cone with radius r and height h
def cone(r,h):
    return "volume of cone is",((math.pi * r**2) * h)* (1/3)

'''
# these are just testing the functions
print("Volume of sphere is",sphere(3))
print("Volume of cylinder is",cylinder(3,3))
print("Volume of cone is",cone(3,3))

r = int(input("input radius"))
h = int(input("input height"))

print(sphere(r))
print(cylinder(r,h))
print(cone(r,h))
'''
