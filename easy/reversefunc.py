t=int(input())
while(t>0):
    n=int(input("Number: "))
    a=list(map(int,input("Enter elements:").strip().split()))[:n]
    print(f"Original List {a}")
    print(a[2])
    for i in range(n//2):
        a[i],a[n-i-1]=a[n-i-1],a[i]
        print(a[i],a[n-i-1])
    print(f"Updated List {a}")
    t-=1