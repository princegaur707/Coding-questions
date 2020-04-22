class Solution:
    def plusOne(self, digits):
        k=num=0
        for i in digits:
            num+=10**k*i
            k+=1
        num+=1
        ans=[]
        while num>0:
            ans.append(num%10)
            num//=10
        return ans