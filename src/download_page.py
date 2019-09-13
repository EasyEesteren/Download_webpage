#!/usr/bin/env python3
import requests, sys

#If command line input is given it is used as the search term, else the user is prompted for input.
if (len(sys.argv) > 1):
	command = "".join(sys.argv[1:])
else:
	command = input("Please enter webpage url to be downloaded: ")
result = input("Please enter the name of the file you wish the page to be saved in: ")
print ("Dowloading....")

res = requests.get(command)
res.raise_for_status()

exampleFile = open(result + ".txt", 'wb')
for chunk in res.iter_content(100000):
	exampleFile.write(chunk)
exampleFile.close()