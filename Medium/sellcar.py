t=int(input())
while t:
    s=k=i=0
    n=int(input())
    a=list(map(int,input().split()))
    while i<n:
        if(a[i]-k>0):
            s+=a[i]-k
            k+=1
        i+=1 
    print(s)
    t-=1