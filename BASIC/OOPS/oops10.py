#Multi level Inheritance
class Employee:
    leaves=8
    def __init__(self,aname, asalary):
        self.name=aname
        self.salary=asalary
    def printdetails(self):
        return f"name is {self.name} salary is {self.salary}"

class Player():
    leaves=9
    def __init__(self,aname,agame):
        self.name=aname
        self.game=agame
    def printplayer():
    return f"Player name is: {name} Game name is: {game}"

class Coolprogrammer(Player,Employee):# variables of that class whose name is coming ahead will overwrite to that of other in case of same name
    #leaves=10    It can overwrite all other values 
    def printprog(self):
        return f"Programmer's name is {self.name} and Salary is {self.game}"

harry= Employee("Harry",555) 
larry=Employee("Larry",556)
jerry=Coolrogrammer("Jerry",["tennis","Football"])
print(jerry.printprog)
print(jerry.leaves)

