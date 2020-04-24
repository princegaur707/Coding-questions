#https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/881/
class Solution:
    def firstUniqChar(self, s):
        see=Counter(s)
        for i in see:
            if see[i]==1:
                return(s.index(i))
        return -1
obj=Solution()
print(obj.firstUniqChar("leetcode"))
print(obj.firstUniqChar("loveleetcode"))