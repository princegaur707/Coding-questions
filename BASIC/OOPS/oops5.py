# Advantage of class method: to speed up the process of changing the class variables b/c latency is very imp.
#cls is that class whose instance is that object from which it's function is called
#It is faster as it is having access only to that specific argument as compared to 
#self which firstly checks in different methods which is relatively slow
class Employee:
    leaves=8
    def __init__(self,aname, asalary):
        self.name=aname
        self.salary=asalary
    def printdetails(self):
        return f"name is {self.name} salary is {self.salary}"

    @classmethod
    def change_leaves(cls,newleaves): #self in not required, cls is that class whose instance is that object with which this function is called
        cls.leaves=newleaves

harry= Employee("Harry",555) # arguments can be passed due to constructor
print(harry.leaves)
harry.change_leaves(30)
print(harry.leaves)