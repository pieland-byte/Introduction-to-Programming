# This program is for checking whether a webpage contains information on Bees
# and prints suitable message.
''' Tested on webpages:
http://www.teesbees.co.uk/ - returned positive
https://www.bumblebeeconservation.org/about-bees/ - returned positive
https://www.ford.co.uk/ - returned negative
https://en.wikipedia.org/wiki/Badminton - returned negative

'''
import urllib.request
import time

url = input("Enter the address of a web page for scanning:")

response = urllib.request.urlopen(url)          #Open the url of the webpage
data = response.read()                          #Read the contents of the page
text = data.decode("utf-8")                     #Decode the page into text

 
blocked_words = []                              #Empty list for blocked words




with open ("blocked_words.txt", "r") as bee:    #Open the file containing blocked words in read mode
    for line in bee:                            #Use each line in the blocked words text file
        blocked_words.append(line.rstrip("\n")) #Add each line to the blocked words list


bee_site = []                                   #Create an empty list


for line in blocked_words:                      #Using the blocked words list
    if line in text:                            #If the blocked word is in the list(bee_site)
        bee_site = True                         #Return True
        break                                   #End loop
    
#If webpage contains information about bees
if bee_site == True:
    print("This website contains BEES!!!!!!You are not allowed to view!")

#If there is not information about bees
else:
    print("This website DOES NOT contain BEES!!!!!!You are allowed to view!")

time.sleep(5)  #For running outside the Repl this gives the user time to read the programs response
