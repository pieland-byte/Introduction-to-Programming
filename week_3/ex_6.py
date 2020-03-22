#This program tosses a virtual coin 100 times and analyzes the results
#showing long runs of heads or tails and how many instances of 3 same
#results in a row


import math
import asyncio
import random

#Function to count total amount of heads(Used only to verify toss results)
def head_count():
    head_count = 0
    for ind in result:
        if ind == 'H':
            head_count = head_count + 1
    return head_count

#Function to count total amount of tails(Used only to verify toss results)
def tail_count():
    tail_count = 0
    for ind in result:
        if ind == 'T':
            tail_count = tail_count + 1
    return tail_count

#Function to return the indices of result list which are heads
def head_index():
    head_index = []                     #Empty list
    for ind in range(len(result)):      #For every index in result
        if result[ind] == "H":          #If index is a head
            head_index.append(ind)      #Add the index to the list
    return head_index

#Function to return the indices of result list which are heads
def tail_index():
    tail_index = []                     #Empty list
    for ind in range(len(result)):      #For every index in result
        if result[ind] == "T":          #If index is a tail
            tail_index.append(ind)      #Add the index to the list
    return tail_index

result = []                             #Empty list
count = 0                               #Count times tossed
while count < 100:                      #Limit tosses to 100
    toss = random.randint(1,2)          #Pick a random 1 or 2
    if toss == 1:                       #If 1 add H to result list
        result.append('H')
    else:
        result.append('T')              #If 2 add T to result list
    count = count + 1                   #Count this toss
'''
Counting instances of triple heads - this process was decided upon to nullify
the program counting instances of 4 heads in a row as 2 instances of triple heads
counting both indexes of [0:2] as triple heads and then [1:4] as triple heads.
To do this it first finds the indexes of the head results, counts how many are
consecutive and then calculates how many triple heads to return
'''
counth = 0
trip_h = []
for ind in range(len(head_index()) - 1):                #Using the indexes of heads
    if head_index()[ind] +1 == head_index()[ind+1] :    #If the next index is consecutive
        counth += 1                                     #Add to the head count
    else:
        trip_h.append(counth)                           #If next index is not ahead
        counth = 1                                      #Add 1 to the count to show the head is single
trip_h.append(counth)                                   #Add count of 1 to show single head


triple_h = 0
for ind in trip_h:              #Using the counts of consecutive indexes above
    if 3 <= ind < 6:            #If the count is 3,4 or 5
        triple_h += 1           #Add 1 instance of triple heads to the list
    elif 6 <= ind < 9:          #If the count is 6,7 or 8
            triple_h += 2       #Add 2 instance of triple heads to the list
    elif 9 <= ind < 12:         #If the count is 9,10 or 11
            triple_h += 3       #Add 3 instance of triple heads to the list

            #Probability of getting more consecutive instances of heads is extremely
            #low so further elif statements were deemed to be unnecessary for example
            #upto 15 instances in a row would add 4 triples to the list and so on

#The following code is a copy of the above for counting instances of triple heads
# excepting that the result is for instances of triple tales - see above annotation            
count_t = 0
trip_t = []
for ind in range(len(tail_index()) - 1):
    if tail_index()[ind] +1 == tail_index()[ind+1]:
        count_t += 1
    else:
        trip_t.append(count_t)
        count_t = 1
trip_t.append(count_t)

triple_t = 0
for ind in trip_t:
    if 3 <= ind < 6:
        triple_t += 1
    elif 6 <= ind < 9:
            triple_t += 2
    elif 9 <= ind < 12:
            triple_t += 3

#Calculating the long runs of each
long_run_h = max(trip_h)    #Find max number in list of consecutive indexes for heads
long_run_t = max(trip_t)    #As above but for tails

print("",result[0:20],"\n",result[20:40],"\n",result[40:60],"\n",result[60:80],"\n",result[80:100])
print ("The longest run of heads is",long_run_h)
print ("The longest run of tails is",long_run_t)
print("There are",triple_h,"instances of triple heads.")
print("There are",triple_t, "instances of triple tails.")

#The below code are all redundant to the final code and were attempts at different
#solutions which didnt quite work out - I decided to keep them here to show
#other processes which were attempted



'''
def triple_h():
    trip_h_list = []
    for ind in result:
        if ind == "H" and ind+1 == "H" and ind+2 == "H":
            trip_h_list.append(ind)
            trip_h_list.append(ind+1)
            trip_h_list.append(ind+2)
    return len(trip_h_list)/3

def three_heads():
    tri_head = 0
    while len(result) > 3:
        if result[0:2] == "H, H, H":
            tri_head = tri_head+1
            result.remove[0:2]
    return tri_head


trip_h_list = []
for ind in result:
    if ind == "H" and ind+1 == "H" and ind+2 == "H":
        trip_h_list.append(ind)
        trip_h_list.append(ind+1)
        trip_h_list.append(ind+2)  
'''
'''

print(len(result))
print(head_count())
print(tail_count())
print(trip_h_list)

'''
'''
count_h = 0
count_t = 0

def long_run():
    count_h = 0
    count_t = 0
    for i in result:
        if i == "H":
            count_h += 1
        else:
            count_t += 1
        count_h = count_h
        count_t = count_t

        print("Head count : ", count_h)
        print("Tails count: ", count_t)

#def long_run_tails():

def triple_head(lst):
    print(result.count(["H", "H", "H"]))


print(coin_toss())
#triple_head(result)
#long_run()
#print("Head count : ", count_h)
#print("Tails count: ", count_t)
'''


