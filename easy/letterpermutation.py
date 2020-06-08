class Solution:
    def letterCasePermutation(self,S):
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
                print("tmp:",tmp)
            res = tmp
            print(res)
        return res

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        return set(map(''.join, itertools.product(*((c.upper(), c.lower()) for c in S))))


obj=Solution()
print(obj.letterCasePermutation("12a34b"))
