class Solution:
    def longestCommonPrefix(self, strs):
        rez = ''
        print("zip(strs):",list(zip(*strs)))
        for letter in zip(*strs):
            print(letter)
            if len(set(letter)) == 1:
                rez += letter[0]
            else:
                break
        return rez
obj=Solution()
print(obj.longestCommonPrefix(["flower","flow","flight"]))