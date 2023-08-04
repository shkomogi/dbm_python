#reading a file
#put input inside try because user might type in wrong name file, or file name without file extension
from logging import exception


#try:
 #   userinput = input("Type file name + extension: ")
  #  stream = open(userinput,"rt")
   # print(stream.read())  #read - method
#except FileNotFoundError:
 #   print("File not found: 1. Check spelling 2. Add file extension")

 #CREATE A FILE
f = open("Session 4.txt","w")   #create a new file named Session 4

#WRITE TO FILE
f.write("Topic: Read and write to a file.")   #write some texts in it
f.close()   #close method

#READ FILE
my_file = open("Session 4.txt","rt")   #open file to read
print(my_file.read())     #output

#APPEND TO EXISTING FILE
f = open("Session 4.txt","a")
f.write(" More on Python")
f.close

#READ UPDATED FILE
updated_file = open("Session 4.txt","rt")
print(updated_file.read())




