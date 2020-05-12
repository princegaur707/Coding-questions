class Solution:
    def findJudge(self, N: int, trust):
        trusted = [0] * (N+1)
        for a, b in trust:
            trusted[a] -= 1
            trusted[b] += 1
            print(trusted)
        for i in range(1, N+1):
            if trusted[i] == N-1:
                return i
        return -1
obj=Solution()
print(obj.findJudge(3,[[1,2],[2,3]]))
print(obj.findJudge(3,[[1,3],[2,3]]))
