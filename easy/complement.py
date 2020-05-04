class Solution:
    def findComplement(self, num: int) -> int:
        n=(bin(num)[2:])
        n=list(n)
        print(n)
        for i in range(len(n)):
            if n[i]=='1':
                n[i]=0
            else:
                n[i]=1
        print(n)
        k=0
        temp=0
        l=len(n)
        for i in range(1,l+1):
            temp+=n[l-i]*(2**k)
            k+=1
        print(temp)
        return temp
            
            
                
        