#This is a program to calculate if a number is divisible by 3 or 5 or both

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("Fizz Buzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)
