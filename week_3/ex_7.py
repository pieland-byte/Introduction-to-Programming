#This program creates an ouput of numbers and then manipulates this list
#and prints the results

import random

#Creates a list of 20 random numbers between 0 and 99
num_list = []
for i in range(0,20):
    num = random.randint(1,99)
    num_list.append(num)
print("First List")
print(num_list)

#Sorts the list of numbers
num_list.sort() 

print()

#Prints second smallest number and second largest number using indexes of sorted list
print("Second smallest number is:", num_list[1],"Second largest number is",num_list[-2])

print()

#Prints number list with numbers after third highest number omitted
print("This is the list minus the numbers higher than the third highest number:")
print(num_list[0:-2])

print()
print()

#Creates second number list
sec_num_list = []
for i in range (0,20):
    num = random.randint(1,99)
    sec_num_list.append(num)

print("Second List")
print(sec_num_list)

print()
print()

#Inserts the number 50 at index 10(half way point)
sec_num_list.insert(10, 50)
print("This is the list with the number 50 inserted into the middle:")
print(sec_num_list)

#Finds numbers larger than 50 in the list and appends them to the end
for ind in sec_num_list[0:10]:      #in the first half of the list
    if ind > 50:                    #if the number is larger than 50
        sec_num_list.append(ind)    #add the number to the end of the list
        sec_num_list.remove(ind)    #remove the number from original position
print()
print()
print("This is the list with numbers larger than 50 moved:")
print(sec_num_list)

#Finds the index of the number 50
def index_50():
    return sec_num_list.index(50)

''' There are potential problems using the index_50() function if the original
list contains the number 50 before inserting at the midpoint.
This could be remedied by removing the original 50 before inserting the 50 at
index 10 and replacing with a random number using the following

for ind in sec_num_list:
    if ind == 50:
        sec_num_list.append(random.randint(1,99))
        sec_num_list.remove(ind)

However the integrity of the original sec_num_list would be questionable by
altering in this way.  Also there is also a chance that the new number that
has been appended will be the number 50 - this possibility could be mitigated
using a while loop to continually replace the number 50 but original list
integrity would be further comprimised.
'''

print()
print()
low_50 = []

#Finds numbers lower than 50 in the list and places them in low_50 list
for ind in sec_num_list[sec_num_list.index(50):22]:         #in list after the index with value 50
    if ind < 50:                                            #if number is lower than 50
        low_50.append(ind)                                  #append to low_50 list
        sec_num_list.remove(ind)                            #remove the number from original position

#Inserts removed numbers back into list at correct position
for ind in low_50:                          #in low_50 list
    sec_num_list.insert(index_50(), ind)    #insert number into second number list at index of value 50

#Print list
print("This is the list with numbers lower than 50 moved: ")
print(sec_num_list)


