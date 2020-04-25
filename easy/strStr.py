class Solution:
    def strStr(self, haystack, needle):
        if needle == "" and haystack == "":
            return 0
        elif haystack == "":
            return -1
        elif needle == "":
            return 0
        elif len(needle) > len(haystack):
            return -1
        for i in range(len(haystack)):
            if i + len(needle) > len(haystack):
                break
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1
obj=Solution()
print(obj.strStr(haystack = "hello", needle = "ll"))