#import os
#print(os.getcwd)   #this is to display my current path
try:
    myinput = input("Please enter filename:")
    stream = open(myinput,"rt")
    print(stream.read())
except FileNotFoundError:
    print("File is not found")
