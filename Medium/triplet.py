t=int(input())
while (t>0):
    n=int(input())
    a=list(map(int,input().split()))[:n]
    s=0
    c=0
    cnt=0
    big=[]
    sma=[]
    for i in range(n):
        c=0
        for j in range(n):
            if(a[i]>a[j]):
                c+=1
        sma.append(c)
        cnt=0
        for j in range(n):
            if(a[i]<a[j]):
                cnt+=1
        big.append(cnt)
    print(sma)
    print(big)
    for i in range(n):
        s+=big[i]*sma[i]
    print(s)
    t-=1