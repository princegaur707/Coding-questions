#https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3290/
class Solution:
    def middleNode(self, head):
        fast = slow = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        return slow
obj=Solution()
obj.middleNode([1,2,3,4,5])