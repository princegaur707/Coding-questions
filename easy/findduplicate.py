import statistics
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return statistics.mode(nums)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums=Counter(nums)
        for key,value in nums.items():
            if value>=2:
                return key

class Solution:
    
    def findDuplicate(self, nums):
        slow = fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            print("slow,fast:",slow,fast)
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

obj=Solution()
print(obj.findDuplicate([3,1,3,4,2]))
