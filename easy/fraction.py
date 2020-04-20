def fraction(a,b):
    cnt1=a[1]*b[0]-a[0]*b[1]
    cnt2=a[1]*b[1]
    def gcd(cnt1,cnt2):
        if(cnt2==0):
            return cnt1
        return gcd(cnt2,cnt1%cnt2)
    g=gcd(cnt1,cnt2)
    return(cnt1/g,cnt2/g)
n=fraction([7,10],[2,5])
print(n)

