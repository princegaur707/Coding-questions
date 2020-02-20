def fibonacci(n):
    if(n<=1):
        return(0)
    elif(n==2):
        return(1)
    else:
        return(fibonacci(n-2)+fibonacci(n-1))
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(fibonacci(i),end=" ")