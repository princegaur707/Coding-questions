t=int(input("Enter no. of iterations: "))
while(t):
    
    n=int(input("Enter no of rows: "))
    b=int(input("Enter choice: "))
    if(bool(b)==True):
        
        for i in range(n):
            print("*" * (i+1), end ="")
            print("\n")
    else :
        for i in range(n):
            print("*"*(n-i), end="")
            print("\n")
    t-= 1