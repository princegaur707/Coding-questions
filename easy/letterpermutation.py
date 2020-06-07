class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
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