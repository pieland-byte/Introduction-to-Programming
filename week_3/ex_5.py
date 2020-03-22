#This program rolls 2 dice 100 times and records the frequency of scores

import random
import collections
import math

counter = 0
score = []


while counter < 100:                #loop for 100 times
    dice_1 = random.randint(1,6)    #rolls dice number 1
    dice_2 = random.randint(1,6)    #rolls dice number 2
    score.append(dice_1 + dice_2)   #adds die score to score list
    counter += 1                    #counts number of rolls
    score.sort()                    #sorts resulting score

'''
def rolls():
    for n in score.count(n):
        print(("*" *n))
'''



#Counts and prints frequency of scores and represents this as a table of *

print("Distribution Chart")
print("Score     ", "Rolls")
print("2         ",score.count(2), str("*" * score.count(2)).ljust(30))
print("3         ",score.count(3), str("*" * score.count(3)).ljust(30))
print("4         ",score.count(4), str("*" * score.count(4)).ljust(30))
print("5         ",score.count(5), str("*" * score.count(5)).ljust(30))
print("6         ",score.count(6), str("*" * score.count(6)).ljust(30))
print("7         ",score.count(7), str("*" * score.count(7)).ljust(30))
print("8         ",score.count(8), str("*" * score.count(8)).ljust(30))
print("9         ",score.count(9), str("*" * score.count(9)).ljust(30))
print("10        ",score.count(10), str("*" * score.count(10)).ljust(30))
print("11        ",score.count(11), str("*" * score.count(11)).ljust(30))
print("12        ",score.count(12), str("*" * score.count(12)).ljust(30))


