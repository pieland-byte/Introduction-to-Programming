# This is a program to convert temperature in fahrenheit to celcius/centigrade

fahrenheit = input("Enter the temperature in fahrenheit: ")

fahrenheit = int(fahrenheit)

celsius = ((5/9) * (fahrenheit - 32))

print(fahrenheit, "Degrees Fahrenheit is",round(celsius,2), "degrees Celsius")
