#Class : Template
#object : instance of the class
#Why to make Class?
#Python follow DRY: Don't repeat yourself
#To restrict the access of some functions or objects
# #self refers to the instance calling the method.
# you should know that it is not necessary to write self as a word.
# koky=Cat('white', 4)
# now in the class itself 
# class Cat:
#          def__init__( myobject, color, legs) :
#                   myobject.catcolor = color 
#                   myobject.catlegs = legs

# here koky is just referring to the object of the class  by using myobject
class Student: #Try to name class with capital letter
    pass    #to not to get the error

harry=Student()
harry.std=12
harry.section=1
larry=Student()
print(harry,larry) # will be saved at different locations
print(harry.std)
print(harry.section)
