#Recursive approach
def factorial(n):
    if(n==0):
        return(1)
    else:
        return(n*factorial(n-1))
while True:
    n=int(input("Enter the number: "))
    print(factorial(n))


"""
Iterative approach:- 
fact=1
 for i in range (1,n):
    fact=fact*i
return(fact)
"""
        