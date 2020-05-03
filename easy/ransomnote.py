class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        str1=Counter(ransomNote)
        str2=Counter(magazine)
        for i in str1:
            if  str1[i]<=str2[i]:
                pass
            else:
                return False
        return True