#from abc import ABCMeta,abstractmethod: for python version below 3.4
#We can't make the object of abstract base class
from abc import ABC, abstractmethod

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

s1=Rectangle() #After decalring object we will get error if don't declare prinarea function in any method 
#because abstract method is saying to must define the print are method  so with this way we can force to have certain function by every method
print(s1.printarea())