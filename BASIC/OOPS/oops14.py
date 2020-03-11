#overriding and use of super()
#Sequence: ins. variable of B-> ins. variable of A -> variable of B-> variable of A
class A:
    classvar1="I am a class variable in class A"
    def __init__(self):
        self.var1="I am inside class A's constructor"
        self.classvar1="Instance var in class A" #firstly instantaneous variable in searched

class B(A):
    classvar1="I am a class variable in class B"
    classvar2="I am in class B"
    def __init__(self): #this will overwrite so above constructor will not run so we require super()
        super().__init__()
        #self.classvar1="Instance var in class B"
        pass

a=A()
b=B()
print(b.classvar1)
