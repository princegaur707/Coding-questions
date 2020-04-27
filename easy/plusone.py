#https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/559/
class Solution:
    def plusOne(self, digits):
        if digits[-1]!=9:
            digits[-1]+=1
        else:
            digits[-1]=0
            c=1
            for i in range(len(digits)-2,-1,-1):
                if c:
                    if digits[i]!=9:
                        digits[i]+=1
                        c=0
                    else:
                        digits[i]=0
            if c:
                digits.insert(0,1)
        return digits
obj=Solution()
print(obj.plusOne([9,9,9]))
