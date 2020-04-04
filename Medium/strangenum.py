t=int(input())
while t:
    x,k=map(int,input().split())
    arr=[]
    c=0
    def isprime(n):
        if(n<=1):
            return False
        if(n<=3):
            return True
        if(n%2==0 or n%3==0 or n%5==0):
            return False
        for i in range(5,ceil(sqrt(n)),6):
            if(n%i==0 or n%(i+2)==0):
                return False
        return True
        
    for i in range x**10*k:
        for j in range i:
            if(i%j==0):
                cnt+=1
                arr.append(j)
                if(cnt>x):
                    break
    if(cnt==x):
        for i  in range(len(arr)):
            if(isprime(arr[i])):
                cnt1+=1
        if(cnt1==k):
            print(1)
            c=1
    if(c==0):
        print(0)