class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        
        if n == 0:
            return 0
        if h < n:
            return -1
        
        for index in range(h-n+1):
            if haystack[index:index+n] == needle:
                return index
        return -1
obj=Solution()
print(obj.strStr(haystack = "hello", needle = "ll"))
