#Rectangle class
import math  #math module
class Rectangle:
    def __init__(self,length,width):  #constructor
        self.length = length
        self.width = width

    def calc_area(self):
        return self.length * self.width

    #to calculate PERIMETER, use same variables length and width
    def peri_rect(self):
        return (self.length*2)+(self.width*2)

#Triangle class
class Triangle:
    #1.constructor
    def __init__(self,base,height):
        self.base = base
        self.height = height
    #2.function to do the calculation
    def calc_triangle(self):
        return (self.base*self.height)/2

#Circle Class
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def calc_circle(self):
        return (self.radius*self.radius)*math.pi

    #circumference of circle
    def peri_circle(self):
        return (2*self.radius)*math.pi



first_choice = int(input("I want to calculate:\n1. Perimeter\n2. Area\n"))
if first_choice is 2:
    choices = int(input("Calculate area for:\n1. Rectangle\n2. Triangle\n3. Circle\n"))

    if choices is 1:
        l = int(input("Enter length: "))
        w = int(input("Enter width: "))
        rect_obj = Rectangle(l,w)  
        print("Area for rectangle is: ",rect_obj.calc_area(), " cm squared")
    elif choices is 2:
        b = int(input("Enter base (cm): "))
        h = int(input("Enter height (cm): "))
        tri_obj = Triangle(b,h)
        print("Area for Triangle is ",tri_obj.calc_triangle()," cm squared")
    elif choices is 3:
        r = int(input("Enter radius(cm): "))
        cir_obj = Circle(r)
        print("Area of Circle is: ",cir_obj.calc_circle()," cm squared")

    else:
        print("Invalid choice")
elif first_choice is 1:
    pchoices = int(input("Calculate perimeter for:\n1. Rectangle\n2. Circumference for Circle\n"))

    if pchoices is 1:
        l = int(input("Enter length: "))
        w = int(input("Enter width: "))
        prect_obj = Rectangle(l,w)  
        print("Perimeter for rectangle is: ",prect_obj.peri_rect(), " cm")
    
    elif pchoices is 2:
        r = int(input("Enter radius(cm): "))
        pcir_obj = Circle(r)
        print("Circumference of Circle is: ",pcir_obj.peri_circle()," cm")

    else:
        print("Invalid choice")
else:
    print("invalid choice")



#instantiation - object_name = class()

        
#Triangle class

#3. get user input


#4. Instantiation (creating your object)


