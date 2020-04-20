t=int(input())
while (t>0):
    n=int(input())
    a=list(map(int,input().split()))[:n]
    s=0
    for i in range(0,len(a),1):
        ss=sg=0
        j=i-1
        while(j>=0): 
            if(a[i]>a[j]): 
                ss+=1
            j-=1
        j=i+1
        while(j<n):
            if(a[i]<a[j]): 
                sg+=1
            j+=1
        s+=ss*sg
    print(s)
    t-=1