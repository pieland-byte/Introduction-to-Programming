# A program for an inventory in an adventure game
from random import *

rucksack = ["Water flask", "Cheese", "Gold coins", "Handkerchief", "Tinderbox", "Scrolls", "Dagger", "Rope", "Nuts", "Pipe", "Tobacco", "Wine skin", "Herbs", "Axe"]
chest = ["Gems", "Necklace"]
theft = sample(rucksack, 5)

#Sort rucksack alphabetically
rucksack.sort()

#Prints contents of rucksack
print("Contents of rucksack: ", rucksack)

print('\n')

#Prints number of items in rucksack
print("Number of items in rucksack: ", len(rucksack))

#Adds chest items to rucksack
rucksack = (chest + rucksack)

print('\n')

#Prints items found in chest
print("In the chest you found: ", chest)

#Sorts rucksack with added chest items
rucksack.sort()

print('\n')

#Prints contents with new items added
print("Contents of rucksack after chest", rucksack)

print('\n')

#Prints theft message and items stolen
print("THEIF!! The following items were stolen!: ", theft)

#Removes stolen items from rucksack
for i in theft:
    rucksack.remove(i)

print('\n')

#Prints updated contents of rucksack
print("new contents of rucksack", rucksack)
