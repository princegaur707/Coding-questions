#https://www.codechef.com/APRIL20B/problems/COVIDLQ
import re
t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    arr=[]
    for i in range(len(a)):
        if(a[i]==1):
            arr.append(i)
    print(arr)
    for i in range(1,len(arr)):
        if(arr[i]-a[i-1]+1<6):
            print(arr[i-1])
            print(arr[i])
            print(arr[i]-a[i-1])
            print("NO")
            c=1
            break
    if(c==0):
        print("YES")
    t-=1