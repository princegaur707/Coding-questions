#Diamond Shape problem
class A:
    var1=9
class B(A):
    var1=8
    pass
class C(A):
    var1=7
class D(B,C): #preference will be given to B as studied earlier
    #var1=6
    pass
d=D()
print(d.var1)