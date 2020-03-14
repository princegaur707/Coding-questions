#abstract class :
#advantage: when u want any function or functions must to have by every method then this can be used
#We can't make the object of abstract base class
from abc import ABC, abstractmethod#from abc import ABCMeta,abstractmethod: for python version below 3.4

class Shape(ABC): #class Shape(metaclass=ABCMeta):for python version below 3.4
    @abstractmethod # Abstract method is must to have by everyone
    def printarea(self):
        return 0

class Rectangle(Shape):
    type="Rectangle"
    sides=4
    def __init__(self):
        self.length=6
        self.bredth=7

    def printarea(self):
        return self.length * self.bredth

s1=Rectangle() #After decalaring object we will get error if don't declare prinarea function in any method 
#because abstract method is saying to must define the print are method  so with this way we can force to have certain function by every method
print(s1.printarea())