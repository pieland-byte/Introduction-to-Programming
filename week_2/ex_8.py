#This program calculates the sum of numbers at even indices from a given list
import math

nums = [14,5,19,20,21,66,89]

current = 0
total = 0

while current < len(nums):
    if current % 2 == 0: 
        print(nums[current])
        total = total + nums[current]

    current += 1

print(total)
