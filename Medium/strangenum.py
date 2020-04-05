import math
from math import ceil,sqrt
arr=[]
t=int(input())
while t:
    x,k=map(int,input().split())
    def chkprime(n):
        if n<=1:
            return False
        if(n<=3):
            return True
        if(n%2==0 or n%3==0):
            return False
        for i in range(1,ceil(sqrt(n))+1,6):
            if n%i==0 or n%(i+2)==0:
                return False
        return True
    def numdivisors(n):
        cnt=0
        arr.clear()
        for i in range(1,int(math.sqrt(n)+1)):
            if(n%i==0):
                if n/i==i:
                    cnt+=1
                    arr.append(i)
                else:
                    cnt+=2
                    arr.append(i)
                    arr.append(n/i)
        #print("Number of divisors:",cnt)
        #print("divisors array",arr)
        return cnt
    def primecount():
        cnt1=0
        for i in range(len(arr)):
            if(chkprime(arr[i])):
                cnt1+=1
        #print("Number of primes:",cnt1)
        return cnt1
    c=0
    for i in range(1,100):
        #print("\ncurrent number:  ",i)
        if(numdivisors(i)==x):
            if(primecount()==k):
                c=1
                print(1)
                break
    if(c==0):
        print(0)
    t-=1

