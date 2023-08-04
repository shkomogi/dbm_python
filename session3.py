#exception exercise
from xml.dom.expatbuilder import InternalSubsetExtractor


#try:
   # x = int(input("Please enter the first number:"))
   # y = int(input("Please enter second number:"))
   # z = x/y
   # print(z)
#except ValueError:
   # print("Invalid number entered")
#except ZeroDivisionError:
  #  print("Cannot divide with zero value")

#interest function
#define calc_interest
def calc_interest(amount, year, rate):
    try:
        if rate>100:
            raise ValueError(rate)
        interest = (amount * year * rate)/100
        print("Simple interest is: ",interest)
        return interest 
    except ValueError:
        print("interest rate is out of range")

#call the function for Q1
#print(calc_interest(8000,2,10))
#ans = calc_interest(8000,2,10)
#print(ans)

#Q2
#ans2 = calc_interest(20000,4,8)
#print(ans2)

#Q3
#ans3 = calc_interest(20000,4,800)
#print(ans3)

#Dictionary
cars = {"brand":"Ford","model":"Mustang","Year":1964}
print(cars)

    
        
        
