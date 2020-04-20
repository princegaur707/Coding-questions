def productExceptSelf(nums, m):
    f=[]
    for j in range(len(nums)):
        fa=1
        for i in range(len(nums)):
            if(j!=i):
                fa*=nums[i]
        f.append(fa)
        print(f)
    for i in range(len(f)):
        f[i]=f[i]%m
    g=sum(f)
    return (g%m)    
while(True):
    try:
        print("Enter list elements:")
        ls=list(map(int,input().split()))
        m=int(input("Enter m:"))
        print(productExceptSelf(ls,m))
    except:
        print("That was invalid input!")
        break


