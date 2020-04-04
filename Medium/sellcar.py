t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    for i in range(len(a)):
        if(a[i]-i >0):
            a[i]-=i
        else:
            a[i]=0
    print(sum(a)%(10**9+7))
    t-=1