#To use class method as an alternative constructor
#Advantage: We can bypass the requirements of the constructor and pass the arguments in any wish but we need to make 
#available such constructor which can accept and make it such 
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
#karan=Employee("Karan-557-student") this line throws error without class method as a constructor
karan=Employee.from_str("Karan-557")
print(karan.salary)