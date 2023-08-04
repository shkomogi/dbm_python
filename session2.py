#Q1
course = "CCDM"

#Q2
names=['Dan','Jane','Andy']
#print(course)
#print(names)

#append 3 to CCDM
#updated_course = course + string(3)  #option 1
three = "3"   #option 2
#print(updated_course)  #option 1
#print(course + three)  #option 2
#typecast
three = str(3)   #convert int to string
jp = 'John Pie'
#for index in range (len(jp)):
    #print(jp[index])

#function try-catch error
#define a function

def bad_fun(n):
    return 1/n
try:
    bad_fun(3)   #risky code
except ArithmeticError:
    print("Check number again")
print("The end")

#STACK
stack =[]
#define functions
def push(val):
    stack.append(val)
    
def pop(val):
    val = stack[-1]
    del stack[-1]
    return val

push(3)
print(stack)

push(2)
print(stack)

push(1)
print(stack)

print(pop(stack))
print(stack)

print(pop(stack))
print(stack)