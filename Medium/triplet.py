t=int(input())
while (t>0):
    n=int(input())
    a=list(map(int,input().split()))[:n]
    s=0
    big=[]
    sma=[]
    for i in range(n):
        s=0
        for j in range(n):
            if(a[i]>a[j]):
                s+=1
        sma.append(s)
        s=0
        for j in range(n):
            if(a[i]<a[j]):
                s+=1
        big.append(s)
    print(sma)
    print(big)
    for i in range(n):
        s+=big[i]*sma[i]
    print(s)
    t-=1