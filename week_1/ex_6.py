#This is a program to convert temperature from celsius to fahrenheit

celsius = input("Enter the temperature in degrees celsius: ")

celsius = int(celsius)

fahrenheit = ((9/5) * celsius + 32)

print (celsius, "degrees celsius is ", round(fahrenheit,1), "degrees fahrenheit")
