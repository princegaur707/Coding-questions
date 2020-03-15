#object introspection: to know about object(class,type,storing etc)
class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        
    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    
    @property   #decorator being used when we wanna get new fname or lname without parenthesis(encapsulation) eg. access with email not email()
    def email(self):
        if(self.fname==None or self.lname==None):
            return("Email is not set already")
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter           #being used when we wanna change email but it is not directly in form of fname and lname
    def email(self,string):
        names=string.split("@")[0]#It will take the first element of the list formed
        self.fname,self.lname=names.split(".")

    @email.deleter      #to delete the email 
    def email(self):
        self.fname=None #For deleting we just set it to None
        self.lname=None

skillf= Employee("Skill","N")
print(type(skillf))
print(id(skillf)) #every object is given unique id
print(dir(skillf)) #will give all functions we can do 
print("_____________________________________________________________________________________________________________________________________________________________________________________________________")
import inspect
print(inspect.getmembers(skillf))