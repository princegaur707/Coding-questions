import math
from math import ceil,sqrt
t=int(input())
while t:
    x,k=map(int,input().split())
    def isprime(n):
        if n<=1:
            return 0
        if n<=3:
            return 1
        if n%2==0 or n%3==0 :
            return 0
        for i in range(5,ceil(sqrt(n))+1,6):
            if n%i==0 or n%(i+2)==0:
                return 0
        return 1
    def numdivisors(n):
        cnt=0
        for i in range(1,n+1):
            if(n%i==0):
                cnt+=1
        return cnt
    def divprimecount(n):
        cnt=0
        for i in range(1,n+1):
            if n%i==0:
                if isprime(i):
                    cnt+=1
        return cnt
    for i in range(200):
        if(numdivisors(i)==x):
            if(divprimecount(i)==k):
                print(i)
                break
    t-=1

