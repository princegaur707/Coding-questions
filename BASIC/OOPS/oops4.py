# Advantage of contructor: automatically initializes with some arguments
class Employee:
    def __init__(self,aname, asalary):
        self.name=aname
        self.salary=asalary
    def printdetails(self):
        return f"name is {self.name} salary is {self.salary}"

harry= Employee("Harry",555) # arguments can be passed due to constructor
print(harry.printdetails())