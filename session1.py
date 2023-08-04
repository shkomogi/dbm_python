#var1 = "Monday"
#print(var1)

#len function
#print(len(var1))

#concatenation 
str1 = "a"
str2 = "b"
print(str1 + str2)

print(str1 * 3)
print("b" * 3)

#Q1 for exercise 1.1
fname = "Shirley"
sname = "Komogi"
print(fname +" " +sname)
print(fname * 3)

string1 = 'silly walks'
for character in string1:
    print(character,end=" ")
print()

#slicing
string2 = "abdefg"
print(string2[3:-2])

#index method
print('aAbByYzZaA'.index('B'))  #index for B is 3

#append char h to existing string2
sting2 = string2 + "h"
print(sting2)

#capitalize method using sting2 
print(sting2.capitalize())

#homework - use center method to include 5 spaces
print('['+sting2.center(5)+']')

#check if string 2 ends with h , H
print(sting2.endswith('h'))
print(sting2.endswith('H'))  #case sensitive

#Find method
print(sting2.find('EF'))
print(sting2.find('ef'))
