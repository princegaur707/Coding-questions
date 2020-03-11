class Employee:
    leaves=8
    def __init__(self,aname, asalary):
        self.name=aname
        self.salary=asalary
    def printdetails(self):
        return f"name is {self.name} salary is {self.salary}"

    def __add__(self,other):# Special method known as Dunder add : it is helping us to manage operator overloading
        return self.salary+other.salary

emp1=Employee("Harry",1000)
emp2=Employee("Larry",200)
print(emp1+emp2)
