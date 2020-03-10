#Class : Template
#object : instance of the class
#Why to make Class?
#Python follow DRY: Don't repeat yourself
#To restrict the access of some functions or objects
class Student:
    pass    #to not to get the error

harry=Student()
harry.std=12
harry.section=1
larry=Student()
print(harry,larry) # will be saved at different locations
print(harry.std)
print(harry.section)
