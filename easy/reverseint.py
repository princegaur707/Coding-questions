class Solution:
    def reverse(self, x: int) -> int:
        parity=1
        if x < 0:
            parity=-1
        raw_x = str(abs(x))
        rev_x = ''.join([i for i in reversed(raw_x)])
        res =  int(rev_x) * parity
        if (res < (-2**31)) or res > ((2**31)-1):
            res = 0 
        return res
obj=Solution()
print(obj.reverse(-123))