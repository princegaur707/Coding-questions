class Solution:
    def letterCasePermutation(S):
        res = [S]
        l=len(S)
        for i in range(l):
            if S[i].isdigit():
                continue
            tmp = []
            for r in res:
				# the growing part
                tmp.append(r[:i] + r[i].upper() + r[i + 1:])
                tmp.append(r[:i] + r[i].lower() + r[i + 1:])
            res = tmp
        return res

obj=Solution()
obj.letterCasePermutation("12a34b")