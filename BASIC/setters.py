#setter and decorators
class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        
    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    
    @property
    def email(self):
        if(self.fname==None or self.lname==None):
            return("Email is not already set")
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self,string):
        names=string.split("@")[0]#It will take the first element of the list formed
        self.fname,self.lname=names.split(".")
        
    @email.deleter
    def email(self):
        self.fname=None #For deleting we just set it to None
        self.lname=None

suppor=Employee("Prince","Gaur")
suppor1=Employee("A","B")
print(suppor1.email)#no need to apply parenthesis after using property decorator
suppor1.fname='C'
suppor1.email="this.is@gmail.com" #email.setter will do this
print(suppor1.email)
del suppor1.email
print(suppor1.email)
