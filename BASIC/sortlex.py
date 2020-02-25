a=['a','b','ab','aab','abb','aba','acc']
print(a)
for i in range(1,len(a)):
    if(len(a[i-1])>len(a[i])):#logn
        a[i-1],a[i]=a[i],a[i-1]
    elif(len(a[i-1])==len(a[i])):
        a.sort(i-1,i)
print(a)