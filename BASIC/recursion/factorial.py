def factorial(n):
    if(n==1):
        return(1)
    else:
        return(n* factorial(n-1))
n=int(input("Enter the number: "))
print(factorial(n))
"""
Iterative approach:- 
fact=1
 for i in range (1,n):
     fact=fact*i
return(fact)
"""
        