#Inheritance
class Employee:
    leaves=8
    def __init__(self,aname, asalary):
        self.name=aname
        self.salary=asalary
    def printdetails(self):
        return f"name is {self.name} salary is {self.salary}"
class programmer(Employee):
    def printprog(self):
        return f"Programmer's name is {self.name} and Salary is {self.salary}"

harry= Employee("Harry",555) 
larry=Employee("Larry",556)
jerry=programmer("Jerry",777)
print(jerry.printdetails())
print(jerry.printprog())

