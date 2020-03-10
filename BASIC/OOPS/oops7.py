#For one line shortcut we are using args and kwargs
class Employee:
    leaves=8
    def __init__(self,aname, asalary):
        self.name=aname
        self.salary=asalary
    def printdetails(self):
        return f"name is {self.name} salary is {self.salary}"

    @classmethod
    def change_leaves(cls,newleaves): 
        cls.leaves=newleaves
    @classmethod
    def from_str(cls,string):
        params=string.split("-")
        return cls(params[0],params[1])
harry= Employee("Harry",555) 
larry=Employee("Larry",556)
karan=Employee.from_str("Karan-557")
print(karan.salary)