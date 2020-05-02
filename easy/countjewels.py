#https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3317/
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count=0
        ref=Counter(S)
        for i in J:
            if ref[i]>0:
                count+=ref[i]
        return count


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for i in S:
            if i in J:
                count += 1
        return count