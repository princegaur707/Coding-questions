# expalains use of self keyword
class Employee:
    leaves=8
    def printdetails(self): #self is that instance or object about which we are talking
        return f"name is {self.name} salary is {self.salary}" #self can also be understood as way to refer to current object

harry=Employee()
larry=Employee()

harry.name='Harry'
harry.salary=455
harry.role="Instructor"

larry.name="Larry"
larry.salary=4554
larry.role="Student"

print(larry.printdetails()) #automatically larry is going as an argument and self in using it 
# if we will remove self then it will say no argument expected but one was given

