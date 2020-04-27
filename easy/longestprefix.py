class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        rez = ''
        for letter in zip(*strs):
            if len(set(letter)) == 1:
                rez += letter[0]
            else:
                break
        return rez
obj