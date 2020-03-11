#Public, protected & public specifiers
class Employee:
    leaves=8
    _protec=8      #Declaring protected variable
    __private=10    #Declarting private variable

    def __init__(self,aname, asalary):
        self.name=aname
        self.salary=asalary

harry= Employee("Harry",555) 
print(harry._protec)
#print(harry.__private) It throws error 
print(harry._Employee__private)  #This is name as name angling python done this so as to make user to remember it is private