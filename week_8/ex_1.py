#This program 

import urllib.request
'''
url = "https://knockoutpest.com/wp-content/uploads/2014/06/honey-bee-close-up.jpg"
file_name = "./bee_pic.jpg"
urllib.request.urlretrieve(url, file_name)
'''


url = input("Enter the address of the file to download including the http:// prefix: ")

file_name = input("Enter the filepath where you would like to save the file: ")


urllib.request.urlretrieve(url, file_name)
