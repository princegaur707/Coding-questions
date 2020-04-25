import re
class Solution:
    def myAtoi(self, s):
        ls = re.findall('^[+-]?\d+',s.lstrip()) #lstrip(): removes all leading whitespace from left side of the string
        if ls:
            return min(max(int(ls[0]),-2**31),2**31-1)
        else:
            return 0
obj=Solution()
print(obj.myAtoi("4193 with words"))
print(obj.myAtoi("-43"))