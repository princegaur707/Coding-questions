#static method :
#Advantage: In this too we are not using self so increasing efficiency
class Employee:
    leaves=8
    def __init__(self,aname, asalary):
        self.name=aname
        self.salary=asalary
    def printdetails(self):
        return f"name is {self.name} salary is {self.salary}"
   
    @staticmethod
    def printsome(string):
        print(f"You are good {string}")

harry= Employee("Harry",555) 
larry=Employee("Larry",556)
karan=Employee.printsome("Karan")