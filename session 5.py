#map function exercise
#step 1 - define function
def id_generator(n):
    year = str(input("Enter year: "))
    sprint = str(input("Enter sprint: "))
    courseid = str(input("Enter to course id:"))
    y = (year+sprint+courseid+n)
    return y     
#now the ITERABLE which is a list
enrollment_list = ["1","2","3"]

#the actual MAP function
yy = map(id_generator,enrollment_list)
print(list(yy))
